from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class Venue(models.Model):
    _name = 'hashmicrowedor.venue'
    _description = 'Venue'

    name = fields.Char(string='Venue Name', required=True)
    address = fields.Char(string='Address')
    capacity = fields.Integer(string='Capacity')
    price = fields.Float(string='Price per Day')
    image = fields.Binary(string='Image')
