from odoo import models

class BahanXlsx(models.AbstractModel):
    _name = 'report.hashmicrocoffee.report_bahan_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, bahan):
        sheet = workbook.add_worksheet('Daftar Bahan')
        bold_format = workbook.add_format({'bold': True})
        sheet.write('A1', 'Nama Bahan', bold_format)
        sheet.write('B1', 'Kondisi Stok', bold_format)

        row = 2
        for obj in bahan:
            sheet.write(row, 0, obj.name)
            sheet.write(row, 1, obj.kondisi_stok)
            row += 1
