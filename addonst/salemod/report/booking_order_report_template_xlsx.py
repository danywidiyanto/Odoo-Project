from odoo import models

class BookingOrderWizardXlsx(models.AbstractModel):
    _name = 'report.booking_order_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, the_report):
        #print(data)
        obj = data['the_report']
        #print(len(obj))
        sheet = workbook.add_worksheet('Booking Order Data')
        bold_format = workbook.add_format({'bold': True})

        # Write the headers
        sheet.write('A1', 'Vendor', bold_format)
        sheet.write('B1', 'Order Deadline Date', bold_format)
        sheet.write('C1', 'Amount Total', bold_format)
        sheet.write('D1', 'Product', bold_format)
        sheet.write('E1', 'Price Unit', bold_format)
        sheet.write('F1', 'Quantity', bold_format)
        sheet.write('G1', 'Subtotal', bold_format)

        row = 1
        for x in obj:
            col = 0
            sheet.write(row, col, x['partner_id'][1])
            col += 1
            sheet.write(row, col, x['date_order'])
            col += 1
            sheet.write(row, col, x['amount_total'])
            col += 1

            # Fetch details of each detailpenjualan_ids
            for detail_id in x['order_line']:
                detail = self.env['sale.order.line'].browse(detail_id)

                # Write detail fields
                sheet.write(row, col, detail.product_id.name)
                col += 1
                sheet.write(row, col, detail.price_unit)
                col += 1
                sheet.write(row, col, detail.product_uom_qty)
                col += 1
                sheet.write(row, col, detail.price_subtotal)
                col += 1
                row += 1  
                col = 3  

      
        if not x['order_line']:
            row += 1  

