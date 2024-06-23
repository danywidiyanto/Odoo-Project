from odoo import models, fields, api
from odoo.exceptions import ValidationError

class WeddingBookingCateringLine(models.Model):
    _name = 'hashmicrowedor.booking.catering.line'
    _description = 'Wedding Booking Catering Line'

    booking_id = fields.Many2one('hashmicrowedor.booking', string='Booking', required=True, ondelete='cascade')
    catering_id = fields.Many2one('hashmicrowedor.catering', string='Catering', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    price = fields.Float(string='Price', compute='_compute_price', store=True)

    @api.depends('catering_id', 'quantity')
    def _compute_price(self):
        for line in self:
            line.price = line.catering_id.price_per_person * line.quantity

    @api.constrains('quantity')
    def _check_quantity(self):
        for line in self:
            if line.quantity < line.catering_id.min_order:
                raise ValidationError(f"Catering order must be at least {line.catering_id.min_order} portions.")

class WeddingBookingVenueLine(models.Model):
    _name = 'hashmicrowedor.booking.venue.line'
    _description = 'Wedding Booking Venue Line'

    booking_id = fields.Many2one('hashmicrowedor.booking', string='Booking', required=True, ondelete='cascade')
    venue_id = fields.Many2one('hashmicrowedor.venue', string='Venue', required=True)
    price = fields.Float(string='Price', related='venue_id.price', store=True)
