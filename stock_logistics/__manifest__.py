# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Auth: Gavin GU Email:guwenfengvip@163.com
{
    'name': "物流管理",

    'summary': """
        物流管理--快递鸟平台应用
        """,

    'description': """
       单号识别
       即时查询
       预约取件
       电子面单
       物流跟踪
    """,

    'author': "Gavin Gu",
    'website': "http://www.qitongyun.cn/",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'delivery', ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/message_log.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'active': False,
    'application': False,
}
