# while-loop
'''
   syntax:
   while kondisi(TRUE): # selama bernilai true
      aksi
'''
angka = 0
print(f"angka awal -> {angka}")

while angka < 5:
    angka += 1 # jika tidak ada maka akan terjadi infinity looping
    print(f"angka sekarang -> {angka}")
print("keluar dari looping")

jawab = 'ya'
hitung = 0

while(jawab == 'ya'):
    hitung =+ 1
    jawab = input("ulangi lagi atau tidak?")
print(f"jumlah pengulangan = {hitung}")