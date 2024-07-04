from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Catering(models.Model):
    _name = 'hashmicrowedor.catering'
    _description = 'Catering'

    name = fields.Char(string='Catering Name')
    min_order = fields.Integer(string='Minimum Order', default=50)
    dish_ids = fields.One2many(comodel_name='hashmicrowedor.catering.dish', inverse_name='catering_id', string='Dishes')

    @api.constrains('min_order')
    def _check_min_order(self):
        for record in self:
            if record.min_order < 50:
                raise ValidationError("Minimum order for catering is 50 portions.")

class CateringDish(models.Model):
    _name = 'hashmicrowedor.catering.dish'
    _description = 'Catering Dish'

    name = fields.Char(string='Dish Name', required=True)
    description = fields.Text(string='Description')
    package = fields.Selection([
        ('premium', 'Premium Package'),
        ('high', 'High Package'),
        ('normal', 'Normal Package'),
        ('custom', 'Custom Package'),
    ], string='Package', default='custom', required=True)
    price_per_person = fields.Float(string='Price per Person')
    catering_id = fields.Many2one('hashmicrowedor.catering', string='Catering', required=True)
    default_foods = fields.Many2many('hashmicrowedor.food', 'catering_dish_default_foods_rel', 'catering_dish_id', 'food_id', string='Default Foods')
    custom_foods = fields.Many2many('hashmicrowedor.food', 'catering_dish_custom_foods_rel', 'catering_dish_id', 'food_id', string='Custom Foods')

    @api.onchange('package')
    def _onchange_package(self):
        if self.package != 'custom':
            # Set default foods based on selected package
            if self.package == 'premium':
                self.default_foods = [(6, 0, self._get_default_foods('premium'))]
            elif self.package == 'high':
                self.default_foods = [(6, 0, self._get_default_foods('high'))]
            elif self.package == 'normal':
                self.default_foods = [(6, 0, self._get_default_foods('normal'))]

    def _get_default_foods(self, package):
        # Example logic to retrieve default foods based on package
        if package == 'premium':
            return self.env.ref('hashmicrowedor.default_food_premium').ids
        elif package == 'high':
            return self.env.ref('hashmicrowedor.default_food_high').ids
        elif package == 'normal':
            return self.env.ref('hashmicrowedor.default_food_normal').ids
        return []

class Food(models.Model):
    _name = 'hashmicrowedor.food'
    _description = 'Food'

    name = fields.Char(string='Food Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
