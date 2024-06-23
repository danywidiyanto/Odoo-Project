from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class Catering(models.Model):
    _name = 'hashmicrowedor.catering'
    _description = 'Catering'

    name = fields.Char(string='Catering Name')
    price_per_person = fields.Integer(string='Price per Person')
    min_order = fields.Integer(string='Minimum Order', default = 50)

    @api.constrains('min_order')
    def _check_min_order(self):
        for record in self:
            if record.min_order < 50:
                raise ValidationError("Minimum order for catering is 50 portions.")
    
    
