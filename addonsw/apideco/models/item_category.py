from odoo import _, api, fields, models, tools

class ItemCategory(models.Model):
    _name = 'apideco.itemcategory'
    _description = 'ItemCategory'


    code = fields.Char(string='Code')
    name = fields.Selection([
        ('book', 'Book'),('stationery','Stationery')
    ], string='Item Category')
    code_category = fields.Char(string='Code Category')
    #code_category = fields.Char(string='Code Category', compute='_compute_code_category')
    num_shelves = fields.Integer(string='Number of Shelves')
    #the_error = fields.Char(string='Error')
    
    #NB: ONCHANGE BERTINDAK DI LEVEL VIEW (FRONTEND) SEMNTARA DEPENDS DI LEVEL SERVER (BACKEND)
    #ONCHANGE HANYA BERTINDAK PADA SATU VIEW MODEL, TIDAK BISA KE MODEL LAIN
    @api.onchange('name')
    def _onchange_code_category(self):
        if (self.name == 'book'):
            self.code_category = self.code + 'BOOK' + str(self.num_shelves)
        elif (self.name == 'stationery'):  
            self.code_category = self.code + 'STAT' + str(self.num_shelves)
    #JIKA FIELD COMPUTE TIDAK DI SIMPAN DALAM DATABASE , JIKA ONCHANGE DISIMPAN DI DATABSE SEPERTI MENETAPKAN NILAI OTOMATIS PADA FIELD
    #COMPUTE BISA BERTINDAK ANTAR MODEL ATAU ANTAR VIEW
    
    # @api.depends('name')
    # def _compute_code_category(self):
    #     for rec in self:
    #         if (rec.name == 'book'):
    #             rec.code_category = 'BOOKS'
    #         elif (rec.name == 'stationery'):
    #             rec.code_category = 'STATS'

