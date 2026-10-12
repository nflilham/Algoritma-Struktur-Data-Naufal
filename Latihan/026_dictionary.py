# Naufal Ilham Fauzan
# 2502106

siswa = {
    "Nama" : "nopalajaib",
    "NIM" : "2502106",
    "Umur" : 20
}

print(siswa)
print()

print(siswa["Nama"])    # nopalajaib
print(siswa["NIM"])     # 2502106
print(siswa["Umur"])    # 20

# Mengubah nilai 
# del siswa["Umur"]
print(siswa)
print()

# Menggunakan iterasi
for key in siswa:
    print(key, ":", siswa[key])
print()

# Menggunakan pairs() untuk iterasi
for key, value in siswa.items():
    print(key, "=", value)