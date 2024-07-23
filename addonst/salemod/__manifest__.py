{
    'name': "salemod",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock', 'product', 'purchase','sale','crm','report_xlsx'],

    # always loaded
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence.xml",
        "data/scheduled_action.xml",
        "views/sale_order_views.xml",
        "views/menu.xml",
        "views/product_template_views.xml",
        "views/booking_config_views.xml",
        "views/booking_order_pivot_views.xml",
        'wizard/purchase_order_report_wizard_views.xml',
        'wizard/booking_order_report_wizard_views.xml',
        'wizard/purchase_order_report_wizard_xlsx_views.xml',
        'wizard/booking_order_report_wizard_xlsx_views.xml',
        'report/purchase_order_report.xml',
        'report/purchase_order_report_template.xml',
        'report/booking_order_report_template.xml',
    ],
    'installable': True,
    'application': True,
}
# -*- coding: utf-8 -*-
