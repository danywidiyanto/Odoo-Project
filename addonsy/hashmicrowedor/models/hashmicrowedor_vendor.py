from odoo import _, api, fields, models, tools
# models/vendor.py

# class Vendor(models.Model):
#     _inherit = 'res.partner'
#     _description = 'Vendor Information'

#     vendor_category = fields.Selection([
#         ('catering', 'Catering'),
#         ('venue', 'Venue'),
#         ('photography', 'Photography'),
#         ('entertainment', 'Entertainment'),
#         ('other', 'Other')
#     ], string='Vendor Category')
#     vendor_services = fields.Many2many('product.template', string='Services Offered',
#                                        domain=[('type', '=', 'service')])
