from odoo import models, fields, api
from datetime import timedelta as waktu

class TrainingCourse(models.Model):
    _name               = 'training.course'
    _description        = 'Training Course'

    name                = fields.Char(string='Nama Kursus', required=True)
    description         = fields.Text(string='Keterangan')
    user_id             = fields.Many2one(comodel_name='res.users', string='Penanggung Jawab')

    session_line        = fields.One2many(comodel_name='training.session', inverse_name='course_id', string='Sesi Training')

    prduct_ids = fields.Many2many(comodel_name='product.product', string='Peralatan/Kosusmsi', domain=[('produk_pelatihan', '!=', 'non_training')])
    

    # oofco 
    _sql_constraints    = [
        ("name_course_unique", "UNIQUE(name)", "Nama Kursus Sudah Ada"),
    ]
    
class TrainingSession(models.Model):
    _name               = 'training.session'
    _description        = 'Training Session'
    _inherit            = ['mail.thread', 'mail.activity.mixin']

    name                = fields.Char(string='Sesi Trainig', tracking=True)
    course_id           = fields.Many2one(comodel_name='training.course', string='Nama Kursus', tracking=True)
    start_date          = fields.Date(string='Tanggal Mulai', tracking=True)
    duration            = fields.Integer(string='Durasi (day)', tracking=True)
    seats               = fields.Integer(string='MAX Peserta', default=1, tracking=True)
    instruktur_id       = fields.Many2one(comodel_name='instruktur', string='Nama Instruktur', tracking=True)
    
    alamat              = fields.Char(string='Alamat', related='instruktur_id.street', tracking=True)
    no_hp               = fields.Char(string='No Hp', related='instruktur_id.mobile', tracking=True)
    email               = fields.Char(string='Email', related='instruktur_id.email', tracking=True)
    jenis_kel           = fields.Selection(string='Jenis Kelamin', related='instruktur_id.jenis_kel', tracking=True)

    peserta_ids         = fields.Many2many(comodel_name='peserta', string='Peserta', tracking=True)

    # oocom 
    jml_peserta         = fields.Integer(compute='_compute_jml_peserta', string='Jumlah Peserta', tracking=True)
    
    state               = fields.Selection(string='Status', selection=[('draf', 'Draft'), ('progres', 'Sedang Berlangsung'),('done', 'Selesai')], default='draf', tracking=True)

    end_date            = fields.Date(string='End Date', compute='_compute_end_date')
    
    @api.depends('peserta_ids')
    def _compute_jml_peserta(self):
        for rec in self:
            rec.jml_peserta = len(rec.peserta_ids)


    def action_konfirmasi(self):
        self.state='progres'

    def action_selesai(self):
        self.state='done'

    def action_draf(self):
        self.state='draf'

    @api.depends('duration')
    def _compute_end_date(self):
        for rec in self:
            rec.end_date = rec.start_date + waktu(days=rec.duration)
    
    