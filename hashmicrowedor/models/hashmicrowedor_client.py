from odoo import _, api, fields, models, tools

class Client(models.Model):
    _name = 'hashmicrowedor.client'
    _description = 'Client'
<<<<<<< HEAD:hashmicrowedor/models/hashmicrowedor_client.py
=======
    _inheritance = 'res.partner'
>>>>>>> bc71baf5 (Update Web Interface):addonsx/hashmicrowedor/models/hashmicrowedor_client.py

    name = fields.Char(string='Client Name',required=True)
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    
    

    
