ya = {"ya", "iya", "mulai", "gas"}
tidak = {"keluar", "quit", "tidak", "nggak", "gak", "ga", "ngga", "nggk", "gk"}

while True:
    mulai = input("Jalankan kalkulator? (ya/tidak) : ").lower()

    if mulai in tidak:
        print("Kalkulator dihentikan!")
        break
    elif mulai not in ya:
        print("Inputan tidak valid! coba lagi")
        continue

    print("==============================")
    print("     KALKULATOR SEDERHANA     ")
    print("==============================")

    angka1 = float(input("Masukkan angka pertama : "))
    operator1 = input("Masukkan operator (+, -, *, /) : ")
    angka2 = float(input("Masukkan angka kedua : "))
    operator2 = input("Masukkan operator (+, -, *, /) : ")
    angka3 = float(input("Masukkan angka ketiga : "))

    if operator1 == "+":
        if operator2 == "+":
            hasil = angka1 + angka2 + angka3
        elif operator2 == "-":
            hasil = angka1 + angka2 - angka3
        elif operator2 == "*":
            hasil = angka1 + (angka2 * angka3)
        elif operator2 == "/":
            hasil = angka1 + (angka2 / angka3)

    elif operator1 == "-":
        if operator2 == "+":
            hasil = angka1 - angka2 + angka3
        elif operator2 == "-":
            hasil = angka1 - angka2 - angka3
        elif operator2 == "*":
            hasil = angka1 - (angka2 * angka3)
        elif operator2 == "/":
            hasil = angka1 - (angka2 / angka3)

    elif operator1 == "*":
        if operator2 == "+":
            hasil = (angka1 * angka2) + angka3
        elif operator2 == "-":
            hasil = (angka1 * angka2) - angka3
        elif operator2 == "*":
            hasil = (angka1 * angka2) * angka3
        elif operator2 == "/":
            hasil = (angka1 * angka2) / angka3

    elif angka1 or angka2 or angka3 != 0:
        if operator1 == "/":
            if operator2 == "+":
               hasil = angka1 / angka2 + angka3
            elif operator2 == "-":
                hasil = angka1 / angka2 - angka3
            elif operator2 == "*":
                hasil = (angka1 / angka2) * angka3
            elif operator2 == "/":
                hasil = (angka1 / angka2) / angka3
        
    else:
        print("Operator tidak valid, silahkan ulangi!")

    print(f"Hasil dari kalkulatormu adalah : {hasil}")
    break