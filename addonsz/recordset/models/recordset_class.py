from odoo import _, api, fields, models, tools

class Class(models.Model):
    _name = 'recordset.class'
    _description = 'Class'

    name = fields.Char(string='Class Name')
    capacity = fields.Integer(string='Capacity')
    student_ids = fields.One2many(comodel_name='recordset.student', inverse_name='class_id', string='Student List')

    # @api.model 
    # def create(self, vals):
    #     record = super(Class, self).create(vals)
    #     a = self.env['recordset.student']
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Class, self).create(vals)
    #     a = self.env['recordset.student'].browse('name')
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Class, self).create(vals)
    #     a = self.env['recordset.student'].search([]).mapped('name')
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Class, self).create(vals)
    #     a = self.env['recordset.canteen'].search([]).mapped('name')
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Class, self).create(vals)
    #     a = self.env['recordset.student'].search(['class_id','=',id]).mapped('name')
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Class, self).create(vals)
    #     a = self.env['recordset.student'].search([('class_id','=',3)]).mapped('score')
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Class, self).create(vals)
    #     a = self.env['recordset.student'].search(['class_id','=',2]).mapped('name')
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Class, self).create(vals)
    #     a = self.env['recordset.canteen'].search(['price','=',2000]).mapped('name')
    #     print(a)
    #     return record

    # @api.model 
    # def create(self, vals):
    #     record = super(Class, self).create(vals)
    #     a = self.env['recordset.student'].search([('class_id','=',record.id)]).mapped('name')
    #     print(a)
    #     return record

    # def unlink(self):
    #     a = self.env['recordset.student'].search([('class_id','=',self.id)]).mapped('name')
    #     print(a)
    #     record = super(Class, self).unlink() 

    # def unlink(self):
    #     a = self.env['recordset.student'].search([]).mapped('name')
    #     print(a)
    #     record = super(Class, self).unlink() 

    # def unlink(self):
    #     a = self.env['recordset.student'].search([('class_id','=',7)]).mapped('name')
    #     print(a)
    #     record = super(Class, self).unlink() 

    def unlink(self):
        a = self.env['recordset.student'].search([]).write({'score' : 100})
        print(a)
        record = super(Class, self).unlink() 
