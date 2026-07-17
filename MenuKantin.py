import random

def inisialisasi_database() -> dict:
    """
    Menginisialisasi dan mengembalikan database menu kantin dalam bentuk dictionary.
    Dictionary menggunakan nama menu sebagai key, dan detail (harga, kategori) sebagai value.
    
    Returns:
        dict: Database menu awal.
    """
    return {
        "Nasi Goreng": {"harga": 15000, "kategori": "makanan"},
        "Mie Ayam": {"harga": 12000, "kategori": "makanan"},
        "Ayam Geprek": {"harga": 18000, "kategori": "makanan"},
        "Es Teh Manis": {"harga": 5000, "kategori": "minuman"},
        "Es Jeruk": {"harga": 6000, "kategori": "minuman"},
        "Siomay": {"harga": 10000, "kategori": "cemilan"}
    }

def tambah_menu(db: dict, nama: str, harga: int, kategori: str) -> bool:
    """
    Menambahkan menu baru ke dalam database.
    Menangani edge case: validasi tipe data input, harga negatif, string kosong, dan duplikasi nama.
    
    Args:
        db (dict): Database menu saat ini.
        nama (str): Nama menu baru.
        harga (int): Harga menu baru.
        kategori (str): Kategori menu baru (makanan/minuman/cemilan).
        
    Returns:
        bool: True jika berhasil ditambahkan, False jika gagal (karena edge case).
    """
    # Edge case: Validasi tipe data dan string kosong
    if not isinstance(nama, str) or not nama.strip():
        print("[Error] Nama menu tidak valid atau kosong.")
        return False
    if not isinstance(harga, int) or harga < 0:
        print("[Error] Harga tidak valid, harus berupa angka bulat positif.")
        return False
    if not isinstance(kategori, str) or not kategori.strip():
        print("[Error] Kategori tidak valid.")
        return False
        
    nama_key = nama.strip().title()
    
    # Edge case: Duplikasi menu
    if nama_key in db:
        print(f"[Error] Menu '{nama_key}' sudah ada di database.")
        return False
        
    db[nama_key] = {"harga": harga, "kategori": kategori.strip().lower()}
    return True

def cari_menu(db: dict, kata_kunci: str) -> list:
    """
    Algoritma Searching (Linear Search - Substring Matching) untuk mencari menu.
    Menangani edge case jika list kosong atau kata kunci tidak valid.
    
    Args:
        db (dict): Database menu.
        kata_kunci (str): Kata kunci pencarian.
        
    Returns:
        list: Daftar menu (list of dict) yang cocok dengan kata kunci.
    """
    # Edge case: Kata kunci invalid / kosong
    if not isinstance(kata_kunci, str) or not kata_kunci.strip():
        print("[Warning] Kata kunci pencarian kosong/invalid.")
        return []
        
    hasil_cari = []
    kata_kunci_lower = kata_kunci.strip().lower()
    
    for nama, detail in db.items():
        if kata_kunci_lower in nama.lower():
            hasil_cari.append({
                "nama": nama,
                "harga": detail["harga"],
                "kategori": detail["kategori"]
            })
            
    return hasil_cari

def filter_menu(db: dict, budget: int = None, kategori: str = None) -> list:
    """
    Melakukan filtering (penyaringan) menu berdasarkan budget maksimal dan/atau kategori.
    Menangani edge cases seperti tipe data invalid atau budget negatif.
    
    Args:
        db (dict): Database menu.
        budget (int, optional): Maksimal harga.
        kategori (str, optional): Kategori menu yang dicari.
        
    Returns:
        list: Daftar menu yang lolos filter.
    """
    rekomendasi = []
    
    # Edge cases: Validasi filter input
    if budget is not None and (not isinstance(budget, int) or budget < 0):
        print(f"[Warning] Budget '{budget}' tidak valid. Filter budget diabaikan.")
        budget = None
        
    if kategori is not None and (not isinstance(kategori, str) or not kategori.strip()):
        print("[Warning] Kategori tidak valid. Filter kategori diabaikan.")
        kategori = None
        
    for nama, detail in db.items():
        harga_menu = detail["harga"]
        kat_menu = detail["kategori"]
        
        kondisi_budget = (budget is None) or (harga_menu <= budget)
        kondisi_kategori = (kategori is None) or (kat_menu.lower() == kategori.strip().lower())
        
        if kondisi_budget and kondisi_kategori:
            rekomendasi.append({
                "nama": nama,
                "harga": harga_menu,
                "kategori": kat_menu
            })
            
    return rekomendasi

def urutkan_menu(daftar_menu: list, descending: bool = False) -> list:
    """
    Algoritma Sorting (Bubble Sort) manual untuk mengurutkan daftar menu berdasarkan harga.
    Menangani edge case jika list kosong atau hanya berisi 1 elemen.
    
    Args:
        daftar_menu (list): Daftar menu dalam bentuk list of dictionary.
        descending (bool): Jika True, urutkan dari mahal ke murah. Default False (murah ke mahal).
        
    Returns:
        list: Daftar menu yang sudah diurutkan.
    """
    n = len(daftar_menu)
    
    # Edge case: jika list kosong atau 1 elemen, tidak perlu di-sort
    if n <= 1:
        return daftar_menu
        
    # Copy list untuk menerapkan pure function approach (tidak memodifikasi argumen asli)
    sorted_list = daftar_menu.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            harga_kiri = sorted_list[j]["harga"]
            harga_kanan = sorted_list[j+1]["harga"]
            
            if descending:
                tukar = harga_kiri < harga_kanan
            else:
                tukar = harga_kiri > harga_kanan
                
            if tukar:
                # Swap posisi
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                
    return sorted_list

def rekomendasi_acak(daftar_menu: list) -> dict:
    """
    Memilih satu menu secara acak dari daftar yang diberikan.
    Menangani edge case list kosong.
    
    Args:
        daftar_menu (list): Daftar menu (list of dict).
        
    Returns:
        dict or None: Satu item menu, atau None jika list kosong.
    """
    # Edge case: List kosong atau tipe data bukan list
    if not isinstance(daftar_menu, list) or len(daftar_menu) == 0:
        return None
        
    return random.choice(daftar_menu)

def tampilkan_daftar_menu(daftar_menu: list, judul: str = "Daftar Menu") -> None:
    """
    Menampilkan daftar menu ke layar dengan format yang rapi.
    Menangani edge case list kosong.
    
    Args:
        daftar_menu (list): Daftar menu yang akan ditampilkan.
        judul (str): Judul tampilan.
    """
    print(f"\n=== {judul} ===")
    
    # Edge case: Tampilan jika data kosong
    if not daftar_menu:
        print("[-] Tidak ada data yang dapat ditampilkan (Kosong).")
        return
        
    for i, item in enumerate(daftar_menu, start=1):
        print(f"{i}. {item['nama']:<15} - Rp{item['harga']:>5} ({item['kategori']})")
        
def main():
    """
    Fungsi utama (Main) untuk mengeksekusi program dan mencontohkan hasil dari 
    masing-masing fungsi, algoritma, serta pengujian edge cases.
    """
    print("Mulai Program...\n")
    db = inisialisasi_database()
    
    # 1. Tampilkan Semua Menu Awal
    semua_menu = [{"nama": k, "harga": v["harga"], "kategori": v["kategori"]} for k, v in db.items()]
    tampilkan_daftar_menu(semua_menu, "Semua Menu di Database Awal")
    
    # 2. [Tes Edge Cases] Fungsi Tambah Menu
    print("\n>>> [Tes Edge Case] Penambahan Menu Baru:")
    sukses = tambah_menu(db, "Sate Madura", 20000, "makanan")
    if sukses: print("[Sukses] Sate Madura ditambahkan.")
    
    print("Menguji input tidak valid:")
    tambah_menu(db, "Sate Madura", 25000, "makanan")  # Duplikat
    tambah_menu(db, "Cilok", -5000, "cemilan")        # Harga negatif
    tambah_menu(db, "", 5000, "minuman")              # Nama kosong
    
    # 3. [Tes Searching] Algoritma Linear Substring Search
    print("\n>>> [Tes Searching] Mencari kata kunci 'Ayam':")
    hasil_cari = cari_menu(db, "Ayam")
    tampilkan_daftar_menu(hasil_cari, "Hasil Pencarian 'Ayam'")
    
    # 4. [Tes Filtering] Beserta Edge Case Budget Tidak Valid
    print("\n>>> [Tes Filtering Edge Case] Budget -10000 (Invalid), Kategori 'cemilan':")
    hasil_filter_invalid = filter_menu(db, budget=-10000, kategori="cemilan")
    
    print("\n>>> [Tes Filtering Valid] Maksimal Budget Rp15000, Kategori 'makanan':")
    hasil_filter_valid = filter_menu(db, budget=15000, kategori="makanan")
    tampilkan_daftar_menu(hasil_filter_valid, "Hasil Filter (Maks Rp15.000, Makanan)")
    
    # 5. [Tes Sorting] Algoritma Bubble Sort Manual
    print("\n>>> [Tes Sorting] Mengurutkan Hasil Filter dari Mahal ke Murah:")
    hasil_urut = urutkan_menu(hasil_filter_valid, descending=True)
    tampilkan_daftar_menu(hasil_urut, "Hasil Filter (Diurutkan Descending)")
    
    # 6. [Tes Rekomendasi Acak] Dan Edge Case List Kosong
    print("\n>>> [Tes Acak Edge Case] Memasukkan list kosong:")
    acak_kosong = rekomendasi_acak([])
    print(f"Hasil List Kosong: {acak_kosong}")
    
    print("\n>>> [Tes Acak Valid] Dari hasil pencarian (filtering):")
    acak_valid = rekomendasi_acak(hasil_filter_valid)
    if acak_valid:
        print(f"Berdasarkan filter, kamu direkomendasikan: {acak_valid['nama']} (Rp{acak_valid['harga']})")

if __name__ == "__main__":
    main()

# =========================================================================================
# AI USAGE LOG (Catatan Reflektif)
# =========================================================================================
# 1. Instruksi / Masalah: 
#    - Program Menu Kantin butuh restrukturisasi mengikuti kriteria Alprog (Algoritma dan 
#      Pemrograman).
#    - Membutuhkan minimal 7 fungsi terpisah dengan docstring, perpaduan dict + list, 
#      serta wajib mengimplementasi searching, sorting secara spesifik.
#    - Penanganan ketat terhadap segala macam edge cases agar "Error-Free".
# 
# 2. Pendekatan AI & Penyelesaian:
#    - Struktur Data: Tetap menggunakan kombinasi `dict` sebagai basis NoSQL-like map 
#      untuk pencarian spesifik nama cepat O(1), dan mengubahnya menjadi `list of dict` 
#      untuk proses iteratif seperti Searching dan Sorting.
#    - Algoritma Searching: Menerapkan O(N) Linear Search dengan substring checking 
#      menggunakan Python `in` operator pada lowercase string. Sangat efektif untuk 
#      kasus menu (misal mencari "ayam" pada "Mie Ayam").
#    - Algoritma Sorting: Untuk kebutuhan akademis algoritmik, saya menggunakan explicit 
#      Bubble Sort O(N^2) untuk mendemonstrasikan swapping secara logis alih-alih 
#      menggunakan `.sort()` built-in dari C-Backend.
#    - Edge Cases: Memasang 'Guard Clauses' di tiap awal fungsi menggunakan `isinstance()`
#      serta checking value constraint (`< 0` untuk harga, `.strip()` string kosong, 
#      list yang panjangnya 0/1, filter budget negatif, dsbg).
# 
# 3. Refleksi Hasil:
#    Program sekarang bertransisi dari sekadar "Working Script" menjadi "Robust Module". 
#    Fungsi bersifat 'Pure' (seperti urutkan_menu meng-copy list asli) sehingga program 
#    aman jika diintegrasikan dengan GUI/Interface eksternal tanpa risiko mutasi state
#    secara liar (Side Effects).
# =========================================================================================

Delete AI_Usage_Log
