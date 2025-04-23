# Contoh Program Dengan Fungsi
# Variabel global untuk menyimpan data buku
buku = []

# Fungsi show_data()
def show_data():
    if not buku:
        print("DATA BUKU BELUM ADA")
    else:
        for indeks, judul in enumerate(buku):
            print(f"[{indeks}] {judul}")

# Fungsi insert_data()
def insert_data():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)
    print("Buku berhasil ditambahkan!")

# Fungsi edit_data()
def edit_data():
    show_data()
    try:
        indeks = int(input("Inputkan ID Buku : "))
        if 0 <= indeks < len(buku):
            judul_baru = input("Judul Baru : ")
            buku[indeks] = judul_baru
            print("Data buku berhasil diubah!")
        else:
            print("ID Buku Tidak Ditemukan")
    except ValueError:
        print("Input harus berupa angka!")

# Fungsi delete_data()
def delete_data():
    show_data()
    try:
        indeks = int(input("Inputkan ID Buku : "))
        if 0 <= indeks < len(buku):
            print(f"Buku '{buku[indeks]}' telah dihapus.")
            buku.pop(indeks)
        else:
            print("ID Buku Tidak Ditemukan")
    except ValueError:
        print("Input harus berupa angka!")

# Fungsi show_menu()
def show_menu():
    while True:
        print("\n" + "-"*5 + " MENU " + "-"*5)
        print("[1] Show Data")
        print("[2] Insert Data")
        print("[3] Edit Data")
        print("[4] Delete Data")
        print("[5] Exit")
        
        try:
            menu = int(input("PILIH MENU : "))
            print()
            if menu == 1:
                show_data()
            elif menu == 2:
                insert_data()
            elif menu == 3:
                edit_data()
            elif menu == 4:
                delete_data()
            elif menu == 5:
                print("Terima kasih! Program selesai.")
                break
            else:
                print("Pilihan Anda Salah!")
        except ValueError:
            print("Input harus berupa angka!")

# Menjalankan program
show_menu()
