#Tugas 8 Algoritma dan Struktur Data
#Kalkulator Sederhana
#Naufal Ilham Fauzan
#2502106

#Mencoba menggunakan While agar bisa mengulang lagi
header = "\n=============================="

print(header, "\n     Kalkulator Sederhana\t", header)
pilihan = int(input("Halo! Mau melakukan operasi apa?\n1 : Penjumlahan\n2 : Pengurangan\n3 : Perkalian\n4 : Pembagian\n5 : Modulus\n6 : Perpangkatan\n7 : Pembagian bulat\nPilih mode operasi (1-7): "))

if pilihan == 1:
    print(header)
    angka1 = int(input("Angka pertama\t: "))
    angka2 = int(input("Angka Kedua\t: "))
    angka3 = int(input("Angka Ketiga\t: "))

    hasil = angka1 + angka2 + angka3
    print("\nHasil penjumlahan anda = ", hasil, header)
    
elif pilihan == 2:
    print(header)
    angka1 = int(input("Angka pertama\t: "))
    angka2 = int(input("Angka Kedua\t: "))
    angka3 = int(input("Angka Ketiga\t: "))

    hasil = angka1 - angka2 - angka3
    print("\nHasil pengurangan anda = ", hasil, header)

elif pilihan == 3:
    print(header)
    angka1 = int(input("Angka pertama\t: "))
    angka2 = int(input("Angka Kedua\t: "))
    angka3 = int(input("Angka Ketiga\t: "))

    hasil = angka1 * angka2 * angka3
    print("\nHasil perkalian anda = ", hasil, header)

elif pilihan == 4:
    print(header)
    angka1 = int(input("Angka pertama\t: "))
    angka2 = int(input("Angka Kedua\t: "))
    angka3 = int(input("Angka Ketiga\t: "))

    hasil = angka1 / angka2 / angka3
    print("\nHasil pembagian anda = ", hasil, header)

elif pilihan == 5:
    print(header)
    angka1 = int(input("Angka pertama\t: "))
    angka2 = int(input("Angka Kedua\t: "))
    angka3 = int(input("Angka Ketiga\t: "))

    hasil = angka1 % angka2 % angka3
    print("\nHasil modulus anda = ", hasil, header)

elif pilihan == 6:
    print(header)
    angka1 = int(input("Angka pertama\t: "))
    angka2 = int(input("Angka Kedua\t: "))
    angka3 = int(input("Angka Ketiga\t: "))

    hasil = angka1 ** angka2 ** angka3
    print("\nHasil perpangkatan anda = ", hasil, header)

elif pilihan == 7:
    print(header)
    angka1 = int(input("Angka pertama\t: "))
    angka2 = int(input("Angka Kedua\t: "))
    angka3 = int(input("Angka Ketiga\t: "))

    hasil = angka1 // angka2 // angka3
    print("\nHasil pembagian bulat anda = ", hasil, header)

else :
    print(header)
    print("Pilihan anda tidak valid!", header)