# -*- coding: utf-8 -*-
{
    'name': "hashmicrowedor",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu_wo.xml',
        'views/views.xml',
        'wizard/hashmicrowedor_booking_report_wizard.xml',
        'report/report.xml',
        'report/hashmicrowedor_booking_report_template.xml',      
        'views/booking_view.xml',  
        'views/client_view.xml',
        'views/venue_view.xml',
        'views/catering_view.xml',
        'views/budgetting_view.xml',
        'views/templates.xml',
        'views/homepage_view.xml',
        'views/vendor_view.xml',
        'views/payment_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'hashmicrowedor/static/src/css/custom.css',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}