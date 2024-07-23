from odoo import api, fields, models
from odoo.exceptions import ValidationError

class AddStudentWizard(models.TransientModel):
    _name = 'schoolcons.addstudent'
    _description = 'Add Student Wizard'

    name = fields.Char(string='Student Name', required=True)
    address = fields.Char(string='Address')
    class_id = fields.Many2one(comodel_name='schoolcons.class', string='Class', required=True)

    def action_add_student(self):
        if self.class_id.total_student >= self.class_id.capacity:
            raise ValidationError('Capacity full, choose another class')

        vals = {
            'name': self.name,
            'address': self.address,
            'class_id': self.class_id.id,
        }
        self.env['schoolcons.student'].create(vals)
        
        # Update total_student field in class_id
        self.class_id._compute_total_student()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Students',
            'res_model': 'schoolcons.student',
            'view_mode': 'tree,form',
            'target': 'current',
        }
    
    def action_class_info(self):
        message = (
        f"Class Info\n\n"
        f"Class: {self.class_id.name}\n"
        f"Total Student: {self.class_id.total_student}\n"
        f"Capacity: {self.class_id.capacity}\n"
        f"Seat Percentage: {self.class_id.seat_percentage:.2f}%\n\n"
        )
        raise ValidationError(message)

