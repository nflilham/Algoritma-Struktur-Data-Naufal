ya = {"ya", "iya", "mulai", "gas"}
tidak = {"keluar", "quit", "tidak", "nggak", "gak", "ga", "ngga", "nggk", "gk"}


def hitung(angka_kiri, operator, angka_kanan):
    if operator == "+":
        return angka_kiri + angka_kanan
    elif operator == "-":
        return angka_kiri - angka_kanan
    elif operator == "*":
        return angka_kiri * angka_kanan
    elif operator == "/":
        return angka_kiri / angka_kanan
    else:
        raise ValueError("Operator tidak valid.")


while True:
    mulai = input("Jalankan kalkulator? (ya/tidak) : ").strip().lower()

    if mulai in tidak:
        print("Kalkulator dihentikan.")
        break
    elif mulai not in ya:
        print("Jawaban tidak dikenali. Masukkan ya atau tidak.\n")
        continue

    print("==============================")
    print("     KALKULATOR SEDERHANA     ")
    print("==============================")

    try:
        angka1 = float(input("Masukkan angka pertama : "))
        operator1 = input("Masukkan operator (+, -, *, /) : ").strip()
        angka2 = float(input("Masukkan angka kedua : "))
        operator2 = input("Masukkan operator (+, -, *, /) : ").strip()
        angka3 = float(input("Masukkan angka ketiga : "))
    except ValueError:
        print("Input angka tidak valid. Masukkan angka, misalnya 5 atau 2.5.")
        print()
        continue

    if operator1 not in {"+", "-", "*", "/"} or operator2 not in {"+", "-", "*", "/"}:
        print("Operator tidak valid. Gunakan +, -, *, atau /.")
    else:
        try:
            if operator1 in {"*", "/"}:
                hasil = hitung(hitung(angka1, operator1, angka2), operator2, angka3)
            elif operator2 in {"*", "/"}:
                hasil = hitung(angka1, operator1, hitung(angka2, operator2, angka3))
            else:
                hasil = hitung(hitung(angka1, operator1, angka2), operator2, angka3)
            print("Hasil:", hasil)
        except ZeroDivisionError:
            print("Tidak bisa membagi dengan nol.")

    print()
