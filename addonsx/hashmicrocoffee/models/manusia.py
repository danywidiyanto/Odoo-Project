from odoo import models,fields,api

class Manusia(models.Model):
    _name = 'hashmicrocoffee.manusia'
    _description = 'Manusia'

    nama = fields.Char(string='Nama')
    usia = fields.Integer(string='Usia')
    alamat = fields.Char(string='Alamat')
    
    
    
