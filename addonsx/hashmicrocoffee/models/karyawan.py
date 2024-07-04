from odoo import _, api, fields, models, tools

class Karyawan(models.Model):
    _inherit = "hr.employee"
    _description = 'Karyawan'

    user_id = fields.Many2one(comodel_name='res.users', string='Kasir', readonly=True, default=lambda self: self.env.user)    
    is_menikah = fields.Boolean(string='Menikah', default=True)
    
