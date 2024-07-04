from odoo import _, api, fields, models, tools

import logging

_logger = logging.getLogger(__name__)

class ReportPenjualanWzXlsx(models.TransientModel):
    _name = 'hashmicrocoffee.reportpenjualanwzxlsx'
    _description = 'ReportPenjualanWzXlsx'

    dari_tgl = fields.Date(string='Dari Tanggal',required=True)
    ke_tgl = fields.Date(string='Ke Tanggal',required=True)
    penjualan_id = fields.Many2one(comodel_name='hashmicrocoffee.penjualan', string='Penjualan')

    def action_penjualan_report(self):
        laporan = []
        dari = self.dari_tgl
        ke = self.ke_tgl
        if dari:
            laporan += [('tgl_transaksi','>=', dari)]
        if ke:
            laporan += [('tgl_transaksi','<=', ke)]
        laporan_jadi = self.env['hashmicrocoffee.penjualan'].search_read(laporan)

        #_logger.info('Laporan yang dihasilkan: %s', laporan_jadi)  # Log data laporan_jadi untuk debugging

        data = {
            'form': self.read()[0],
            'laporannya' : laporan_jadi,
        }
        report_action = self.env.ref('hashmicrocoffee.report_penjualan_wizard_xlsx').report_action(self, data=data)
        report_action['close_on_report_download'] = True
        return report_action
    
