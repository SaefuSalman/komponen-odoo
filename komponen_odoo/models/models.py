from odoo import fields, api, models

class MasterKomponen(models.Model):
    _name = 'master.komponen'
    _description = 'Master Komponen'

    # Master Komponen
    name = fields.Char('Referense', default='-', readonly=True)
    nama_komponen = fields.Char(string='Nama Komponen', required=True)
    waktu_pengerjaan = fields.Char(string='Waktu Pengerjaan')


    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('master.komponen')
        return super(MasterKomponen, self).create(vals)

class MasterItem(models.Model):
    _name = 'master.item'
    _description = 'Master Item'

    nama_item = fields.Char(string='Nama Item')
    mulai_pengerjaan = fields.Datetime(string='Tanggal Mulai Pengerjaan')
    bobot_persen = fields.Float(string='Bobot Persentase')
    komponen_id = fields.Many2one('master.komponen', string='komponen')
    nama_komponen = fields.Char(related='komponen_id.nama_komponen', invisible=True)
    waktu_pengerjaan = fields.Char(related='komponen_id.waktu_pengerjaan', invisible=True)
    master_item_line = fields.One2many('master.item.line', 'item_id', string='Master Item')

    # @api.depends('bobot_persen', 'komponen_id')
    # def compute_bobot_persen(self):
    #     for bobot in self:
    #         bobot.komponen_id = 0
    #         if bobot.bobot_persen and bobot.komponen_id:
    #             bobot.komponen_id = 100 * len(bobot.komponen_id) / bobot.bobot_persen
    def action_custom_import(self):
        return self.env.ref('komponen_odoo.action_report_komponen').report_action(self)



class MasterItemLines(models.Model):
    _name = 'master.item.line'
    _description = 'Master Item Line'

    komponen_id = fields.Many2one('master.komponen', string= 'Komponen', required=True)
    item_id = fields.Many2one('master.item', string='Item')
    quantity = fields.Integer('Quantity', required=True)
