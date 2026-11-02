print("==============================")
print("           INSTAGRAM          ")
print("==============================\n")

username = input("Username : ")

if username == "admin":
    password = input("Password : ")
    if password == "admin123":
        print("Anda berhasil Login!\nSelamat datang di Instagram!")
    else:
        print("Password yang anda masukkan salah!")
else:
    print("\nUsername tidak ditemukan!")
    print("==============================")