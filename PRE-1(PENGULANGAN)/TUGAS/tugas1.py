baris = int(input("Masukkan jumlah baris bintang: "))

for i in range(baris):
    spasi = ' ' * (baris - i - 1)
    bintang = '*' * (2 * i + 1)
    print(spasi + bintang)
print(f"berikut hasil dari jumlah bintang : {baris}")