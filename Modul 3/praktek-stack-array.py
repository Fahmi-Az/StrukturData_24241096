# Membuat wadah Stack
stack = []

# Push menggunakan operasi push untuk menambah elemen pada stack
# operasi menambah elemen pada array menggunakan .append()
stack.append('5')
stack.append('17')
stack.append('30')
stack.append('15')
stack.append('77')

# cetak stack
print ("Stack : ", stack)

# cari tahu ukuran stack
print("ukuran stack : ", len(stack))

# pop menggunakan operasi top cek puncak dari stack
if len(stack) != 0:
    print("Pop : ", stack.pop())
    print("Stack setelah di hapus : ", stack)
else:
    print("stack kosong")