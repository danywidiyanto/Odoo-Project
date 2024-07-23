from odoo import _, api, fields, models, tools

class Student(models.Model):
    _name = 'schoolcons.student'
    _description = 'Student'

    name = fields.Char(string="Student's Name")
    class_id = fields.Many2one(comodel_name='schoolcons.class', inverse_name='student_ids', string='ID Class')
    address = fields.Char(string="Student's Address")
    
    _sql_constraints = [
        ('unique_name',
         'UNIQUE(name)',
         "Student names must be unique")
    ]
    
