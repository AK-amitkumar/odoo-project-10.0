# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Auth: Gavin GU Email:guwenfengvip@163.com
{
    'name': "import_data_by_fields",

    'summary': """
        导入时可指定某些字段来查询更新""",

    'description': """
        导入时可指定某些字段来查询更新
    """,

    'author': "Gavin GU ",
    'website': "",
    'license': 'AGPL 3.0',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Toosl',
    'version': '0.1',

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
    ],
    'qweb': ['static/src/*.xml'],

    # any module necessary for this one to work correctly
    'depends': ['base_import'],
}
