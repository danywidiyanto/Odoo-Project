from odoo import models,fields,api



class Member(models.Model):
    _name = 'hashmicrocoffee.member'
    _inherit = 'hashmicrocoffee.manusia'
    _description = 'Member'
    
    no_member = fields.Integer(string='Nomor Member')
    
