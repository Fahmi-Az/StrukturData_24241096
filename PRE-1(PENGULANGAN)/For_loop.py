# PENGULANGAN (LOOP)
# For-loop
"""
   for-loop digunakan untuk perulangan
   yang diketahui jumlah perulangannya
   Counted-loop

   syntax: 
    for kondisi:
        aksi 1 - bagian dari loop sebaris
    aksi 2 - bukan bagian dari loop

"""

a = 0
a += 1 # a = a + 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)
# boros line of code

angka = [0,1,5,7,10] 
for i in angka:
    print(f"i saat ini = {i}")
print("ini akhir dari loop\n")

# perulangan menggunakan range (batas)
angka_range = range(5) # diulang lima kali
print(list(angka_range))

for i in angka_range:
    print(f"i saat ini = {i}")
print("ini akhir dari loop 2\n")

angka2_range = range(1,10) # diulang 9 kali
print(list(angka2_range))

for i in angka2_range:
    print(f"i saat ini = {i}")
print("ini akhir dari loop 3\n")

# latihan

string = "MANDALIKA"

for huruf in string:
    print(huruf)