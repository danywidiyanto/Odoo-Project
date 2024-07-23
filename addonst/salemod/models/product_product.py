from odoo import models, fields

class ProductProduct(models.Model):
    _inherit = 'product.product'

    sale_order_line_ids = fields.One2many('sale.order.line', 'product_id', string='Sales Order Lines')
