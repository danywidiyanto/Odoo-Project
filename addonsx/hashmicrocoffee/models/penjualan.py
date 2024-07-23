from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class Penjualan(models.Model):
    _name = 'hashmicrocoffee.penjualan'
    _description = 'Penjualan'

    referensi = fields.Char(
        string='No. Referensi', 
        required=True, 
        readonly=True, 
        default=lambda self: _('New')
    )
    user_id = fields.Many2one(
        comodel_name='res.users', 
        string='Cashier', 
        readonly=True, 
        default=lambda self: self.env.user
    )
    membership = fields.Boolean(string='Apakah member?')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Nama Member')  
    name = fields.Char(string='Nama Pembeli')
    tgl_transaksi = fields.Datetime(string='Tanggal Transakasi', default=fields.Datetime.now())
    detailpenjualan_ids = fields.One2many(
        comodel_name='hashmicrocoffee.detailpenjualan', 
        inverse_name='penjualan_id', 
        string='Detail Penjualan'
    )
    total_harga = fields.Integer(compute='_compute_total_harga', string='Total Harga')
    state = fields.Selection(
        string='State', 
        selection=[('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done'), ('cancel', 'Cancel')], 
        readonly=True, 
        default='draft'
    )

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancel'})

    def action_draft(self):
        self.write({'state': 'draft'})

    @api.depends('detailpenjualan_ids')
    def _compute_total_harga(self):
        for rec in self:
            a = rec.detailpenjualan_ids.mapped('subtotal')
            rec.total_harga = sum(a)

    def unlink(self):
        for detail in self:
            a = detail.detailpenjualan_ids
            for bahannya in a:
                # Mengubah bahan_id menjadi makanan_id dan mengakses detailmakanan_ids
                details = bahannya.makanan_id.detailmakanan_ids
                for detail in details:
                    detail.bahan_id.stok += detail.kebutuhan * bahannya.quantity
        return super(Penjualan, self).unlink()

    def write(self, vals):
        for rec in self:
            a = rec.detailpenjualan_ids
            for data in a:
                # Mengubah bahan_id menjadi makanan_id dan mengakses detailmakanan_ids
                details = data.makanan_id.detailmakanan_ids
                for detail in details:
                    detail.bahan_id.stok -= detail.kebutuhan * data.quantity
        record = super(Penjualan, self).write(vals)
        for recc in self:
            b = recc.detailpenjualan_ids
            for databaru in b:
                if databaru in a:
                    # Mengubah bahan_id menjadi makanan_id dan mengakses detailmakanan_ids
                    details = databaru.makanan_id.detailmakanan_ids
                    for detail in details:
                        detail.bahan_id.stok += detail.kebutuhan * databaru.quantity
        return record

    @api.model
    def create(self, vals):
        if vals.get('referensi', _("New")) == _("New"):
            membership = vals.get('membership', False)
            if membership:
                vals['referensi'] = self.env['ir.sequence'].next_by_code('referensi.penjualanmember') or _("New")
            else:
                vals['referensi'] = self.env['ir.sequence'].next_by_code('referensi.penjualannonmember') or _("New")
        record = super(Penjualan, self).create(vals)
        return record

class DetailPenjualan(models.Model):
    _name = 'hashmicrocoffee.detailpenjualan'
    _description = 'DetailPenjualan'

    penjualan_id = fields.Many2one(comodel_name='hashmicrocoffee.penjualan', string='Penjualan')
    tgl_transaksi = fields.Datetime(string='Tanggal Transaksi', default=fields.Datetime.now())
    makanan_id = fields.Many2one(comodel_name='hashmicrocoffee.makanan', string='Makanan')
    harga_satuan = fields.Integer(string='Harga Satuan', related='makanan_id.harga', readonly=True, store=True)
    quantity = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'quantity')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.harga_satuan * rec.quantity

    @api.model
    def create(self, vals):
        record = super(DetailPenjualan, self).create(vals)
        # Mengakses detailmakanan_ids untuk mengurangi stok bahan berdasarkan makanan_id
        details = self.env['hashmicrocoffee.makanan'].search([('id', '=', record.makanan_id.id)]).mapped('detailmakanan_ids')
        print(details)
        for detail in details:
            self.env['hashmicrocoffee.bahan'].search([('id', '=', detail.bahan_id.id)]).write({'stok': detail.bahan_id.stok - (detail.kebutuhan * record.quantity)})
        return record
