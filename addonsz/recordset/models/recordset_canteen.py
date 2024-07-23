from odoo import _, api, fields, models, tools

class Canteen(models.Model):
    _name = 'recordset.canteen'
    _description = 'Canteen'

    name = fields.Char(string='Food Name')
    price = fields.Integer(string='Food Price')
