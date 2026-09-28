#Menecetak angka 1 - 5
angka = 1
while angka <= 3:
    print(angka)
    angka += 1

#Password
print("====================================")
password = ""
while password != "123456":
    password = input("Masukkan Password : ")
    if password != "123456":
        print("Password yang anda masukkan salah!\n")
print("Password benar!")
print("====================================")