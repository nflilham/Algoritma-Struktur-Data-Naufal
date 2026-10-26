# Naufal Ilham Fauzan
# 2502106

print("======== TEBAK ANGKA ========\n")

import random
kesempatan = 3
pilihan = random.randint(1, 20)

while kesempatan > 0:
    print(f"Sisa kesempatan = {kesempatan}x lagi!")

    try:
        tebakan = int(input("Masukkan angka pilihan : "))
        if tebakan == pilihan:
            print(f"Tebakanmu benar! ({pilihan})")
        elif tebakan > pilihan:
            print("Terlalu tinggi!")
        else:
            print("Terlalu rendah!")
    except ValueError:
        print("Masukkan angka/bilangan yang valid!")
        kesempatan += 1
    print()
    
    kesempatan -= 1

else:
    print(f"Kesempatanmu habis!\nAngka yang benar adalah {pilihan}\n\n======== SELESAI ========")