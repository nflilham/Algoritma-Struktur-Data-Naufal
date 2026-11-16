# Naufal Ilham Fauzan
# 2502106
# Kalkulator Modular | Kelompok 2
# main.py

from decimal import Decimal, InvalidOperation
from kalkulator_modular import *


def input_angka(pesan: str) -> Decimal:
    """Meminta input angka bertipe Decimal hingga valid."""
    # Ulangi input angka jika terjadi InvalidOperation tanpa kembali ke menu awal
    while True:
        try:
            return Decimal(input(pesan))
        except InvalidOperation:
            print("Input tidak valid! Harap masukkan angka yang benar.\n")


if __name__ == "__main__":

    # Memetakan simbol operator ke masing-masing fungsi operasi dalam 1 dictionary
    operasi = {
        "+": tambah,
        "-": kurang,
        "*": kali,
        "/": bagi,
        "^": pangkat,
        "%": modulus,
    }

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

        a = input_angka("Masukkan angka pertama: ")

        # Loop khusus operator agar input salah langsung mengulang ke operator
        while True:
            operator = input("Masukkan operator [+ / - / * / (/) / ^ / %] : ")
            if operator in operasi:
                break
            print("Operator yang anda masukkan tidak valid!\n")

        b = input_angka("Masukkan angka kedua : ")
        print()

        # Panggil fungsi operasi dari dictionary berdasarkan operator yang sudah valid
        print(f"hasil dari {a} {operator} {b} = {operasi[operator](a, b)}")
