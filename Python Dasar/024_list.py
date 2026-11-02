# Naufal Ilham Fauzan
# 2502106
# Pertemuan 7 - 5 Oktober 2026

# List kosong
list_kosong = []
print(list_kosong)

# List angka
angka = [1, 2, 3, 4, 5]
print(angka)

# List string / huruf / kata
nama = ["Ajriel", "Ghaniar", "Ega"]
print(nama)

# List campuran
nama_umur = ["Ajriel", 19, "Ghaniar", 75]
print(nama_umur)
print()

# Mengakses elemen
kendaraan = ["Civic Turbo", "XMAX", "Ninja RR", "BMW M4"]
print(kendaraan[0])     # Memanggil civic turbo
print(kendaraan[1])     # Memanggil xmax
print(kendaraan[2])     # Memanggil ninja rr
print(kendaraan[-1])    # Memanggil bmw m4
print()

# Mengubah elemen
kendaraan[2] = "ZX6R"
print(kendaraan[2])

# Menambah list
kendaraan.append("BMW 1000")
print(kendaraan)

# Menghapus list - .remove methode
kendaraan.remove("Civic Turbo")
print(kendaraan)

# Menghapus list - .pop methode
kendaraan.pop(0)
print(kendaraan)

# Menghapus list - del methode
del kendaraan[1]
print(kendaraan)

# Menghitung isi list
print(len(kendaraan))   #Sisa 2
kendaraan.append("Aerox 155 New")
kendaraan.append("Beat Karbu")
print(len(kendaraan))   #4

# Menggabungkan list
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

gabungan = list1 + list2
print(gabungan)
print(len(gabungan))
print()

# Mengecek elemen dalam list
print(kendaraan)
if "Beat Karbu" in kendaraan:
    print("Kamu mempunyai \'Beat Karbu\'!")
else:
    print("Kamu Tidak mempunyai \'Beat Karbu\'!")
print()

# Menggunakan for loop dalam list
buah = ["apel", "mangga", "pisang", "jeruk", "rambutan"]

buah.append("manggis")
buah.append("pir")

print("Buah yang kamu punya: ")
no = 1
for i in buah:
    print(f"{no}. {i}")
    no += 1
print()

# Menggunakan for loop dalam list dengan index
print("Buah yang kamu punya: ")
for i in range(len(buah)):
    print(str(i+1) + ".", buah[i])
print()

print()