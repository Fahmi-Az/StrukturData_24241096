# Program Rekapitulasi Nilai Mahasiswa // MIZII

data_mahasiswa = {}

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa ke-{i+1}")
    nim = input("Masukkan NIM: ")

    nama = input("Masukkan Nama: ")
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))

    mata_kuliah = []
    for j in range(jumlah_matkul):
        
        while True:
            matkul = input(f"  Nama Mata Kuliah ke-{j+1}: ")
            if all(c.isalpha() or c.isspace() for c in matkul) and matkul.strip() != "":
                break
            else:
                print("  ❌ Nama mata kuliah harus berupa huruf dan tidak boleh mengandung angka!")

        
        while True:
            try:
                nilai = float(input(f"  Nilai Mata Kuliah '{matkul}': "))
                break
            except ValueError:
                print("  ❌ Nilai harus berupa angka (misal: 80 atau 75.5)!")

        mata_kuliah.append((matkul, nilai))

    
    data_mahasiswa[nim] = (nama, mata_kuliah)

print("\n=== Rekap Data Mahasiswa ===")
for nim, (nama, nilai_list) in data_mahasiswa.items():
    total_nilai = sum(nilai for _, nilai in nilai_list)
    rata_rata = total_nilai / len(nilai_list) if nilai_list else 0

    print(f"\nNIM   : {nim}")
    print(f"Nama  : {nama}")
    print("Nilai Mata Kuliah:")
    for matkul, nilai in nilai_list:
        print(f"  - {matkul}: {nilai}")
    print(f"Rata-rata Nilai: {rata_rata:.2f}")


print("\n=== Cari Data Mahasiswa ===")
cari_nim = input("Masukkan NIM yang ingin dicari: ")

if cari_nim in data_mahasiswa:
    nama, nilai_list = data_mahasiswa[cari_nim]
    print(f"\nData Mahasiswa dengan NIM {cari_nim}")
    print(f"Nama  : {nama}")
    print("Nilai Mata Kuliah:")
    for matkul, nilai in nilai_list:
        print(f"  - {matkul}: {nilai}")
    rata_rata = sum(nilai for _, nilai in nilai_list) / len(nilai_list)
    print(f"Rata-rata Nilai: {rata_rata:.2f}")
else:
    print("❌ Data dengan NIM tersebut tidak ditemukan.")
