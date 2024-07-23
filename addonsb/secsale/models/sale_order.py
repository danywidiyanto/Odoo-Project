from odoo import _, api, fields, models, tools

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'SaleOrder'

    partner_id = fields.Many2one('res.partner', string='Customer')
    opportunity_id = fields.Many2one('crm.lead', string='Opportunity')
    user_id = fields.Many2one(comodel_name='res.users', string='Customer', readonly=True, default=lambda self: self.env.user)
    
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _description = 'SaleOrderLine' 