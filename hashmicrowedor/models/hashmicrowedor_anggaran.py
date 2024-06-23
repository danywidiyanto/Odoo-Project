from odoo import _, api, fields, models, tools

class Anggaran(models.Model):
    _name = 'hashmicrowedor.anggaran'
    _description = 'Anggaran'
    name = fields.Char(string='Nama')
    
