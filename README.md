# 🍽️ Sistem Rekomendasi Menu Kantin

## Deskripsi Proyek

Sistem Rekomendasi Menu Kantin merupakan aplikasi berbasis console yang dibuat menggunakan bahasa pemrograman Python. Program ini bertujuan untuk membantu pengguna dalam memilih menu makanan atau minuman sesuai dengan kebutuhan, seperti budget yang dimiliki, kategori menu, maupun nama menu yang ingin dicari.

Selain itu, program ini juga menerapkan konsep-konsep dasar Algoritma Pemrograman, seperti penggunaan struktur data List dan Dictionary, Function, Searching, Sorting, serta Random Recommendation.

---

## Latar Belakang

Di lingkungan kampus, kantin menyediakan berbagai pilihan makanan dan minuman dengan harga yang beragam. Banyaknya pilihan tersebut sering membuat pengguna kesulitan menentukan menu yang sesuai dengan kebutuhan atau budget yang dimiliki.

Oleh karena itu dibuat Sistem Rekomendasi Menu Kantin yang mampu membantu pengguna memilih menu dengan lebih cepat melalui fitur pencarian, filter, pengurutan harga, dan rekomendasi menu secara acak.

---

## Tujuan Program

Program ini dibuat untuk membantu pengguna memilih menu kantin sesuai dengan kebutuhan. Selain itu, proyek ini juga bertujuan untuk mengimplementasikan materi Algoritma Pemrograman melalui penggunaan struktur data List dan Dictionary, Function, Searching, Sorting, serta validasi input pada sebuah aplikasi sederhana berbasis Python.

---

## Fitur Program

Program memiliki beberapa fitur utama, yaitu:

- Menampilkan seluruh daftar menu kantin.
- Filter menu berdasarkan budget.
- Filter menu berdasarkan kategori.
- Mencari menu berdasarkan nama.
- Mengurutkan menu berdasarkan harga (Ascending dan Descending).
- Memberikan rekomendasi menu secara acak.
- Menampilkan hasil filter atau rekomendasi terakhir.
- Validasi input pengguna.

---

## Struktur Data

Program menggunakan dua struktur data utama, yaitu List dan Dictionary.

### List

List digunakan sebagai database utama yang menyimpan seluruh data menu.

Contoh:

```python
menu_kantin = [


Dictionary

Setiap menu disimpan dalam bentuk Dictionary.

Contoh:

{
    "nama": "Nasi Goreng",
    "kategori": "Makanan",
    "harga": 15000
}

Dengan kombinasi List dan Dictionary, data menjadi lebih mudah diproses untuk proses pencarian, filter, sorting, maupun rekomendasi.

Algoritma yang Digunakan
1. Linear Search

Digunakan pada fitur pencarian menu berdasarkan nama.

Program akan memeriksa setiap data menu satu per satu hingga menemukan menu yang sesuai dengan kata kunci yang dimasukkan pengguna.

Fungsi:

cari_menu_nama()
2. Filtering

Digunakan pada fitur:

Filter Budget
Filter Kategori

Program akan menyeleksi data yang memenuhi syarat tertentu kemudian menyimpannya ke dalam list hasil.

Fungsi:

filter_budget()

filter_kategori()
3. Sorting

Digunakan untuk mengurutkan menu berdasarkan harga.

Program menggunakan algoritma sorting manual dengan dua buah perulangan bersarang sehingga dapat mengurutkan harga dari:

Termurah → Termahal
Termahal → Termurah

Fungsi:

sorting_harga()
4. Random Recommendation

Digunakan untuk memberikan rekomendasi menu secara acak menggunakan library random.

Fungsi:

rekomendasi_acak()
Daftar Fungsi
Fungsi	Kegunaan
tampilkan_judul()	Menampilkan menu utama
tampilkan_menu()	Menampilkan seluruh menu
validasi_angka()	Memvalidasi input pengguna
filter_budget()	Filter berdasarkan budget
filter_kategori()	Filter berdasarkan kategori
cari_menu_nama()	Searching berdasarkan nama
sorting_harga()	Sorting berdasarkan harga
rekomendasi_acak()	Memberikan rekomendasi acak
tampilkan_hasil()	Menampilkan hasil proses
Cara Menjalankan Program
Install Python 3.x.
Download project atau clone repository GitHub.
Buka project menggunakan Visual Studio Code atau terminal.
Jalankan program dengan perintah:
python nama_file.py
Pilih menu sesuai kebutuhan.
Contoh Tampilan Program

Menu utama:

Tampilkan semua menu
Filter menu berdasarkan budget
Filter menu berdasarkan kategori
Cari menu berdasarkan nama
Urutkan menu berdasarkan harga
Rekomendasi menu acak
Lihat hasil rekomendasi terakhir
Keluar
Pengujian Program

Program telah diuji menggunakan beberapa skenario.

Pengujian	Hasil
Menampilkan Menu	Berhasil
Filter Budget	Berhasil
Filter Kategori	Berhasil
Searching Nama	Berhasil
Sorting Harga	Berhasil
Rekomendasi Acak	Berhasil
Validasi Input	Berhasil
Keluar Program	Berhasil
Edge Cases yang Ditangani

Program telah menangani beberapa kondisi khusus, seperti:

Input kosong.
Input bukan angka.
Budget bernilai negatif.
Kategori tidak valid.
Kata kunci pencarian kosong.
Data tidak ditemukan.
Jumlah rekomendasi melebihi jumlah menu.
Jumlah rekomendasi bernilai 0.
Pilihan menu di luar rentang 1–8.

Kesimpulan

Program Sistem Rekomendasi Menu Kantin berhasil dibuat dan dapat berjalan dengan baik tanpa error. Program telah menerapkan konsep dasar Algoritma Pemrograman berupa penggunaan List, Dictionary, Function, Searching, Sorting, Random Recommendation, serta validasi input sehingga dapat membantu pengguna memilih menu sesuai kebutuhan.
