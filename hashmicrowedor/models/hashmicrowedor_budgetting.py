from odoo import _, api, fields, models, tools

class Budgetting(models.Model):
    _name = 'hashmicrowedor.budgetting'
    _description = 'Budgetting'

    client_id = fields.Many2one('hashmicrowedor.client', string='Client', required=True)
    category = fields.Selection([
        ('venue', 'Venue'),
        ('makeup', 'Makeup'),
        ('organizer', 'Wedding Organizer'),
        ('photographer', 'Photographer'),
        ('entertainment', 'Music/Entertainment'),
        ('catering', 'Catering'),
        ('souvenir', 'Souvenir'),
        ('invitation', 'Invitation'),
        ('rental', 'Rental Services'),
        ('jewelry', 'Jewelry'),
        ('other', 'Other')
    ], string='Category', required=True)
    budget_amount = fields.Float(string='Budget Amount')
    actual_amount = fields.Float(string='Actual Amount')
    variance = fields.Float(string='Variance', compute='_compute_variance', store=True)

    @api.depends('budget_amount', 'actual_amount')
    def _compute_variance(self):
        for record in self:
            record.variance = record.actual_amount - record.budget_amount
    
