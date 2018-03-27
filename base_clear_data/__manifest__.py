# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Auth: Gavin GU Email:guwenfengvip@163.com
{
    'name': "清除业务数据",

    'summary':
        """
            清除数据
        """,

    'description':
        """
            自定义清除业务数据     
       """,

    'author': 'Gavin Gu.',
    'website': "",
    "license": "AGPL-3",
    'category': 'Tools',
    'version': '0.1',

    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv'
    ],

}
