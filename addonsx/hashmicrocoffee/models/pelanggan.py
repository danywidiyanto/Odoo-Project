from odoo import models,fields,api

class Pelanggan(models.Model):
    _inherit = 'res.partner'
    _description = 'Pelanggan'

    user_id = fields.Many2one(comodel_name='res.users', string='Cashier', readonly=True, default=lambda self: self.env.user)    
    is_member = fields.Boolean(string='Member')

    level = fields.Selection([
        ('nonlevel', 'Nonlevel'),
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold')
    ], string='level')
       