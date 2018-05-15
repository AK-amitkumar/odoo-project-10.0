# -*- coding: utf-8 -*-

import logging
import json
import urllib2
import urlparse
import werkzeug.urls
import werkzeug.utils
from urllib import urlencode
import odoo
from odoo import fields, models, api
from odoo import http
from odoo import SUPERUSER_ID
from odoo.addons.auth_oauth.controllers.main import fragment_to_query_string
from odoo.addons.auth_oauth.controllers.main import OAuthController
from odoo.addons.auth_signup.models.res_partner import SignupError, now

from odoo.addons.web.controllers.main import login_and_redirect
from odoo.addons.web.controllers.main import set_cookie_and_redirect

from odoo.modules.registry import RegistryManager

_logger = logging.getLogger(__name__)


class OAuthController_extend(OAuthController):

    @http.route('/auth_oauth/signin', type='http', auth='none')
    @fragment_to_query_string
    def signin(self, **kw):
        kw = json.loads(json.dumps(kw).replace('+', ''))
        state = json.loads(kw['state'])
        dbname = state['d']
        provider = state['p']
        context = state.get('c', {})
        registry = RegistryManager.get(dbname)
        with registry.cursor() as cr:
            try:
                env = api.Environment(cr, SUPERUSER_ID, context)
                credentials = env['res.users'].sudo().auth_oauth(provider, kw)
                cr.commit()
                action = state.get('a')
                menu = state.get('m')
                redirect = werkzeug.url_unquote_plus(state['r']) if state.get('r') else False
                url = '/web'
                if redirect:
                    url = redirect
                elif action:
                    url = '/web#action=%s' % action
                elif menu:
                    url = '/web#menu_id=%s' % menu
                return login_and_redirect(*credentials, redirect_url=url)
            except AttributeError:
                # auth_signup is not installed
                _logger.error("auth_signup not installed on database %s: oauth sign up cancelled." % (dbname,))
                url = "/web/login?oauth_error=1"
            except odoo.exceptions.AccessDenied:
                # oauth credentials not valid, user could be on a temporary session
                _logger.info(
                    'OAuth2: access denied, redirect to main page in case a valid session exists, without setting cookies')
                url = "/web/login?oauth_error=3"
                redirect = werkzeug.utils.redirect(url, 303)
                redirect.autocorrect_location_header = False
                return redirect
            except Exception, e:
                # signup error
                _logger.exception("OAuth2: %s" % str(e))
                url = "/web/login?oauth_error=2"

        return set_cookie_and_redirect(url)


class res_users(models.Model):
    _inherit = 'res.users'

    @api.model
    def _auth_oauth_validate(self, provider, access_token):
        """ return the validation data corresponding to the access token """
        oauth_provider = self.env['auth.oauth.provider'].browse(provider)
        if oauth_provider.data_endpoint:
            data = self._auth_oauth_rpc(oauth_provider.data_endpoint, access_token)
        return data

    def _auth_oauth_rpc(self, endpoint, access_token):
        params = werkzeug.url_encode({'access_token': access_token})
        if urlparse.urlparse(endpoint)[4]:
            url = endpoint + '&' + params
        else:
            url = endpoint + '?' + params
        f = urllib2.urlopen(url)
        response = f.read()
        if response.find('callback') == 0:
            response = response[response.index("(") + 1: response.rindex(")")]
        return json.loads(response)

    def _auth_oauth_signin(self, provider, validation, params):

        """ retrieve and sign in the user corresponding to provider and validated access token
            :param provider: oauth provider id (int)
            :param validation: result of validation of access token (dict)
            :param params: oauth parameters (dict)
            :return: user login (str)
            :raise: odoo.exceptions.AccessDenied if signin failed

            This method can be overridden to add alternative signin methods.
        """
        try:
            oauth_uid = validation['id']
            user_ids = self.search([("oauth_uid", "=", oauth_uid), ('oauth_provider_id', '=', provider)])
            if not user_ids:
                raise odoo.exceptions.AccessDenied()
            assert len(user_ids) == 1
            user_ids.write({'oauth_access_token': validation['access_token']})
            return user_ids.login
        except odoo.exceptions.AccessDenied, access_denied_exception:
            state = json.loads(params['state'])
            token = state.get('t')
            oauth_uid = validation['id']
            login = validation['login']
            email = validation.get('email', login)
            name = validation.get('name', login)
            access_token = validation.get('access_token')
            values = {
                'name': name,
                'login': login,
                'email': email,
                'oauth_provider_id': provider,
                'oauth_uid': oauth_uid,
                'oauth_access_token': access_token,
                'active': True,
            }
            _logger.info(values)
            try:
                _, login, _ = self.signup(values, token)
                return login
            except SignupError:
                _logger.info(SignupError)
                raise access_denied_exception

    def get_access_token(self, params, provider):
        oauth_provider = self.env['auth.oauth.provider'].browse(provider)
        data = {
            'grant_type': str(oauth_provider.scope),
            'client_id': str(oauth_provider.client_id),
            'client_secret': 'c56a3f0c18a96e3df33a528c1378ae5149b96fba',
            'code': str(params['code']),
        }
        headers = {'Accept': 'application/json'}
        url = str(oauth_provider.validation_endpoint)
        req = urllib2.Request(url=url, data=urlencode(data), headers=headers)
        f = urllib2.urlopen(req).read()
        result = json.loads(f)
        return result

    def auth_oauth(self, provider, params):
        access_token = params.get('access_token')
        if access_token:
            validation = self._auth_oauth_validate(provider, access_token)
        else:
            data = self.get_access_token(params, provider)
            access_token = data['access_token']
            validation = self._auth_oauth_validate(provider, access_token)
            validation.update({'access_token': access_token})
        oauth_uid = 'id'
        if not validation.get(oauth_uid):
            raise odoo.exceptions.AccessDenied()
        # retrieve and sign in user
        login = self._auth_oauth_signin(provider, validation, params)
        if not login:
            raise odoo.exceptions.AccessDenied()
        # return user credentials
        state = json.loads(params['state'])
        return (state['d'], login, access_token)
