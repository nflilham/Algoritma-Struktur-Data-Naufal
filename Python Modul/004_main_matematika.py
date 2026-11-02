# Naufal Ilham Fauzan
# 2502106

import matematika

if __name__ == "__main__":

    # Gunakan function dari module
    hasil1 = matematika.tambah(7, 7)
    hasil2 = matematika.kurang(7, 5)
    hasil3 = matematika.kali(5, 5)
    hasil4 = matematika.bagi(10, 2)

    print(f"Hasil Penjumlahan\t: {hasil1}")
    print(f"Hasil Pengurangan\t: {hasil2}")
    print(f"Hasil Perkalian\t\t: {hasil3}")
    print(f"Hasil Pembagian\t\t: {int(hasil4)}")

    # Gunakan variabel dari module
    print(f"\nPI\t\t: {matematika.PI}")
    print(f"NAMA PEMBUAT\t: {matematika.NAMA_PEMBUAT}")