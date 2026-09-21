#String dan Manipulasi String -- Algoritma dan Struktur Data
#21 September 2026

#Naufal Ilham Fauzan
#2502106

nama = "Naufal Ilham Fauzan"
umur = 20

print("Halo nama saya " + nama + " umur saya " + str(umur) + " tahun.")

pesan = "Halo nama saya " + nama + " umur saya " + str(umur) + " tahun."

print(pesan)            #Mengecek apakah print biasa dan print pesan sama
print(type(pesan))      #Mengecek tipe data dari pesan

print(len(nama))        #Mengecek panjang string dari nama
print(len(str(umur)))   #Mengecek panjang string dari umur
print(len(pesan))       #Mengecek panjang string dari pesan

#str berfungsi untuk mengubah tipe data menjadi string
#len berfungsi untuk menghitung panjang karakter dari string