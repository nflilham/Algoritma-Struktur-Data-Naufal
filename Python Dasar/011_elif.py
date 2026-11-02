#Algoritma dan Struktur data Pertemuan 6
#Naufal Ilham Fauzan
#2502106

nilai = int(input("\nMasukkan nilai : "))

if nilai >= 92:
    print("Anda lulus dengan Predikat \'A\'!")
elif nilai >= 76:
    print("Anda lulus dengan Predikat \'B\'!")
elif nilai >= 60:
    print("Anda lulus dengan Predikat \'C\'!")
elif nilai >= 55:
    print("Anda lulus dengan Predikat \'D\'!")
else:
    print("Anda \'TIDAK LULUS!\' Silahkan mengulang tahun depan.")
print("\n")