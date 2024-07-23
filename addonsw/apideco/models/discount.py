from odoo import _, api, fields, models, tools



class Discount(models.Model):
    _name = 'apideco.discount'
    _description = 'Discount'
    _inherits = {'apideco.item':'related_item_id'}
    
    name = fields.Char(string='Discount name')
    
