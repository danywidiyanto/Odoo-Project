# -*- coding: utf-8 -*-
{
    'name': "report_purchase",

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
    'depends': ['base','purchase','report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'data/booking_order_query.sql',
        'views/purchase_booking_order_pivot_views.xml',
        'views/purchase_booking_order_views.xml',
        'wizard/purchase_order_report_wizard_views.xml',
        'wizard/purchase_order_report_wizard_xlsx_views.xml',
        'report/purchase_order_report.xml',
        'report/purchase_order_report_template.xml',
        'report/purchase_order_report_template_xlsx.xml',
    ],
}
