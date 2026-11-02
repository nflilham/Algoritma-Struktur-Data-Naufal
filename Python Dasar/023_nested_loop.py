# Tabel perkalian lengkap
print("==============================")
print("     Tabel Perkalian 1-10     ")
print("==============================")

for i in range(1, 11):
    for j in range(1, 11):
        hasil = i * j
        print(">", i, "X", j, "=", hasil)
    print("==============================")