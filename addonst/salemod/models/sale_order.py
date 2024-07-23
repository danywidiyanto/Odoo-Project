from odoo import models, fields, api, _
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_booking = fields.Boolean(string='Is Booking', default=False)
    is_rfq = fields.Boolean(string='Is RFQ', default=False)
    user_id = fields.Many2one(comodel_name='res.users', string='Customer', readonly=True, default=lambda self: self.env.user)

    
    def action_create_rfq(self):
        for record in self:
            if record.is_rfq == True:
                raise ValidationError(f'Product {record.name} already been added to RFQ.')
            sequence_name = self.env['ir.sequence'].next_by_code('request.quotation') or _('New')
            rfq = self.env['purchase.order'].create({
                'partner_id': record.partner_id.id,
                'date_order': fields.Datetime.now(),
                'name': sequence_name,
                'is_booking': True,
                'order_line': [(0, 0, {
                    'product_id': line.product_id.id,
                    'name': line.name,
                    'product_qty': line.product_uom_qty,
                    'price_unit': line.price_unit,
                    'date_planned': fields.Datetime.now(),
                }) for line in record.order_line]
            })
            self.is_rfq = True
            return {
                'name': 'RFQ Created',
                'type': 'ir.actions.act_window',
                'res_model': 'purchase.order',
                'res_id': rfq.id,
                'view_mode': 'form',
                }
        
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            if vals.get('is_booking'):
                sequence_code = 'booking.order'
            else:
                sequence_code = 'sale.order'
            vals['name'] = self.env['ir.sequence'].next_by_code(sequence_code) or _('New')
        res = super(SaleOrder, self).create(vals)
        return res

    @api.model
    def cancel_unprocessed_orders(self):
        three_days_ago = datetime.now() - timedelta(days=3)
        orders_to_cancel = self.search([('state', '=', 'draft'), ('create_date', '<=', three_days_ago)])
        for order in orders_to_cancel:
            order.action_cancel()


        

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    qty_booking = fields.Float(string='Quantity Booking', default=1.0)
    user= fields.Many2one(comodel_name='res.users', string='Customer', readonly=True, default=lambda self: self.env.user)
    check_group = fields.Boolean(string='Check Group', compute="_compute_check_group")

    @api.onchange('qty_booking')
    def _onchange_qty_booking(self):
        if self.qty_booking:
            self.product_uom_qty = self.qty_booking

    @api.depends('order_id.is_booking', 'product_id.lst_price')
    def _compute_price_unit(self):
        for line in self:
            if line.order_id.is_booking:
                line.price_unit = line.product_id.lst_price * 1.1  
            else:
                line.price_unit = line.product_id.lst_price
    @api.model
    def create(self, vals):
        if vals.get('order_id') and self.env['sale.order'].browse(vals.get('order_id')).is_booking:
            vals['price_unit'] = vals.get('price_unit', 0) * 1.1
        return super(SaleOrderLine, self).create(vals)

    def write(self, vals):
        if 'order_id' in vals:
            order = self.env['sale.order'].browse(vals['order_id'])
            if order.is_booking:
                if 'price_unit' in vals:
                    vals['price_unit'] = vals['price_unit'] * 1.1
        return super(SaleOrderLine, self).write(vals)   


    @api.depends('user')
    def _compute_check_group(self):
        for line in self:
            if line.env.user.has_group('salemod.sales_group_admin'):
                line.check_group = True
            else:
                line.check_group = False
    

    def write(self, vals):
        for line in self:
            if 'product_uom_qty' in vals:
                product = line.product_id
                new_qty = vals['product_uom_qty']
                qty_difference = new_qty - line.product_uom_qty
                if qty_difference > 0 and product.qty_available < qty_difference:
                    raise ValidationError(_('Not Enough quantity Available for Product %s') % product.display_name)
                product.qty_available -= qty_difference
        return super(SaleOrderLine, self).write(vals)

    def unlink(self):
        for line in self:
            if line.product_id:
                if line.order_id.is_booking:
                    product = line.product_id
                    product.qty_available += line.product_uom_qty
        return super(SaleOrderLine, self).unlink()

    @api.constrains('qty_booking')
    def _check_product_booking_limit(self):
        for line in self:
            config = self.env['booking.config'].search([('product_id', '=', line.product_id.id)], limit=1)
            if config and line.qty_booking > config.max_booking_per_order:
                raise ValidationError(_('Total booking quantity for this product has reached the limit. %s') % config.max_booking_per_order)
            total_qty = line.product_id.qty_available + (line.product_id.qty_available * config.qty_limit_by_percentage / 100)
            if line.qty_booking > total_qty:
                raise ValidationError('Total booking quantity exceeds the maximum limit by percentage')
