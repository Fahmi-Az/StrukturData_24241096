batas = int(input("Masukkan batas deret: "))

for i in range(1, batas + 1, 2):
    print(i, end=', ' if i + 2 <= batas else '\n')
print(f"berikut hasil dari deret: {batas}")