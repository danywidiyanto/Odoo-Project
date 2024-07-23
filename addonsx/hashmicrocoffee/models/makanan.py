from odoo import _, api, fields, models, tools

class Makanan(models.Model):
    _name = 'hashmicrocoffee.makanan'
    _description = 'Makanan'

    name = fields.Char(string='Nama Makanan', required=True) 
    harga = fields.Integer(string='Harga')
    detailmakanan_ids = fields.One2many(comodel_name='hashmicrocoffee.detailmakanan', inverse_name='makanan_id', string='Detail Makanan')


class DetailMakanan(models.Model):
    _name = 'hashmicrocoffee.detailmakanan'
    _description = 'Detail Makanan'

    bahan_id = fields.Many2one(comodel_name='hashmicrocoffee.bahan', string='Nama Bahan')
    kebutuhan = fields.Integer(string='Kebutuhan')
    makanan_id = fields.Many2one(comodel_name='hashmicrocoffee.makanan', string='Makanan')
