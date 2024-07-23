from odoo import models, fields

class BookingConfiguration(models.Model):
    _name = 'booking.config'

    max_booking_per_order = fields.Float(string='Max Booking per Order', required=True)
    qty_limit_by_percentage = fields.Float(string='Quantity Limit by Percentage', required=True)
    product_id = fields.Many2one('product.product', string='Product Template', required=True)



