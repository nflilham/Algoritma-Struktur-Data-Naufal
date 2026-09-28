angka_rahasia = 9

while True:
    tebakan = int(input("\nTebak angka (1-10) : "))

    if tebakan == angka_rahasia:
        print("Tebakan anda Benar!\n")
        break

    else:
        print("Tebakan anda Salah! Coba lagi")