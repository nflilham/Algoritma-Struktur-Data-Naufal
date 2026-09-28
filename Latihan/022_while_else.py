# Password benar dengan batas percobaan
password_benar = "admin123"
percobaan = 0
max_percobaan = 3

print("\n")
while percobaan < max_percobaan:
    password = input("Masukkan Password\t: ")
    percobaan += 1

    if password == password_benar:
        print("Login Berhasil!\n")
        break
    else:
        print("Password salah! Sisa percobaan anda sebanyak", max_percobaan - percobaan, "kali")
else:
    print("Sisa percobaan telah habis, silahkan coba lagi nanti!")