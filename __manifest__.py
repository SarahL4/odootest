# -*- coding: utf-8 -*-
{
    'name': "sarahModule",

    'summary': """Kim VVS Service""",

    'description': """
        Professional VVS Service med 30 år erfarenhet!
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': [
    'base',
    'sale',
    'project',
    'account',
    'website',
    'hr',
    'hr_timesheet'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
