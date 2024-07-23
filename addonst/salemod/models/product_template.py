from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    quantity_booking = fields.Float(string='Quantity Booking', compute='_compute_quantity_booking',store=True)
    quantity_after_booking = fields.Float(string='Quantity After Booking', compute='_compute_qty_after_booking')
    order_line_ids = fields.One2many('sale.order.line', 'product_template_id', string='Order Line')

    @api.depends('quantity_booking', 'qty_available')
    def _compute_qty_after_booking(self):
        for template in self:
            template.quantity_after_booking = template.qty_available - template.quantity_booking
    

    @api.depends('product_variant_ids.sale_order_line_ids')
    def _compute_quantity_booking(self):
        SaleOrderLine = self.env['sale.order.line']
        for product in self:
            lines = SaleOrderLine.search([('product_id.product_tmpl_id', '=', product.id)])
            qty = sum(line.qty_booking for line in lines)
            product.quantity_booking = qty
