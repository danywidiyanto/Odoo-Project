from odoo import models

class PenjualanWizardXlsx(models.AbstractModel):
    _name = 'report.hashmicrocoffee.report_penjualan_template_wizard_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, laporannya):
        #print(data)
        obj = data['laporannya']
        #print(len(obj))
        sheet = workbook.add_worksheet('Data Penjualan')
        bold_format = workbook.add_format({'bold': True})

        # Write the headers
        sheet.write('A1', 'Nama', bold_format)
        sheet.write('B1', 'Tanggal Transaksi', bold_format)
        sheet.write('C1', 'Total Harga', bold_format)
        sheet.write('D1', 'Barang', bold_format)
        sheet.write('E1', 'Harga Satuan', bold_format)
        sheet.write('F1', 'Quantity', bold_format)
        sheet.write('G1', 'Subtotal', bold_format)

        row = 1
        for x in obj:
            col = 0
            sheet.write(row, col, x['name'])
            col += 1
            sheet.write(row, col, x['tgl_transaksi'])
            col += 1
            sheet.write(row, col, x['total_harga'])
            col += 1

            # Fetch details of each detailpenjualan_ids
            for detail_id in x['detailpenjualan_ids']:
                detail = self.env['hashmicrocoffee.detailpenjualan'].browse(detail_id)

                # Write detail fields
                sheet.write(row, col, detail.bahan_id.name)
                col += 1
                sheet.write(row, col, detail.harga_satuan)
                col += 1
                sheet.write(row, col, detail.quantity)
                col += 1
                sheet.write(row, col, detail.subtotal)
                col += 1
                row += 1  # Move to the next row for each detail
                col = 3  # Reset to the column after 'Total Harga' for new detail

        # Ensure to handle cases where there are no details
        if not x['detailpenjualan_ids']:
            row += 1  # Move to the next row for the next record

