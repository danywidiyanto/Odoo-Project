from odoo import _, api, fields, models, tools

class PurchaseOrderReportWizard(models.TransientModel):
    _name = 'purchase.order.report.wizard.xlsx'
    _description = 'Purchase Order Report Wizard Xlsx'

    date_from = fields.Datetime(string='Date From')
    date_to = fields.Datetime(string='Date To')
    order_id = fields.Many2one(comodel_name='purchase.order', string='Orders')
    
    def action_purchase_order_report_xlsx(self):
        report=[]
        from_date = self.date_from
        to_date = self.date_to

        if from_date :
            report += [('date_order','>=',from_date)]
        if to_date :
            report += [('date_order','<=',to_date)]

        report +=[('is_booking','=',True)]

        final_report = self.env['purchase.order'].search_read(report)

        data = {
            'form': self.read()[0],
            'the_report': final_report,
        }
        
        report_action = self.env.ref('salemod.purchase_order_report_xlsx').report_action(self, data=data)
        report_action['close_on_report_download'] = True
        return report_action
        print(final_report.type)