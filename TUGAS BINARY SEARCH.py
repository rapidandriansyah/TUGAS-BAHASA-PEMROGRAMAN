# Fungsi untuk mengurutkan produk berdasarkan harga
def urutkan_produk_berdasarkan_harga(produk):
    return sorted(produk, key=lambda x: x['harga'])

# Fungsi untuk melakukan binary search berdasarkan harga
def binary_search_berdasarkan_harga(produk, target_harga):
    rendah = 0
    tinggi = len(produk) - 1

    while rendah <= tinggi:
        tengah = (rendah + tinggi) // 2
        if produk[tengah]['harga'] == target_harga:
            return tengah  # Mengembalikan indeks produk yang dicari
        elif produk[tengah]['harga'] < target_harga:
            rendah = tengah + 1
        else:
            tinggi = tengah - 1

    return -1  # Mengembalikan -1 jika produk tidak ditemukan

# Contoh penggunaan
produk = [
    {"NAMA PRODUK": "MIE", "HARGA": 30000},
    {"NAMA PRODUK": "KOPI", "HARGA": 20000},
    {"NAMA PRODUK": "SUSU", "HARGA": 50000},
    {"NAMA PRODUK": "ROTI", "HARGA": 40000},
    {"NAMA PRODUK": "TELUR", "HARGA": 10000}
]

# Mengurutkan produk berdasarkan harga
produk_terurut = urutkan_produk_berdasarkan_harga(produk)

# Menampilkan produk yang sudah diurutkan
print("PRODUK YANG SUDAH DIURUTKAN:")
for p in produk_terurut:
    print(f"{p['nama']} - Rp{p['harga']}")

# Harga target yang ingin dicari
target_harga = 40000
hasil = binary_search_berdasarkan_harga(produk_terurut, target_harga)
if hasil != -1:
    print(f"PRODUK DITEMUKAN: {produk_terurut[hasil]['nama']} - Rp{produk_terurut[hasil]['harga']}")
else:
    print("PRODUK TIDAK DITEMUKAN")
