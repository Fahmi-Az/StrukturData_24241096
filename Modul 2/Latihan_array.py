# Praktek 1 : Membuat array
import numpy as np

# Membuat array dengan numpy
nilai_siswa = np.array([85, 55, 40, 90])

# Akses data pada array
print(nilai_siswa[3])


# Praktek 2 : Mengakses, Mengubah, dan Cek Ukuran dan Dimensi Array
nilai_siswa_1 = np.array([75, 65, 45, 80])
nilai_siswa_2 = np.array([[85, 55, 40], [50, 40, 99]])

# Akses elemen array
print(nilai_siswa_1[0])
print(nilai_siswa_2[1][1])

# Ubah nilai elemen array
nilai_siswa_1[0] = 88
nilai_siswa_2[1][1] = 70

# Cek perubahan
print(nilai_siswa_1[0])
print(nilai_siswa_2[1][1])

# Cek ukuran dan dimensi array
print("Ukuran Array 1:", nilai_siswa_1.shape)
print("Ukuran Array 2:", nilai_siswa_2.shape)
print("Dimensi Array 2:", nilai_siswa_2.ndim)


# Praktek 3 : Operasi Aritmatika Pada Array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Operasi penjumlahan array
print(a + b)

# Indexing dan Slicing
arr = np.array([10, 20, 30, 40])
print(arr[1:3])

# Iterasi pada array
for x in arr:
    print(x)


# Praktek 4 : Linear Traversal
arr = [1, 2, 3, 4, 5]
print("Linear Traversal:", end=" ")
for i in arr:
    print(i, end=" ")
print()


# Praktek 5 : Reverse Traversal
arr = [1, 2, 3, 4, 5]
print("Reverse Traversal:", end=" ")
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
print()


# Praktek 7 : Linear Traversal dengan While
arr = [1, 2, 3, 4, 5]
i = 0
print("Linear Traversal (while):", end=" ")
while i < len(arr):
    print(arr[i], end=" ")
    i += 1
print()


# Praktek 8 : Reverse Traversal dengan While
arr = [1, 2, 3, 4, 5]
start = 0
end = len(arr) - 1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print("Reverse Traversal (while):", arr)


# Praktek 9 : Insertion di Akhir Array
arr = [12, 16, 20, 40, 50, 70]
print("Array Sebelum Insertion:", arr)
print("Panjang Array:", len(arr))
arr.append(26)
print("Array Setelah Insertion:", arr)
print("Panjang Array:", len(arr))


# Praktek 10 : Insertion di Tengah Array
arr = [12, 16, 20, 40, 50, 70]
print("Array Sebelum Insertion:", arr)
print("Panjang Array:", len(arr))
arr.insert(4, 5)
print("Array Setelah Insertion:", arr)
print("Panjang Array:", len(arr))


# Insertion tanpa fungsi insert()
arr = [12, 16, 20, 40, 50, 70]
print("Array Sebelum Penyisipan:", arr)
pos = 4
x = 5
arr.append(0)
for i in range(len(arr) - 2, pos - 1, -1):
    arr[i + 1] = arr[i]
arr[pos] = x
print("Array Sesudah Penyisipan:", arr)


# Praktek 11 : Menghapus Array
a = [10, 20, 30, 40, 50]
print("Array Sebelum Deletion:", a)
a.remove(30)
print("Setelah remove(30):", a)
popped_val = a.pop(1)
print("Popped element:", popped_val)
print("Setelah pop(1):", a)
del a[0]
print("Setelah del a[0]:", a)
