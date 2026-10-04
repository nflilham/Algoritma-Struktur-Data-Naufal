ya = {"ya", "iya", "punya", "lulus", "lolos", "mau"}
tidak = {"tidak", "nggak", "gak", "ga", "ngga", "nggk", "gk"}

nama = input("Masukkan nama : ")
umur = int(input("Masukkan umur : "))

while True:
    if umur > 17:
        instagram = input(f"Halo {nama}, mau membuat akun instagram? (ya/tidak) :").lower()
        if instagram in ya:
            username = input("Masukkan username : ")
            password = input("Masukkan password : ")
            print(f"Selamat {nama}, akun instagrammu berhasil dibuat dengan username {username} dan password {password}.")
            break

        elif instagram in tidak:
            print(f"Baik {nama}, akun instagram tidak jadi dibuat.")
            break

        else:
            print("Input tidak valid. Silakan jawab dengan 'ya' atau 'tidak'.")
            continue

    elif umur < 17:
        instagram_kids = input(f"Halo {nama}, mau bikin akun instagram for kids? (ya/tidak) :").lower()
        if instagram_kids in ya:
            username = input("Masukkan username : ")
            password = input("Masukkan password : ")
            print(f"Selamat {nama}, akun instagram for kids berhasil dibuat dengan username {username} dan password {password}.")
            break

        elif instagram_kids in tidak:
            print(f"Baik {nama}, akun instagram for kidstidak jadi dibuat.")
            break

        else:
            print("Input tidak valid. Silakan jawab dengan 'ya' atau 'tidak'.")
            continue

    else:
        print("Umur tidak valid. Silakan masukkan umur yang benar.")
        continue