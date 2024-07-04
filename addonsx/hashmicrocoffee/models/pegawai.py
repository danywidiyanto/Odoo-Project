from odoo import models,fields,api

class Pegawai(models.Model):
    _name = 'hashmicrocoffee.pegawai'
    _description = 'model.technical.name'

    name = fields.Char(string='Nama')
    age = fields.Integer(string='Usia')
    jabatan = fields.Selection(string='Jabatan', selection=[('cashier', 'Cashier'), ('accounting', 'Accounting'),('cs', 'Cleaning Service'),])
    photo = fields.Binary(string='Foto', 
    help='Choose your avatar'
    )
    tgl_lahir = fields.Datetime(string='Tanggal Lahir' ,default=fields.Datetime.now())
    status = fields.Char(string='status')
    
    @api.onchange('age')
    def _tentukan_status(self):        
            if self.age > 30:
                self.status = "tua"
            else:
                self.status = "muda"
    
    
    
    
    
