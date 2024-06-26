# Odoo Tutorial By Rizki Desu

## 1. Membuat Module
- buat folder modulnya contoh `om_hospital`.
- buat file di poldernya `init.py` suapa dapat membaca file python lainya.
- buat file `__manifest__.py` karena odoo membaca modul mu di file ini.
- cara paling gampang yaitu memakai `SCAFFOLDING`
---

## 2 Menambahkan Icon Pada Module
- buat folder `static/description` di modul mu
- tambahkan gambar dengan nama `icon.png` 
- buat ikon mu di `https://spilymp.github.io/ibo`
- ingat penamaan harus menggunakan penamaan `icon.png`
---

## 3 Membuat model 
- model adalah sebuah database, kita bisa memaukan umur, jenis kelamin dan lainya di situ
- kita cek di pengatiran `odoo > teknikal > models` kamu bisa cari model yang kamu buat
---

## 4 mendefinisikan menu
- kita bisa cek menu yang kita buat di `odoo setting > menu items ` ketikan menu mu yang kamu buat atau kit bisa lihat di modul info
- menu tanpa `action` dan `parent` adalah menu utama
- menu dengan `parent` adalah menu yang basanya utuk meng kaegori kam nemu kita
- menu dengan `action` dan `parent` adalah menu yang berjalan
- jangan lupa di masukan di `manifest` bagian `data`
---
## 5 membuat action
- action adalah sebuah cara agar odoo menjalankan kode mu melalaui tombol menu dengan di definisiak melalui `window action`
- buat file xml sesuai dengan aksi einginan mu contoh `patient.xml`
- gunakan snipet `oact` sesuakan dengan model mu
- window action memiliki macam macam bentuk
- kita bisa cek di `odoo setting >Window Actions` cari action mu yang kamu buat
- tapi kita perlu `membuat` odoo tree, from atau kanban nya dulu `dengan modelnya` untuk meng kostum tampilanya
---
## 6 menghubungkan menu dengan aksi
- kita tambakan menu aksi di file tempat aksi di buat contoh di sini adalah `patient_view.xml`
- kita bisa juga memanggil aksi dari mudule lainya dengan meilih view yang ingin di tampiklan dan pilih edit dan copy `External ID` sebagai action nya. 
---
## 7 mengeset ir model aksess
- sebelum kita set aksess kita mengkases aplikasi yang kita buat, menggunakan `super user` kita pelu set akses nya
- kita perlu mengatur model akses dengan membuat folder `security` dan masuk ke `pengaturan odoo > teknikal ` pilih `Access Rights` di bagian security di link browser ada model `ir.model.access` gunanan nama itu untuk nama file. 
- buat file csv dengan nama `ir.model.access.csv` 
- masukan ini sebagai header csvnya
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
```
- isikan
```
access.<model>,access_<model>,<nama modul>.model_<model>,<group akses>,<read>,<write>,<create>,<delete>
```
- CRUD menggunakan 1 atau 0
- bisa di cek di `odoo setting > teknikal > models` di model mu dan cek access 
---
## 8 set ikon menu pada modul mu
- untuk menampilkan icon modul menu kita msukan ke menu root dengan menambahkan 
```
web_icon= "<nama folder modul mu>,<lokasi gambar mu>"
```
- untuk melihat perubanyan install modul di link [web_responsive](https://apps.odoo.com/apps/modules/16.0/https://apps.odoo.com/apps/modules/16.0/web_responsive/)
- buat ikon mu di `https://spilymp.github.io/ibo` yang stabil atau buat sendiri
- jangan lupa upgrade
---
## 9 membuat form
- sebenarnya di odoo 16 sudah di buat tetapi jika igin custom bisa melakukan hal ini
- gunakan snipet `oform`
- gunakan ofied dan pada name sesuakan dengan variabel yang da pda model masing masing
---
## 10 membuat view 
- membuat view, di odoo jika belum membuat akan cuma menampilkan nama/id nys saja
- buat dengan snipet `otree`
- gunakan ofied dan pada name sesuakan dengan variabel yang da pada model masing masing
---
## 11 membuat pencarian di view
- membuat mencarian di view menggunakan ofsearch 
- bagian field tuliskan field yang akan di cari 
- Pada odoo Domain adalah list yang berisi ekspresi tertentu yang digunakan untuk memfilter suatu data dari database. Umumnya domain akan diterjemahkan oleh odoo menjadi ekspresi SQL untuk mengisi klausa where [refrensi](https://ngasturi.id/2020/04/03/menguji-domain-pada-odoo/)
---

## 12 membuat filter di odoo
- filter adalah tenik untuk memfilter apa yang ingin kita cari teknik penulisnaya yaitu : 
```
<filter name="<nama_filter>" string="<nama_tampilan>" domain="[('<variabel>', '=', '<nilai>')]" />
```
- dalam menggunkaan lebih besar atau lebih kecil odoo mengenali : `gt` = > lebih besar  dan `lt` = < lebih kecil atau bisa di tulis dengan contoh
```
<filter name="kids" string="Anak-anak" domain="[('umur', '&lt;=', 5)]" />
```
---

## 13 teknik arip dan unarsip 
- buat variable bollean active `variable spesial untuk menampiklan arcive,` dengan defaultnya `True` karena archive defaulnya di oddo adalah `False`
```
active = fields.Boolean(string='Activate', default=True)
```
- buat filter archived untuk menampilkan data yang di arsip kan 
---

## 14 tenik domain di menu 
- buat oact baru di file xml baru, dan tambahakan domain contoh 
```
<field name="domain">[('<variable>','=','<nilai>')]</field>
```
## 15 set nilai default di menu
- buat oact baru di file di xml baru, dan tambahakan context contoh 
```
<field name="context">{'default_<variable>':'<nilai>'}</field> 
```

## 16 set default filter dan grub by
- set grup by 
```
<group expand="0" string="Group By">
    <filter string="Gender" name="group_by_<variabel>" context="{'group_by': '<variabel>'}"/>
</group>
```
- set nya
```
<field name="context">{'search_default_<nama filter/group>':1}</field> 
```

## 17 tempat chat 
- Chatter adalah fitur komunikasi dan kolaborasi yang terintegrasi dalam berbagai modul Odoo. Fitur ini memungkinkan pengguna untuk berkomunikasi, berbagi informasi, dan melacak aktivitas terkait dengan dokumen bisnis seperti faktur, penjualan, pembelian, dan tugas proyek.
- cara menggunakanya pertama aialah tambahakan deppend `mail` 
- tambahakan `_inherit = ['mail.thread','mail.activity.mixin']` di model mu
- dan tambahkan di view form di bawah sheet
```
        </sheet>
        <!-- Chatter -->
        <div class="oe_chatter">
            <field name="message_follower_ids" groups="base.group_user"/>
            <field name="activity_ids"/>
            <field name="message_ids"/>
        </div>
    </form>
```

## 18 cara tracking model mu dan muncul histori
- tracking adalah teknik untuk melacak perubahan data pada model mu
- disetiap peribahan model ingin ada perubahan dan ti tampiklan di chatter
- tambahakan `tracking=True` di model mu
- contoh `name = fields.Char(string='Nama Pasien', tracking=True)`

## 19 menambahkan seach panel di odoo 
- search panel adalah teknik untuk mempermudah pencarian data di odoo
- tambahakan di view form di bawah sheet
- contoh
```
    <searchpanel>
        <field name="<nama_field>" icon="fa-users" select='multi'/>
    </searchpanel>
```

## 20 Many2one 
- Dalam Odoo, `Many2one` adalah salah satu jenis field yang digunakan dalam model data untuk merepresentasikan relasi banyak-ke-satu (Many-to-One) antara dua model. 
- penulisan many2one adalah 

```
nama_field = fields.Many2one(comodel_name='<model>', string='<Label>')
```
- contoh kasus many2one adalah kita sebagai desa yang  memiliki kecamatan

## 21 date time dan date
- dalam odoo ada dua jenis field yang digunakan untuk menampilkan tanggal dan waktu yaitu `datetime` dan `date`
- date time menampilkan tanggal dan waktu penulisan datetime adalah :
```
<field_name> = fields.Datetime('string='<label>'')
```
- date hanya menampilkan tanggal contoh penulisan :
```
<field_name> = fields.Date(string='<label>')
```

## 22 set default di py
- dalam odoo kita bisa mengset default value di field yang kita buat 
- set default bearti ada nilai yang terseting meskipun nanti tidak di isi
```
<nama_field> = fields.Integer(string='<label>')
```

## 23 relate database 
- dalam odoo kita bisa mengakses database yang lain menggunakan `related`
- kelemahan related adalah tidak bisa di edit
- penulisan related adalah: 
```
<variabel> = fields.<jenis_variabel>(related='<model/tabel>.<field/data>')
```
## 24 compute
- dalam odoo kita bisa menghitung data yang ada di field yang lain menggunakan `compute` 
- dalam odoo ada sebuah teknik yang namanya compute berikut contoh simpelnya
```
variabel = fields.Integer(string='angka1') 
hasil = fields.Integer(string='Hasil 2x lipat', compute='_2xlipat', store=True) #store artinya menyimpan ke db
@api.depends('variabel') # akan di utamakan variabel yang di sini
def _2xlipat(self): #selft artinya diri sendiri yaitu model itu sendiri
    self.hasil=self.variabel * self.variabel #variabel di kali variabel
```
## 25 onchange 
- dalam odoo kita bisa mengubah field yang lain menggunakan `onchange`
- onchange adalah teknik yang digunakan untuk mengubah field yang lain berdasarkan field yang di pilih
- contoh implentasi

```
pejabat_id = fields.Many2one(comodel_name='desu.pejabat', string='Nama Atasan')
jabatan_pejabat = fields.Char(string='Jabatan Atasan', store=True, readonly=True)
@api.onchange('pejabat_id')
def _onchange_pasien_id(self):
    self.jabatan_pejabat = self.pejabat_id.jenis_jabatan
```
- field `jabatan_pejabat` akan di ganti menggunakan fungsi `_onchange_pasien_id`

## 26 penggunakan rec name
- rec_name adalah teknik untuk menampilkan field yang di inginkan di view
- saat membat model tanpa field name atau ingin mengcostume name nanti akan ketemu masaalah sehingga hanya memunculkan id olekarena itu penggunaaan rech_name penting contoh implentasi: 
```
_rec_name = '<nama field yang ingin di tampilkan>'
```

## 27 nootebook 
- notebook adalah teknik untuk membuat tab di view
- contoh penulisan
```
<notebook>
    <page string="Resep" name="resep">
        <group>
            <field>
        </group>
    </page>
    <page string="Farmasi" name="farmasi">
        <group>
            <field>
        </group>
    </page>
</notebook>
```

## 28 html
- html adalah teknik untuk menampilkan html di view
- contoh penulisan
```
<field name="deskripsi" widget="html"/>
```

## 29 hapus tombol edit delete duplikat
- untuk menghapus tombol edit delete duplikat tambahkan code berikut di view model mu

```
- tree
```
<tree create="0" delete="0">
```
- from
```
form create="0" delete="0" edit="0">
```

## 30 prority 
- priority adalah teknik untuk menampilkan prioritas di view model

- buat seleksi field contoh
```
ploritas= fields.Selection([('0', 'Normal'),('1', 'Low'),('2', 'High'),('3', 'Very High')], string="Priority") 
```
- lalu buat view nya 
```
<div>
    <h2>
        <field name="ploritas" widget="priority" class="me-3"/>
    </h2>
</div>
```
## 31 status bar

- membuat status bar awal awal buat field selection untuk acuan contoh
```
keadaan = fields.Selection([('draf', 'Draft'),('running', 'Berlangsung'),('done', 'Selesai'),('cancel', 'Batal'), string="Keadaan", required=True)
```
- view nya
```
<form>
    <header>
        <field 
            name="keadaan" 
            widget="statusbar" 
            nolabel="1" 
            statusbar_visible="draf,running,done"
            options="{'clickable': '1'}"/>
    </header>
    <sheet>
```

## 32 membuat action button
- membuat action button adalah teknik untuk membuat tombol di view model mu

- mula mula buat action funsinya dulu karena nanti program berjalan mengikuti fungsi ini contoh : 
```
def <nama fungsi>(self):
    print("button test !!!")

```
- sekarang buat tombolnya di view model nya `bertype opbjek` karena ke fungsi
```
<button name="<nama fungsi>" string="Tes Button" type="object" class="oe_highlight"/>
```
- tes ke terminal atau docker logs mu

## 33 menambahkan konfirmasi message di button 
- caranya cukup tambahakan code berikut pada button mu
- contoh
```
confirm="<pesan nya apa>"
```
## 34 help mesage
- help message adalah pesan yang akan muncul saat di hover di field atau tombol
```
help="<pesan nya apa>"
```
## 35 hitung umur brdasrkan tanggal lahir 
- untuk menghitung umur berdasarkan tanggal lahir kita bisa menggunakan fungsi `date`
- tambahakan library berikut: 
```
from datetime import date
```
fungsi nya berikut:
```
def _hitung_umur_dari_lahir(self):
        for rec in self:
            today = date.today()
            if rec.tanggal_lahir:
                rec.umur = today.year - rec.tanggal_lahir.year
            else:
                rec.umur = 0
```

## 36 menambahkan penand pelangi di objek button atau sebagainya 
- untuk menambahkan efek pelangi di objek button atau sebagainya kita bisa menggunakan `effect`
- tambahakan kode berikut ke fungsi 
```
return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Berhasil di klik',
                'type': 'rainbow_man',
            }
        }
```

## 37 widget bandage dan decoration 
- bandage adalah untuk menambahkan penampilan di field
- decoration adalah untuk memberikan warna di field
- contoh penulisan bandage dan decoration
```
<field name="keadaan" 
                    decoration-success="keadaan == 'done'" 
                    decoration-info="keadaan == 'draf'" 
                    decoration-danger="keadaan =='cancel'" 
                    decoration-muted="keadaan == 'running'"
                    widget="badge"/>
```
`decoration-danger = red`
`decoration-success = green`
`decoration-warning = orange`
`decoration-info = light blue`
`decoration-muted`
## 38 decoration di view tree berdasarkan keadaan
- decoration untuk memberikan warna contoh code 
```
<tree decoration-success="keadaan == 'done'" 
        decoration-info="keadaan == 'draf'" 
        decoration-danger="keadaan == 'cancel'" 
        decoration-muted="keadaan == 'on_consultasion'">
```

## 39 widget list_activity
- widget list_activity adalah teknik untuk menampilkan activity di view model mu
- agar lebih menarik di bagian activity tambhakan di field `activity_ids` dari inherit dari `_inherit = ['mail.thread','mail.activity.mixin']`
```
widget="list_activity"
```

## 65 load data xml
- untuk memuat data xml di odoo kita bisa menggunakan `data` di `__manifest__.py` contoh
```
<?xml version='1.0' encoding='utf-8'?>
<odoo>
    <data>

        <record id="<id bebas adal gak sama>" model="<nama_model>">
            <field name="name"><yang mau di tampilkan></field>
        </record>

        <record id="pasien_tag_mr" model="cdn.pasien.tag">
            <field name="name">Mr</field>
            <field name="active" eval="False"/>
        </record>

    </data>

</odoo>
```

## 66 load data csv
- untuk memuat data csv di odoo kita bisa menggunakan `data` di `__manifest__.py` contoh
- buat file csv di folder `data` contoh `pasien_tag.csv`
- tambahkan kode berikut di `__manifest__.py`
- penulisan file csv berdasarkan model yang di buat contoh : `<nama_model>.csv`
```
<cdn.pasien.tag>.csv
```
```
id,name,active
pasien_tag_ceo,CEO,True
pasien_tag_vvip,VVIP,False
pasien_tag_mrs,Mrs,True
```

## 68 inherit Model In Odoo 
- Inheritance adalah teknik yang digunakan untuk menambahkan atau mengubah field yang ada di model lain
- ada 3 jenis inheritance di odoo yaitu `_inherit`, `_inherits`, `_name`
- `_inherit` adalah teknik yang digunakan untuk menambahkan field yang ada di model lain
- `_inherits` adalah teknik yang digunakan untuk menambahkan field yang ada di model lain dan membuat model baru
- `_name` adalah teknik yang digunakan untuk mengubah nama model yang ada di odoo
- contoh penulisan `_inherit`
```
_inherit = 'res.partner'
```
- contoh penulisan `_inherits`
```
_inherits = {'res.partner': 'partner_id'}
```
- contoh penulisan `_name`
```
_name = 'res.partner'
```
jangan lupa tambahakn `depend` di `__manifest__.py` contoh
```
'depends': ['base', 'mail'],
```
