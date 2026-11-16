# Naufal Ilham Fauzan
# 2502106
# Kalkulator Modular | Kelompok 2
# main.py

from kalkulator_modular import *

if __name__ == "__main__":

    print("=== KALKULATOR SEDERHANA ===\n")

    while True:

        mulai = input("Mulai kalkulator? [y/n] : ")

        if mulai.lower() == "n":
            print("Terima kasih telah menggunakan kalkulator!")
            break
        elif mulai.lower() == "y":
            print("Kalkulator siap digunakan!\n")
        else:
            print("Input tidak valid! Harap masukkan 'y' atau 'n'.\n")
            continue

        try:
            a = float(input("Masukkan angka pertama: "))
            operator = input("Masukkan operator [+ / - / * / (/) / ^ / %] : ")
            b = float(input("Masukkan angka kedua : "))
            print()
        except ValueError:
            print("Input tidak valid! Harap masukkan angka yang benar.\n")
            continue

        if operator == "+":
            print(f"hasil dari {a} + {b} = {tambah(a, b)}")

        elif operator == "-":
            print(f"hasil dari {a} - {b} = {kurang(a, b)}")

        elif operator == "*":
            print(f"hasil dari {a} X {b} = {kali(a, b)}")

        elif operator == "/":
            print(f"hasil dari {a} / {b} = {bagi(a, b)}")

        elif operator == "^":
            print(f"hasil dari {a} ^ {b} = {pangkat(a, b)}")

        elif operator == "%":
            print(f"hasil dari {a} % {b} = {modulus(a, b)}")

        else:
            print("Operator yang anda masukkan tidak valid!")
            continue
