from odoo import _, api, fields, models, tools

class BookingOrderReportWizard(models.TransientModel):
    _name = 'booking.order.report.wizard'
    _description = 'Booking Order Report Wizard'

    date_from = fields.Datetime(string='Date From')
    date_to = fields.Datetime(string='Date To')
    booking_order_id = fields.Many2one(comodel_name='sale.order.line', string='Orders')

    def action_booking_order_report_pdf(self):
        report=[]
        from_date = self.date_from
        to_date = self.date_to
        if from_date :
            report += [('date_order','>=',from_date)]
        if to_date :
            report += [('date_order','<=',to_date)]

        report +=[('is_booking','=',True)]


        final_report = self.env['sale.order'].search_read(report)

        data = {
            'form': self.read()[0],
            'the_report': final_report,
        }

        print
        
        report_action = self.env.ref('salemod.booking_order_report').report_action(self, data=data)
        report_action['close_on_report_download'] = True
        return report_action
