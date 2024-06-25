# Fungsi untuk melakukan pencarian sequential berdasarkan ID produk
def sequential_search(produk, id_produk):
    for i in range(len(produk)):
        if produk[i]['ID'] == id_produk:
            return i  # Mengembalikan indeks jika ditemukan
    return -1  # Mengembalikan -1 jika tidak ditemukan

# Contoh penggunaan dengan input otomatis
produk = [
    {'ID': 101, 'NAMA': 'MIE', 'JUMLAH': 50},
    {'ID': 102, 'NAMA': 'KOPI', 'JUMLAH': 20},
    {'ID': 103, 'NAMA': 'SUSU', 'JUMLAH': 30},
    {'ID': 104, 'NAMA': 'TELUR', 'JUMLAH': 15},
    {'ID': 105, 'NAMA': 'ROTI', 'JUMLAH': 60}
]

# Menampilkan daftar produk
print("DAFTAR PRODUK:")
for p in produk:
    print(f"ID: {p['ID']}, NAMA: {p['NAMA']}, JUMLAH: {p['JUMLAH']}")

# Meminta input dari pengguna
try:
    id_produk = int(input("MASUKKAN ID PRODUK YANG INGIN DICARI: "))

    hasil = pencarian_sequential(produk, id_produk)
    if hasil != -1:
        print(f"PRODUK DITEMUKAN DI INDEKS {hasil}: {produk[hasil]}")
    else:
        print("PROODUK TIDAK DITEMUKAN DALAM DAFTAR")
except ValueError:
    print("ID PRODUK HARUS BERUPA ANGKA.")
