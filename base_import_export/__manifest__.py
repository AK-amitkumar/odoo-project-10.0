# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Auth: Gavin GU Email:guwenfengvip@163.com
{
    "name": "数据导入导出权限管理",
    'author': "Gavin Gu",
    'website': "",
    'category': 'Tools',
    'version': '1.0',
    "summary": "数据导入导出权限管理",
    "description": """
    """,
    "depends": [
        'web',
        'base_import'
    ],
    "data": [
        'security/data_impexp_security.xml',
        'views/webclient_templates.xml',
    ],
    "installable": True,
}
