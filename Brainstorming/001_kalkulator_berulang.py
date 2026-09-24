#Kalkulator Berulang
#Naufal Ilham Fauzan
#2502106

while True:
    header = "\n=============================="
    print(header, "\nKALKULATOR SEDERHANA", header)

    pilihan = input("Pilih operasi:\n1\t: Pertambahan\n2\t: Pengurangan\n3\t: Perkalian\n4\t: Pembagian\nMasukkan pilihan (1-4): ")

    if pilihan not in ("1", "2", "3", "4"):
        print("Pilihan tidak valid! Silakan pilih angka 1 sampai 4.")
        ulang = input("Apakah ingin mencoba lagi? (y/t): ").lower()
        if ulang != "y":
            print("Program selesai.")
            break
        continue

    print(header)
    angka1 = int(input("Angka pertama\t: "))
    angka2 = int(input("Angka kedua\t: "))

    if pilihan == "1":
        hasil = angka1 + angka2
        print("Hasil penjumlahan anda = ", hasil)

    elif pilihan == "2":
        hasil = angka1 - angka2
        print("Hasil pengurangan anda = ", hasil)

    elif pilihan == "3":
        hasil = angka1 * angka2
        print("Hasil perkalian anda = ", hasil)

    elif pilihan == "4":
        if angka2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
        else:
            hasil = angka1 / angka2
            print("Hasil pembagian anda = ", hasil)

    lanjut = input("Apakah ingin memakai kalkulator lagi? (y/t): ").lower()
    if lanjut != "y":
        print("Program selesai.")
        break

#tes