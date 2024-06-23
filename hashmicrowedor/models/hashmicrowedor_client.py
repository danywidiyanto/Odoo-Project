from odoo import _, api, fields, models, tools

class Client(models.Model):
    _name = 'hashmicrowedor.client'
    _description = 'Client'

    name = fields.Char(string='Client Name',required=True)
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    
    

    
