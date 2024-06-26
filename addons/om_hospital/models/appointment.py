from odoo import api, fields, models, _
from odoo.exceptions import ValidationError as pesan_error

class CdnAppointment(models.Model):
    _name           = 'cdn.appointment' # nama tabel di database
    _inherit        = ['mail.thread','mail.activity.mixin'] # tambahkan mail thread
    _description    = 'Cdn Appointment' # deskripsi tabel di database
    _rec_name       = 'name' 
    _order          = 'id desc' # bisa, name, age,  asc desc berfungsi untuk mengurutkan data dari yang terbesar ke yang terkecil

    name            = fields.Char(string='sequence') # field name
    
    # pasien_id       = fields.Many2one(comodel_name='cdn.pasien', string='Pasien', ondelete='restrict')
    pasien_id       = fields.Many2one(comodel_name='cdn.pasien', string='Pasien', ondelete='cascade') 
    appoinment_time = fields.Datetime(string='Appoinment Time', default=fields.Datetime.now) # tabel waktu appoinment
    jenis_kel       = fields.Selection(related='pasien_id.jenis_kel') # tabel jenis kelamin
    booking_date    = fields.Date(string='Tanggal Booking', default=fields.Date.context_today) # tabel tanggal booking
    operasi         = fields.Many2one(comodel_name='cdn.oprasional', string='Operasi')
    
    ref             = fields.Char(string='Refrensi', help="refrenis ke pasien record") # tabel refrensi
    resep           = fields.Html(string='Resep') # tabel resep
    ploritas        = fields.Selection([
                                ('0', 'Normal'),
                                ('1', 'Low'),
                                ('2', 'High'),
                                ('3', 'Very High')
                                ], string="Priority") # tabel prioritas dengan bintang dan jumlah bintang mengikuti banyaknya seleksi
    state           = fields.Selection([
                                ('draf', 'Draft'),
                                ('on_consultasion', 'Lagi Konsultasi'),
                                ('done', 'Selesai'),
                                ('cancel', 'Batal')
                                ], string="Keadaan", required=True, default='draf') #state spesial
    dokter_id       = fields.Many2one(comodel_name='res.users', string='Dokter', Tracking=True) # tabel dokter

    farmasi_ids     = fields.One2many(comodel_name='cdn.farmasi', inverse_name='appointment_id', string='Farmasi') # tabel farmasi
    
    hide_sales_price = fields.Boolean(string='Sembuyikan Sales Harga') # tabel sembuyikan sales harga

    @api.model
    def create(self, vals): # fungsi create untuk membuat record baru
        vals['name'] = self.env['ir.sequence'].next_by_code('nomor.appointmen')
        return super(CdnAppointment, self).create(vals)
    def write(self, vals): # fungsi write untuk mengubah data
        if not self.ref: # jika kosong
            vals['name'] = self.env['ir.sequence'].next_by_code('nomor.appointmen')
        res = super(CdnAppointment, self).write(vals)
        return res

    def unlink(self): # fungsi unlink untuk menghapus data
        print("test........", self)
        for rec in self:
            if rec.state != 'draf': # jika state draf
                raise pesan_error(_("Tidak bisa menghapus data yang sudah di proses")) # tampilkan pesan error
        return super(CdnAppointment, self).unlink()

    @api.onchange('pasien_id') # fungsi on change untuk mengubah refrensi ketika pasien di ubah
    def _onchange_pasien_id(self):
        self.ref = self.pasien_id.ref # mengubah refrensi menjadi refrensi pasien
    def action_share_to_whatsapp(self): # fungsi share to whatsapp untuk membagikan data ke whatsapp
        if not self.pasien_id.phone:
            
            raise pesan_error(_("Nomor telepon pasien tidak di temukan"))
        message = "Halo %s, anda memiliki janji dengan %s pada tanggal %s" % (self.pasien_id.name, self.dokter_id.name, self.appoinment_time) # pesan yang akan di kirim
        url_whastapp = "https://api.whatsapp.com/send?phone=%s&text=%s" % (self.pasien_id.phone, message) # url whatsapp
        return {
            'type': 'ir.actions.act_url',
            'url': url_whastapp,
            'target': 'new',
        }

    def action_test(self): # fungsi test untuk menampilkan pesan saat button di klik
        print("button test !!!")
        return {
                'effect': {
                    'fadeout': 'slow', # efek fadeout
                    'message': 'Berhasil di klik', # pesan yang akan di tampilkan
                    'type': 'rainbow_man', # tipe pesan
                }
            }
    def action_on_consultasion(self): # fungsi on consultasion untuk mengubah state menjadi on consultasion
        for rec in self:
            if rec.state == 'draf': # jika state draf
                rec.state ='on_consultasion'

    def action_done(self): # fungsi done untuk mengubah state menjadi done
        for rec in self:
            rec.state = 'done'

    def action_cancel(self): 
        action = self.env.ref('om_hospital.cdn_wz_batalapointment_action').read()[0] # memanggil action batal appointment
        return action # mengembalikan action
    def action_draf(self): # fungsi draf untuk mengubah state menjadi draf
        for rec in self:
            rec.state = 'draf'

class CdnFarmasi(models.Model):
    _name           = 'cdn.farmasi' # nama tabel di database
    _description    = 'Cdn Farmasi' # deskripsi tabel di database

    produk_id       = fields.Many2one(comodel_name='product.product', required=True) # many to one ke tabel product product pada app odoo
    price_unit      = fields.Float(string='Harga',related='produk_id.list_price') # tabel harga
    qty             = fields.Integer(string='Quantity', default=1) # tabel quantity
    appointment_id  = fields.Many2one(comodel_name='cdn.appointment', string='Appointment') # many to one ke tabel cdn appointment
    
    
    
    