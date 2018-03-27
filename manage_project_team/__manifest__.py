# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Auth: Gavin GU Email:guwenfengvip@163.com
{
    'name': '项目团队管理',

    'summary': '项目团队管理',
    'category': 'Project Management',
    'description': """
   * 建立项目团队

       """,
    'author': 'Gavin Gu',
    'website': "",

    'version': '1.0',
    'depends': ['project', 'crm', 'web'],
    'data': [
        'views/template.xml',
        'views/project_team_view.xml',
    ],
    'installable': True,
    'auto_install': False
}
