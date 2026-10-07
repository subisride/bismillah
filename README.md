# Template `myportofolio` — Hasil Akhir Tutorial 3

Repositori ini berisi proyek `myportofolio` dalam kondisi **selesai sampai Tutorial 03** mata kuliah PBP Gasal 2026/2027. Gunakan template ini untuk mengerjakan ulang **Tutorial 04, 05, dan 06** dari titik awal yang bersih.

Isi yang sudah tersedia:

- Tutorial 0: proyek Django 5.2, `requirements.txt`, `.gitignore`, konfigurasi `.env` dan database SQLite/PostgreSQL.
- Tutorial 1: folder konfigurasi `portofolio/`, halaman profil, CSS, serta konfigurasi WhiteNoise untuk PWS.
- Tutorial 2: aplikasi `main`, model `Experience`, halaman `/experience/`, routing, dan 6 *unit test*.
- Tutorial 3: `base.html`, model `Project`, `ProjectForm`, halaman `/projects/` (pencarian dan modal hapus), `/projects/add/`, dan endpoint JSON `/api/projects/`.

Data contoh memakai profil **Burhan** (NPM `67676767`) dengan foto burung hantu.

## Cara Memakai

1. Klik **Use this template** di GitHub (atau *clone* repositori ini), lalu buat repositori baru milikmu sendiri.
2. Siapkan *virtual environment* dan *dependencies*:

   ```bash
   python3 -m venv env
   source env/bin/activate        # Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Buat berkas `.env` di root proyek:

   ```env
   PRODUCTION=False
   ```

4. Jalankan migrasi dan server:

   ```bash
   python manage.py migrate
   python manage.py test main
   python manage.py runserver
   ```

5. Buka <http://localhost:8000/>, lalu lanjutkan ke Tutorial 04.

## Yang Perlu Kamu Sesuaikan

| Lokasi | Nilai contoh | Ganti dengan |
|---|---|---|
| `main/views.py` (`name`, `npm`, `bio`, `study_program`) | Burhan, `67676767` | data dirimu |
| `templates/index.html` (tautan sosial, email) | `github.com`, `burhan@example.com` | tautanmu |
| `static/img/burhan.jpg` | foto burung hantu | fotomu (sesuaikan `src` di `index.html`) |

## Catatan

Template ini dipakai untuk pengerjaan lokal saja dan tidak perlu di-*deploy* ke PWS. Nilai `ALLOWED_HOSTS` dan `CSRF_TRUSTED_ORIGINS` untuk domain PWS dibiarkan sebagai contoh agar sesuai dengan kode Tutorial 03.

## Kredit Foto

Foto burung hantu: "Eurasian eagle-owl (Bubo bubo) at African Lion Safari, Ontario, Canada", Wikimedia Commons, berlisensi CC0 (domain publik), dipotong menjadi persegi.
