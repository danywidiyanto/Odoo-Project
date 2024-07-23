from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    validity_datetime = fields.Datetime(string='Validity Date')
    due_date = fields.Char(string='Due Date', compute='_compute_due_date', store=True)

    discount = fields.Float(string='Discount (%)', digits='Discount', default=0.0)
    final_price = fields.Monetary(string='Final Price', compute='_compute_final_price', store=True)

    @api.depends('validity_datetime', 'date_order')
    def _compute_due_date(self):
        for order in self:
            if order.validity_datetime and order.date_order:
                validity_datetime = fields.Datetime.from_string(order.validity_datetime)
                date_order = fields.Datetime.from_string(order.date_order)
                delta = validity_datetime - date_order
                order.due_date = f'{delta.days} days'
            else:
                order.due_date = False

    @api.depends('amount_total', 'discount')
    def _compute_final_price(self):
        for order in self:
            order.final_price = order.amount_total * (1 - (order.discount or 0.0) / 100)
