import random

# ==========================================
# PROYEK AKHIR ALGORITMA PEMROGRAMAN
# SISTEM REKOMENDASI MENU KANTIN
# ==========================================

# Database menu kantin
menu_kantin = [
    {"nama": "Nasi Goreng", "kategori": "Makanan", "harga": 15000},
    {"nama": "Mie Ayam", "kategori": "Makanan", "harga": 12000},
    {"nama": "Bakso", "kategori": "Makanan", "harga": 13000},
    {"nama": "Ayam Geprek", "kategori": "Makanan", "harga": 18000},
    {"nama": "Sate Ayam", "kategori": "Makanan", "harga": 20000},
    {"nama": "Es Teh", "kategori": "Minuman", "harga": 5000},
    {"nama": "Jus Alpukat", "kategori": "Minuman", "harga": 10000},
    {"nama": "Kopi Susu", "kategori": "Minuman", "harga": 12000},
    {"nama": "Roti Bakar", "kategori": "Snack", "harga": 8000},
    {"nama": "Kentang Goreng", "kategori": "Snack", "harga": 10000},
    {"nama": "Pisang Coklat", "kategori": "Snack", "harga": 9000}
]

# List untuk menyimpan hasil rekomendasi / hasil filter terakhir
rekomendasi = []


def tampilkan_judul():
    """
    Menampilkan judul program dan menu utama.
    """
    print("\n" + "=" * 50)
    print("         SISTEM REKOMENDASI MENU KANTIN")
    print("=" * 50)
    print("1. Tampilkan semua menu")
    print("2. Filter menu berdasarkan budget")
    print("3. Filter menu berdasarkan kategori")
    print("4. Cari menu berdasarkan nama")
    print("5. Urutkan menu berdasarkan harga")
    print("6. Rekomendasi menu acak")
    print("7. Lihat hasil rekomendasi terakhir")
    print("8. Keluar")
    print("=" * 50)


def tampilkan_menu(data_menu):
    """
    Menampilkan daftar menu yang diberikan ke layar.
    Jika data kosong, program akan menampilkan pesan bahwa menu tidak tersedia.
    """
    if len(data_menu) == 0:
        print("Menu tidak tersedia.")
        return

    print("\n===== DAFTAR MENU =====")
    for i in range(len(data_menu)):
        print(f"{i+1}. {data_menu[i]['nama']} | {data_menu[i]['kategori']} | Rp{data_menu[i]['harga']}")


def validasi_angka(input_user):
    """
    Memeriksa apakah input dari user berupa angka bulat positif.
    Mengembalikan integer jika valid, dan None jika tidak valid.
    """
    if input_user.strip() == "":
        return None

    if not input_user.isdigit():
        return None

    nilai = int(input_user)
    if nilai < 0:
        return None

    return nilai


def filter_budget(data_menu, budget):
    """
    Menyaring menu berdasarkan budget maksimum.
    Hanya menu dengan harga <= budget yang akan dimasukkan ke hasil.
    """
    hasil = []
    for menu in data_menu:
        if menu["harga"] <= budget:
            hasil.append(menu)
    return hasil


def filter_kategori(data_menu, kategori):
    """
    Menyaring menu berdasarkan kategori yang dipilih pengguna.
    Contoh kategori: Makanan, Minuman, atau Snack.
    """
    hasil = []
    for menu in data_menu:
        if menu["kategori"].lower() == kategori.lower():
            hasil.append(menu)
    return hasil


def cari_menu_nama(data_menu, kata_kunci):
    """
    Mencari menu berdasarkan nama menu.
    Program akan menampilkan menu yang namanya mengandung kata kunci tertentu.
    """
    hasil = []
    for menu in data_menu:
        if kata_kunci.lower() in menu["nama"].lower():
            hasil.append(menu)
    return hasil


def sorting_harga(data_menu, urutan="asc"):
    """
    Mengurutkan menu berdasarkan harga.
    asc  = dari harga termurah ke termahal
    desc = dari harga termahal ke termurah
    """
    hasil = data_menu.copy()

    for i in range(len(hasil)):
        for j in range(i + 1, len(hasil)):
            if urutan == "asc":
                if hasil[i]["harga"] > hasil[j]["harga"]:
                    hasil[i], hasil[j] = hasil[j], hasil[i]
            elif urutan == "desc":
                if hasil[i]["harga"] < hasil[j]["harga"]:
                    hasil[i], hasil[j] = hasil[j], hasil[i]

    return hasil


def rekomendasi_acak(data_menu, jumlah):
    """
    Mengambil beberapa menu secara acak dari data menu.
    Jika jumlah melebihi jumlah menu, maka jumlah akan disesuaikan.
    """
    if len(data_menu) == 0:
        return []

    if jumlah > len(data_menu):
        jumlah = len(data_menu)

    return random.sample(data_menu, jumlah)


def tampilkan_hasil(hasil, judul):
    """
    Menampilkan hasil proses seperti filter, searching, sorting,
    atau rekomendasi dengan format yang lebih rapi.
    """
    print(f"\n===== {judul} =====")
    if len(hasil) == 0:
        print("Data tidak ditemukan.")
    else:
        for i in range(len(hasil)):
            print(f"{i+1}. {hasil[i]['nama']} | {hasil[i]['kategori']} | Rp{hasil[i]['harga']}")


# ==========================================
# PROGRAM UTAMA
# ==========================================
while True:
    tampilkan_judul()
    pilihan = input("Masukkan pilihan menu (1-8): ").strip()

    if pilihan == "1":
        tampilkan_menu(menu_kantin)

    elif pilihan == "2":
        budget_input = input("Masukkan budget maksimal: Rp")
        budget = validasi_angka(budget_input)

        if budget is None:
            print("Input budget harus berupa angka positif.")
        else:
            hasil_budget = filter_budget(menu_kantin, budget)
            rekomendasi = hasil_budget.copy()
            tampilkan_hasil(hasil_budget, "HASIL FILTER BUDGET")

    elif pilihan == "3":
        kategori = input("Masukkan kategori (Makanan/Minuman/Snack): ").strip()

        if kategori == "":
            print("Kategori tidak boleh kosong.")
        elif kategori.lower() not in ["makanan", "minuman", "snack"]:
            print("Kategori tidak valid. Pilih: Makanan, Minuman, atau Snack.")
        else:
            hasil_kategori = filter_kategori(menu_kantin, kategori)
            rekomendasi = hasil_kategori.copy()
            tampilkan_hasil(hasil_kategori, "HASIL FILTER KATEGORI")

    elif pilihan == "4":
        kata_kunci = input("Masukkan nama menu yang ingin dicari: ").strip()

        if kata_kunci == "":
            print("Kata kunci pencarian tidak boleh kosong.")
        else:
            hasil_cari = cari_menu_nama(menu_kantin, kata_kunci)
            rekomendasi = hasil_cari.copy()
            tampilkan_hasil(hasil_cari, "HASIL PENCARIAN MENU")

    elif pilihan == "5":
        print("\nUrutkan harga:")
        print("1. Murah ke mahal")
        print("2. Mahal ke murah")
        pilih_urut = input("Pilih urutan (1/2): ").strip()

        if pilih_urut == "1":
            hasil_sort = sorting_harga(menu_kantin, "asc")
            tampilkan_hasil(hasil_sort, "MENU DIURUTKAN DARI HARGA TERMURAH")
        elif pilih_urut == "2":
            hasil_sort = sorting_harga(menu_kantin, "desc")
            tampilkan_hasil(hasil_sort, "MENU DIURUTKAN DARI HARGA TERMAHAL")
        else:
            print("Pilihan urutan tidak valid.")

    elif pilihan == "6":
        print("\nRekomendasi bisa diambil dari:")
        print("1. Semua menu")
        print("2. Hasil filter/pencarian terakhir")
        sumber = input("Pilih sumber rekomendasi (1/2): ").strip()

        jumlah_input = input("Berapa menu yang ingin direkomendasikan? ")
        jumlah = validasi_angka(jumlah_input)

        if jumlah is None or jumlah == 0:
            print("Jumlah rekomendasi harus berupa angka dan lebih dari 0.")
        else:
            if sumber == "1":
                hasil_random = rekomendasi_acak(menu_kantin, jumlah)
                rekomendasi = hasil_random.copy()
                tampilkan_hasil(hasil_random, "REKOMENDASI MENU ACAK")
            elif sumber == "2":
                if len(rekomendasi) == 0:
                    print("Belum ada hasil filter/pencarian yang bisa direkomendasikan.")
                else:
                    hasil_random = rekomendasi_acak(rekomendasi, jumlah)
                    rekomendasi = hasil_random.copy()
                    tampilkan_hasil(hasil_random, "REKOMENDASI ACAK DARI HASIL TERAKHIR")
            else:
                print("Pilihan sumber rekomendasi tidak valid.")

    elif pilihan == "7":
        tampilkan_hasil(rekomendasi, "HASIL REKOMENDASI / FILTER TERAKHIR")

    elif pilihan == "8":
        print("Terima kasih telah menggunakan Sistem Rekomendasi Menu Kantin.")
        break

    else:
        print("Pilihan menu tidak valid. Silakan pilih 1 sampai 8.")