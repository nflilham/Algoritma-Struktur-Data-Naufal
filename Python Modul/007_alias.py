# Naufal Ilham Fauzan
# 2502106

import matematika as math

if __name__ == "__main__":

    # Gunakan function dari module
    hasil1 = math.tambah(7, 7)
    hasil2 = math.kurang(7, 5)
    hasil3 = math.kali(5, 5)
    hasil4 = math.bagi(10, 2)

    print(f"Hasil Penjumlahan\t: {hasil1}")
    print(f"Hasil Pengurangan\t: {hasil2}")
    print(f"Hasil Perkalian\t\t: {hasil3}")
    print(f"Hasil Pembagian\t\t: {int(hasil4)}")

    # Gunakan variabel dari module
    print(f"\nPI\t\t: {math.PI}")
    print(f"NAMA PEMBUAT\t: {math.NAMA_PEMBUAT}")