from odoo import models, fields

class PurchaseBookingOrder(models.Model):
    _name = 'purchase.booking.order'
    _description = 'Purchase Booking Order'

    date_order = fields.Datetime('Order Date')
    partner_id = fields.Many2one('res.partner', 'Customer')
    amount_total = fields.Float('Total Amount')
    date_planned= fields.Datetime('Confirmation  Date')
 
    # state = fields.Selection([
    #     ('draft', 'Quotation'),
    #     ('sent', 'Quotation Sent'),
    #     ('sale', 'Sales Order'),
    #     ('done', 'Locked'),
    #     ('cancel', 'Cancelled')
    # ], string='Status')

    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW booking_order_pivot AS (
                SELECT
                    po.id,
                    po.date_order,
                    po.partner_id,
                    po.date_planned,
                    po.amount_total
                FROM
                    purchase_order po
                WHERE
                    po.is_booking = TRUE
            )
        """)
