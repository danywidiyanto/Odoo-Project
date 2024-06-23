from odoo import models, fields, api
from odoo.exceptions import ValidationError

class WeddingBooking(models.Model):
    _name = 'hashmicrowedor.booking'
    _description = 'Wedding Booking'

    client_id = fields.Many2one('hashmicrowedor.client', string='Client', required=True)
    booking_date = fields.Date(string='Booking Date', required=True)
    catering_line_ids = fields.One2many('hashmicrowedor.booking.catering.line', 'booking_id', string='Catering Lines')
    venue_line_ids = fields.One2many('hashmicrowedor.booking.venue.line', 'booking_id', string='Venue Lines')
    total_price = fields.Float(string='Total Price', compute='_compute_total_price', store=True)

    @api.depends('catering_line_ids.price', 'venue_line_ids.price')
    def _compute_total_price(self):
        for record in self:
            total_catering = sum(line.price for line in record.catering_line_ids)
            total_venue = sum(line.price for line in record.venue_line_ids)
            record.total_price = total_catering + total_venue

    @api.onchange('booking_date')
    def _onchange_booking_date(self):
        if self.booking_date and self.id:
            existing_bookings = self.search([
                ('booking_date', '=', self.booking_date),
                ('id', '!=', self.id)
            ])
            if existing_bookings:
                return {
                    'warning': {
                        'title': "Booking Date Conflict",
                        'message': "The selected date is already booked. Please choose another date.",
                    }
                }

    @api.constrains('booking_date')
    def _check_booking_date(self):
        for booking in self:
            if booking.booking_date and booking.id:
                existing_bookings = self.search([
                    ('booking_date', '=', booking.booking_date),
                    ('id', '!=', booking.id)
                ])
                if existing_bookings:
                    raise ValidationError("Another booking already exists for this date. Please choose another date.")

    @api.constrains('catering_line_ids', 'venue_line_ids')
    def _check_lines(self):
        for booking in self:
            for catering_line in booking.catering_line_ids:
                if catering_line.quantity < catering_line.catering_id.min_order:
                    raise ValidationError(f"Catering order for '{catering_line.catering_id.name}' must be at least {catering_line.catering_id.min_order} portions.")
