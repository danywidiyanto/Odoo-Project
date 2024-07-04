from odoo import models, fields, api

class StokOpname(models.Model):
    _name = 'hashmicrocoffee.stokopname'
    _description = 'Stok Opname'

    name = fields.Char(string='Nama Petugas')
    tgl_stokopname = fields.Date(string='Tanggal Stok Opname', default=fields.Date.today())
    detailstokopname_ids = fields.One2many(comodel_name='hashmicrocoffee.detailstokopname', inverse_name='stokopname_id', string='Detail Stok Opname')

    @api.model
    def default_get(self, fields_list):
        res = super(StokOpname, self).default_get(fields_list)
        bahan_record = self.env['hashmicrocoffee.bahan'].search([])
        detail_vals = []
        for bahan in bahan_record:
            detail_vals.append((0, 0, {
                'bahan_id': bahan.id,
                'check': False,
                'catatan': ''
            }))
        res['detailstokopname_ids'] = detail_vals
        return res

class DetailStokOpname(models.Model):
    _name = 'hashmicrocoffee.detailstokopname'
    _description = 'Detail Stok Opname'

    name = fields.Char(compute='_compute_name', string='Name')
    stok = fields.Char(compute='_compute_stok', string='Stok')
    bahan_id = fields.Many2one(comodel_name='hashmicrocoffee.bahan', string='Bahan')
    check = fields.Boolean(string='Sudah di check')
    catatan = fields.Char(string='Catatan')
    stokopname_id = fields.Many2one(comodel_name='hashmicrocoffee.stokopname', string='Stokopname')

    @api.depends('bahan_id')
    def _compute_stok(self):
        for rec in self:
            rec.stok = rec.bahan_id.stok

    @api.depends('bahan_id')
    def _compute_name(self):
        for rec in self:
            rec.name = rec.bahan_id.name
