from odoo import models, fields, api

class BookingReportWizard(models.TransientModel):
    _name = 'hashmicrowedor.booking.report.wizard'
    _description = 'Booking Report Wizard'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    booking_id = fields.Many2one(comodel_name='hashmicrowedor.booking', string='Booking')

    def action_generate_report(self):
        laporan = []
        start_date = self.start_date
        end_date = self.end_date
        
        if start_date:
            laporan += [('booking_date', '>=', start_date)]
        if end_date:
            laporan += [('booking_date', '<=', end_date)]

        laporan_jadi = self.env['hashmicrowedor.booking'].search_read(laporan)

        data = {
            'form': self.read()[0],
            'laporannya': laporan_jadi,
        }
        
        report_action = self.env.ref('hashmicrowedor.booking_report_pdf').report_action(self, data=data)
        report_action['close_on_report_download'] = True
        return report_action
