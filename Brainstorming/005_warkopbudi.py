#Mencoba Tugas Mahasiswa Informatika Itenas

print("==============================")
print("     WARUNG KOPI PAK BUDI     ")
print("==============================\n")

nama = input("Masukkan nama Pembeli\t: ")
print(f"Halo {nama.upper()}, Mau pesen menu apa?\n")

print("==============================")
print("       MENU WARKOP BUDI       ")
print("==============================")

menu = int(print("1 : Josu\n2 : Kopsu\n3 : Kumsu\n4 : Gulaku"))
jumlahmenu = 0
print("==============================")

while True:
    pilihan = input("Mau pesen apa\t: \n(1-4 / ga)\t: ")

    if pilihan == "ga":
        uangpembeli = int(input("Berapa Uangmu\t: "))
        print("Total\t: ",uangpembeli - (menu * jumlahmenu))
        break

    elif pilihan == 