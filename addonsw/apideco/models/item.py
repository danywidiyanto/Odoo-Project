from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class Item(models.Model):
    _name = 'apideco.item'
    _description = 'Item'

    name = fields.Char(string='Item Name')
    codecategory_id = fields.Many2one(comodel_name='apideco.itemcategory', string='Code Category')

    code_item = fields.Char(compute='_compute_code_item', string='Code Item')
    price = fields.Integer(string='Price')
    installment = fields.Integer(string='Installment', default=3)
    installment_price = fields.Integer(string='Installment Price', compute='_compute_installment_price')   
    the_code_category = fields.Char(string='The code category', related='codecategory_id.code_category')
    sign = fields.Char(string='Error')

    @api.depends('codecategory_id')
    def _compute_code_item(self):
        for rec in self:
            rec.code_item = rec.codecategory_id.code_category + rec.name

    @api.depends('price', 'installment')
    def _compute_installment_price(self):
        for rec in self:
            rec.installment_price = rec.price / rec.installment if rec.installment != 0 else 0

    @api.constrains('installment')
    def _installmentCheck(self):
        for rec in self:
            if rec.installment <= 0:
                raise ValidationError('Required installment is 1 time or more')

    @api.model
    def create(self, vals):
        record = super(Item, self).create(vals)
        try:
            if record.installment == 0:
                raise ZeroDivisionError('Installment cannot be zero.')
            record.installment_price = record.price / record.installment
            record.sign = "Success"
        except ZeroDivisionError:
            record.sign = "Installment cannot be zero."
        except Exception as e:
            record.sign = 'An error occurred: %s' % str(e)
        return record
