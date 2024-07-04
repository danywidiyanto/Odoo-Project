# models/payments.py

from odoo import models, fields

# class Payments(models.Model):
#     _inherit = 'account.payment'
#     _description = 'Payment Information'

#     wedding_id = fields.Many2one('custom_wedding.weddings', string='Wedding')
#     payment_status = fields.Selection([
#         ('pending', 'Pending'),
#         ('paid', 'Paid'),
#         ('late', 'Late'),
#         ('cancelled', 'Cancelled')
#     ], string='Payment Status', default='pending')
