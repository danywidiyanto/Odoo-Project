from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class Class(models.Model):
    _name = 'schoolcons.class'
    _description = 'Class'

    name = fields.Char(string='Class Name')
    no_room = fields.Char(string='No. Room')
    total_student = fields.Integer(compute='_compute_total_student', string='Total Student')
    capacity = fields.Integer(string='Capacity')
    student_ids = fields.One2many(comodel_name='schoolcons.student', inverse_name='class_id', string='Student List')
    seat_percentage = fields.Float(compute='_compute_seat_percentage', string='Seat Percentage', store=True)

    @api.depends('student_ids')
    def _compute_total_student(self):
        for rec in self:
            rec.total_student = len(rec.student_ids)
    
    @api.depends('total_student', 'capacity')
    def _compute_seat_percentage(self):
        for rec in self:
            if rec.capacity:
                rec.seat_percentage = (rec.total_student / rec.capacity) * 100.0
            else:
                rec.seat_percentage = 0.0
    
    @api.model
    def create(self, vals):
        if 'capacity' in vals:
            self._validate_capacity(vals['capacity'])
        return super(Class, self).create(vals)
    
    def write(self, vals):
        if 'capacity' in vals:
            self._validate_capacity(vals['capacity'])
        return super(Class, self).write(vals)
    
    def _validate_capacity(self, capacity):
        if capacity <= 0:
            raise ValidationError(_("Capacity must be greater than zero."))
        elif capacity > 50:
            raise ValidationError(_("Capacity cannot be greater than 50."))
    
    @api.constrains('total_student', 'capacity')
    def _check_class_capacity(self):
        for rec in self:
            if rec.total_student > rec.capacity:
                raise ValidationError(_('Capacity full, choose another class.'))
    
