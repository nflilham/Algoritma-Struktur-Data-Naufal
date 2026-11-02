# Naufal Ilham Fauzan
# 2502106

# Tipe Error :

# SyntaxError
# VariableError
# TypeError
# ValueError
# IndexError
# KeyError
# ZeroDivisionError

# =================================================

# Penanganan error
# Error handling memungkinkan program untuk menangani error dengan baik tanpa berhenti secara tiba-tiba

# Try-Except
#print(100 / 10)
#print()

#try:
#    print(100/0)
#except:
#    print("Error: Tidak dapat membagi dengan nol")
#print()

# Kalkulator Sederhana Try-Except
# print("=== Pembagian : Kalkulator Sederhana ===")

#try:
#    angka1 = int(input("Masukkan angka ke-1 : "))
#    angka2 = int(input("Masukkan angka ke-2 : "))
#    hasil = angka1/angka2
#    print(f"\nHasil dari pembagian {angka1} / {angka2} = {int(hasil)}")
#except:
#    print("Error: Kalkulator Gagal Dieksekusi1")

# Try dengan Except yang banyak
#print("=== Pembagian : Kalkulator Sederhana ===")
#try:
#    angka1 = int(input("Masukkan angka ke-1 : "))
#    angka2 = int(input("Masukkan angka ke-2 : "))
#    hasil = angka1/angka2
#    print(f"\nHasil dari pembagian {angka1} / {angka2} = {int(hasil)}")
#except ValueError:
#    print("Error: Masukkan angka yang valid!")
#except ZeroDivisionError:
#    print("Error: Pembagian oleh nol tidak diperbolehkan!")
#except:
#    print("Kalkulasi Gagal!")

# Try-Except-Else
#print("=== Melihat Bilangan ===")
#try:
#    angka = int(input("Masukkan angka : "))
#    print()
#except ValueError:
#    print("Error: Masukkan angka/bilangan!")
#else:
#    print(f"Angka yang kamu masukkan : {angka}")
#    if angka > 0:
#        print("Angka yang kamu masukkan : Bilangan Positif")
#    elif angka < 0:
#        print("Angka yang kamu masukkan : Bilangan Negatif")
#    else:
#        print("Angka yang kamu masukkan : Nol")

#Try-Except-Finally
print("=== Melihat Bilangan ===")
try:
    angka = int(input("Masukkan angka : "))
    print()
except ValueError:
    print("Error: Masukkan angka/bilangan!")
else:
    print(f"Angka yang kamu masukkan : {angka}")
    if angka > 0:
        print("Angka yang kamu masukkan : Bilangan Positif")
    elif angka < 0:
        print("Angka yang kamu masukkan : Bilangan Negatif")
    else:
        print("Angka yang kamu masukkan : Nol")
finally:
    print("Program selesai!\n")  # Output baris 1