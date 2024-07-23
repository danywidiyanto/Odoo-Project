from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    #booking_order_id = fields.Many2one('purchase.booking.order', string='Booking Order')
    is_booking = fields.Boolean(string='Is Booking?')
    

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    #booking_order_id = fields.Many2one('purchase.booking.order', string='Booking Order')
    qty_booking = fields.Char('Quantity Booking')