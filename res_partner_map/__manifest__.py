# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Auth: Gavin GU Email:guwenfengvip@163.com
{
    'name': 'Partner Map',
    'version': '1.0',
    'category': 'MAP',
    'summary': '业务伙伴百度地图',
    'description': '',
    'author': 'Gavin Gu',
    'website': '',
    'depends': [
        'web',
        'purchase',
        'base_setup'
    ],
    'data': [
        "views/map.xml",
        "views/partner_map.xml"
    ],
    "qweb": [
        "static/src/xml/baidu_map.xml"
    ],
    'installable': True,
}
