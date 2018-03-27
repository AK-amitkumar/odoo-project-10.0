# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Auth: Gavin GU Email:guwenfengvip@163.com
{
    'name': '业务伙伴地图',
    'category': 'website',
    'description': """
    主要内容:
    ----------------
    * 配置全局参数用于地图API，
    * 根据业务伙伴的地址显示百度地图坐标
    * 在首页显示本公司的地图坐标
        """,
    'version': '1.0',
    'author': 'Gavin Gu',
    'website': '',
    'data': [
        "views/layoutone.xml",
        "views/res_company.xml",
    ],
    'category': 'Contact Baidu Map',
    'depends': ['website'],
}
