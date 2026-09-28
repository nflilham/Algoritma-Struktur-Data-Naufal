print("==============================")
print("           INSTAGRAM          ")
print("==============================\n")

username = input("Username : ")

if username == "admin":
    password = input("Password : ")
    print("\n")
    if password == "admin123":
        print("Anda berhasil Login!\nSelamat datang di Instagram!")
        print("==============================")
    else:
        print("Password yang anda masukkan salah!")
        print("==============================")
else:
    print("\nUsername tidak ditemukan!")
    print("==============================")