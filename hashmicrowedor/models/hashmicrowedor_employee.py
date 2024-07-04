from odoo import _, api, fields, models, tools


class Employee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Employee'


    