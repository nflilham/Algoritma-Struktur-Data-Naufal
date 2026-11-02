#Materi indexing string -- Algoritma dan Struktur Data Pertemuan 5
#Naufal Ilham Fauzan
#2502106

#index
pesan = "Python"
print(pesan[0])
print(pesan[1])
print(pesan[2])
print(pesan[3])
print(pesan[4])
print(pesan[5],"\n")
#/n berfungsi untuk membuat baris baru

#negative index
print(pesan[-1])     #Mengambil karakter terakhir dari string
print(pesan[-2])     #Mengambil karakter kedua dari belakang string
print(pesan[-3])     #Mengambil karakter ketiga dari belakang string
print(pesan[-4])     #Mengambil karakter keempat dari belakang string
print(pesan[-5])     #Mengambil karakter kelima dari belakang string
print(pesan[-6],"\n")     #Mengambil karakter keenam dari belakang string

#slicing string
print(pesan[0:3])
print(pesan[3:])
print(pesan[:3])    
print(pesan[:])
print(pesan[0:6],"\n")

#String methode
nama = "ajril lutpi"
namagede = nama.upper()
namakecil = nama.lower()
namajudul = nama.title()
namakapital = nama.capitalize()
namakosong = nama.strip()
namaganti = nama.replace("lutpi", "ganteng")
namahitung = nama.count("i")
namacari = nama.find("lutpi")


#print
print(nama)
print(nama.upper())
print(namagede)
print(namakecil)
print(namajudul)
print(namakapital)
print(namakosong)
print(namaganti)
print(namahitung)
print(namacari)