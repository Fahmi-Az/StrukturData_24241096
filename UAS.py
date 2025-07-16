# Program Rekapitulasi Belanja Supermarket // MIZII

from datetime import datetime

data_pelanggan = {}


nama = input("Masukkan Nama Pelanggan: ")
tanggal = input("Masukkan Tanggal (format: YYYY-MM-DD): ")

jumlah_barang = int(input("Masukkan jumlah jenis barang yang dibeli: "))
daftar_belanja = []

for j in range(jumlah_barang):
    while True:
        nama_barang = input(f"  Nama Barang ke-{j+1}: ")
        if all(c.isalpha() or c.isspace() for c in nama_barang) and nama_barang.strip() != "":
                break
        else:
                print("  X Nama barang harus berupa huruf dan tidak boleh mengandung angka!")

    while True:
        try:
            harga = float(input(f"  Harga per unit '{nama_barang}': Rp "))
            break
        except ValueError:
                print("  X Harga harus berupa angka (contoh: 15000 atau 12000.5)!")

    while True:
        try:
            jumlah_beli = int(input(f"  Jumlah beli '{nama_barang}': "))
            break
        except ValueError:
                print("  X Jumlah beli harus berupa angka bulat!")

    daftar_belanja.append((nama_barang, harga, jumlah_beli))

    data_pelanggan[nama] = (tanggal, daftar_belanja)

data_pelanggan[nama] = {
 "tanggal": tanggal,
 "belanja": daftar_belanja
}

# OUTPUT:
print("\n=== Rekap Belanja Pelanggan ===")
for nama, info in data_pelanggan.items():
    tanggal = info["tanggal"]
    belanja_list = info["belanja"]
    total_item = sum(jumlah for _, _, jumlah in belanja_list)
    total_belanja = sum(harga * jumlah for _, harga, jumlah in belanja_list)
    
    print(f"\n Data Customer :")
    print(f" Nama          : {nama}")
    print(f" Tanggal       : {tanggal}")
    print(f" Jumlah Barang : {total_item}")
    print(f" Daftar Belanja:")

    for barang, harga, jumlah in belanja_list:
        subtotal = harga * jumlah
        print(f"  - {barang} | Rp {harga:.2f} x {jumlah} = Rp {subtotal:.2f}")

    print(f" Total Belanja : Rp {total_belanja:.2f}")
