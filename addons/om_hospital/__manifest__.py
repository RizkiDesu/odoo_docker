# -*- coding: utf-8 -*-
{
    'name': 'Hospital',
    'version': '1.0.0',
    'summary': 'Odoo 16 Development Tutorials',
    'sequence': -100,
    'description': """Odoo 16 Development Tutorials""",
    'category': 'Hospital',
    'author': 'rizki',
    'maintainer': 'Odoo Mates',
    'website': 'https://www.odoomates.tech',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        # 'security/groups.xml',
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        'views/dokter_list.xml',

    ],

    'aplication':True,

}