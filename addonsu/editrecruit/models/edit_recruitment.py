from odoo import models, fields

class EditHrApplicant(models.Model):
    _inherit = 'hr.applicant'

    major = fields.Char(string="Major")
    school_university = fields.Char(string="School/University")
