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

Program menggunakan dua struktur data utama, yaitu **List** dan **Dictionary**.

### 1. List

List digunakan sebagai database utama yang menyimpan seluruh data menu kantin.

**Contoh:**

```python
menu_kantin = [
    {"nama": "Nasi Goreng", "kategori": "Makanan", "harga": 15000},
    {"nama": "Mie Ayam", "kategori": "Makanan", "harga": 12000},
]
```

**Fungsi List dalam program:**

- Menyimpan seluruh data menu kantin.
- Memudahkan proses perulangan menggunakan `for`.
- Menjadi sumber data untuk proses filter, pencarian, sorting, dan rekomendasi menu.
- Menyimpan hasil proses filter maupun rekomendasi pada variabel `rekomendasi`.

---

### 2. Dictionary

Dictionary digunakan untuk menyimpan informasi setiap menu kantin dalam bentuk pasangan **key** dan **value**.

**Contoh:**

```python
{
    "nama": "Nasi Goreng",
    "kategori": "Makanan",
    "harga": 15000
}
```

**Fungsi Dictionary dalam program:**

- Menyimpan nama menu.
- Menyimpan kategori menu.
- Menyimpan harga menu.
- Memudahkan pengambilan data menggunakan key, seperti:
  - `menu["nama"]`
  - `menu["kategori"]`
  - `menu["harga"]`

---

### Hubungan List dan Dictionary

Pada program ini, **List** digunakan sebagai wadah utama yang menyimpan beberapa **Dictionary**. Setiap Dictionary mewakili satu data menu yang memiliki atribut **nama**, **kategori**, dan **harga**. Kombinasi kedua struktur data tersebut membuat proses filtering, searching, sorting, dan rekomendasi menu menjadi lebih mudah serta lebih terstruktur.

Ilustrasi struktur data:

```text
menu_kantin (List)
│
├── Dictionary 1
│     nama      : Nasi Goreng
│     kategori  : Makanan
│     harga     : 15000
│
├── Dictionary 2
│     nama      : Mie Ayam
│     kategori  : Makanan
│     harga     : 12000
│
├── Dictionary 3
│     nama      : Bakso
│     kategori  : Makanan
│     harga     : 13000
```

---

## Algoritma yang Digunakan

### 1. Linear Search

Linear Search digunakan pada fitur pencarian menu berdasarkan nama. Program akan memeriksa setiap data menu satu per satu hingga menemukan menu yang sesuai dengan kata kunci yang dimasukkan pengguna.

Fungsi yang digunakan:

```python
cari_menu_nama()
```

---

### 2. Filtering

Filtering digunakan untuk menyaring data sesuai kebutuhan pengguna.

Fitur yang menggunakan filtering:

- Filter berdasarkan budget.
- Filter berdasarkan kategori.

Fungsi yang digunakan:

```python
filter_budget()

filter_kategori()
```

---

### 3. Sorting

Sorting digunakan untuk mengurutkan data menu berdasarkan harga, baik dari harga termurah ke termahal maupun sebaliknya. Program menggunakan algoritma sorting manual dengan dua buah perulangan bersarang.

Fungsi yang digunakan:

```python
sorting_harga()
```

---

### 4. Random Recommendation

Random Recommendation digunakan untuk memberikan rekomendasi menu secara acak menggunakan library `random`.

Fungsi yang digunakan:

```python
rekomendasi_acak()
```

---

## Daftar Fungsi

| Nama Fungsi | Kegunaan |
|-------------|----------|
| tampilkan_judul() | Menampilkan menu utama program. |
| tampilkan_menu() | Menampilkan seluruh data menu kantin. |
| validasi_angka() | Memvalidasi input agar berupa angka positif. |
| filter_budget() | Menyaring menu berdasarkan budget pengguna. |
| filter_kategori() | Menyaring menu berdasarkan kategori. |
| cari_menu_nama() | Mencari menu berdasarkan nama menggunakan Linear Search. |
| sorting_harga() | Mengurutkan menu berdasarkan harga. |
| rekomendasi_acak() | Memberikan rekomendasi menu secara acak. |
| tampilkan_hasil() | Menampilkan hasil filter, pencarian, sorting, maupun rekomendasi. |

---

## Cara Menjalankan Program

1. Pastikan Python 3 telah terinstal pada komputer.
2. Clone repository atau download project.
3. Buka project menggunakan Visual Studio Code atau terminal.
4. Jalankan program menggunakan perintah:

```bash
python nama_file.py
```

5. Pilih menu sesuai kebutuhan.

---

## Pengujian Program

Program telah diuji menggunakan beberapa skenario berikut.

| Pengujian | Hasil |
|------------|--------|
| Menampilkan Menu | ✅ Berhasil |
| Filter Budget | ✅ Berhasil |
| Filter Kategori | ✅ Berhasil |
| Searching Nama | ✅ Berhasil |
| Sorting Harga | ✅ Berhasil |
| Rekomendasi Acak | ✅ Berhasil |
| Validasi Input | ✅ Berhasil |
| Keluar Program | ✅ Berhasil |

---

## Edge Cases yang Ditangani

Program telah menangani berbagai kondisi khusus, antara lain:

- Input kosong.
- Input bukan angka.
- Budget bernilai negatif.
- Kategori tidak valid.
- Kata kunci pencarian kosong.
- Data tidak ditemukan.
- Jumlah rekomendasi melebihi jumlah menu.
- Jumlah rekomendasi bernilai nol.
- Pilihan menu di luar rentang 1–8.

---

## Kesimpulan

Program Sistem Rekomendasi Menu Kantin berhasil dibuat dan dapat berjalan dengan baik tanpa error. Program telah menerapkan penggunaan struktur data List dan Dictionary, Function, Searching, Sorting, Random Recommendation, serta validasi input. Dengan adanya fitur-fitur tersebut, pengguna dapat memilih menu kantin dengan lebih mudah sesuai kebutuhan dan budget yang dimiliki.

---

## Penulis

**Nama :** Julia Ardhana

**NIM :** (Isi NIM Anda)

**Mata Kuliah :** Algoritma Pemrograman
