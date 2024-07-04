from odoo import models,fields,api

class KategoriBahan(models.Model):
    _name = 'hashmicrocoffee.kategoribahan'
    _description = 'KategoriBahan'

    name = fields.Selection(string='Nama Kategori', selection=[('kategori kopi', 'Kopi'), ('kategori makanan', 'Makanan'), ('kategori minuman', 'Minuman'),])
    
    no_rak = fields.Integer(string='No. Rak')
    
    bahan_ids = fields.One2many(comodel_name='hashmicrocoffee.bahan', inverse_name='kategori_bahan_id', string='Daftar Bahan')
    