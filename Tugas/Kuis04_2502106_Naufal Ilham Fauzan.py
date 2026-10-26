# Kuis 4
# Naufal Ilham Fauzan
# 2502106
# Algoritma dan Struktur Data

print(f"=== KALKULATOR SEDERHANA ===\n")

while True:

    try:
        pilihan = int(input("Sistem operasi :\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Modulo\n6. Perpangkatan\n0. Exit\nPilih sistem operasi (0-6) : "))
        print()

        if pilihan == 1:
            angka1 = int(input("Masukkan angka ke-1 : "))
            angka2 = int(input("Masukkan angka ke-2 : "))
            hasil = angka1 + angka2
            print(f"Hasil {angka1} + {angka2} = {hasil}\n")

        elif pilihan == 2:
            angka1 = int(input("Masukkan angka ke-1 : "))
            angka2 = int(input("Masukkan angka ke-2 : "))
            hasil = angka1 - angka2
            print(f"hasil {angka1} - {angka2} = {hasil}\n")

        elif pilihan == 3:
            angka1 = int(input("Masukkan angka ke-1 : "))
            angka2 = int(input("Masukkan angka ke-2 : "))
            hasil = angka1 * angka2
            print(f"hasil {angka1} X {angka2} = {hasil}\n")

        elif pilihan == 4:
            try: 
                angka1 = int(input("Masukkan angka ke-1 : "))
                angka2 = int(input("Masukkan angka ke-2 : "))
                hasil = angka1 / angka2
                print(f"hasil {angka1} / {angka2} = {int(hasil)}\n")
            except ZeroDivisionError:
                print("Tidak bisa membagi dengan 0\n")

        elif pilihan == 5:
            angka1 = int(input("Masukkan angka ke-1 : "))
            angka2 = int(input("Masukkan angka ke-2 : "))
            hasil = angka1 % angka2
            print(f"hasil {angka1} Modulo {angka2} = {hasil}\n")

        elif pilihan == 6:
            angka1 = int(input("Masukkan angka ke-1 : "))
            angka2 = int(input("Masukkan angka ke-2 : "))
            hasil = angka1 ** angka2
            print(f"hasil {angka1} Pangkat {angka2} = {hasil}\n")

        elif pilihan == 0:
            print("=== SELESAI ===\n")
            break

        else:
            print("Pilih angka 0-6\n")
            continue
        
        
    except SyntaxError:
        print("Periksa kembali kode penulisan!")
        print()
    except NameError:
        print("Periksa kembali variabel yang ditulis!")
        print()
    except TypeError:
        print("Periksa kembali Tipe Data yang ditulis!")
        print()
    except ValueError:
        print("Masukkan angka/bilangan yang valid!")
        print()