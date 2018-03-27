# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Auth: Gavin GU Email:guwenfengvip@163.com
{
    'name': '超级客服在线',
    'version': '1.0',
    'summary': '设置超级客服',
    'category': 'Website',
    'author': 'Gavin Gu',
    'website': '',
    'description':
        """
        设置超级客服
        无任何活动用户在线时，消息推送给超级客服
        """,
    'data': [
        "views/res_users_views.xml",
    ],

    'depends': ["im_livechat", "website_livechat"],
    'installable': True,
    'auto_install': False,
    'application': False,
}
