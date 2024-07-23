from odoo import _, api, fields, models, tools

class Student(models.Model):
    _name = 'recordset.student'
    _description = 'Student'

    name = fields.Char(string="Student's name")
    score = fields.Integer(string='Score')
    class_id = fields.Many2one(comodel_name='recordset.class', inverse_name='student_ids', string='ID Class')

    # @api.model 
    # def create(self, vals):
    #     record = super(Student, self).create(vals)
    #     a = self.env['recordset.class'].search([('id','=',record.class_id.id)]).mapped('name')
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Student, self).create(vals)
    #     a = self.env['recordset.class'].search([('id','=',record.class_id.id)]).mapped('capacity')
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Student, self).create(vals)
    #     a = self.env['recordset.class'].search([('id','=',record.class_id.id)]).write({'capacity' : 100})
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Student, self).create(vals)
    #     a = self.env['recordset.class'].search([]).write({'capacity' : 100})
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Student, self).create(vals)
    #     a = self.env['recordset.canteen'].search([]).write({'harga' : 5000})
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Student, self).create(vals)
    #     a = self.env['recordset.class'].search([]).mapped('name')
    #     print(a)
    #     return record