# Naufal Ilham Fauzan
# 2502106
# Function
# 19 Oktober 2026

# Membuat fungsi
def nama_fungsi():
    print()
    print("Kalau fungsi ini dipanggil, ini akan muncul!")   # Output baris 1
    print("Ini akan muncul di baris kedua")                 # Output baris 2
    print("Ini akan muncul di baris ketiga")                # Output baris 3
    print()

# Memanggil fungsi
nama_fungsi()
nama_fungsi()
nama_fungsi()

# Function dengan parameter
def sapa_nama(nama):
    print(f"Halo, {nama}! Selamat datang di Python!")
    print(f"Senang bertemu denganmu!\n")

# Memanggil function dengan parameter
sapa_nama("Nopal")
sapa_nama("Gagan")
sapa_nama("Ajril")

# Luas Persegi
def luas_persegi(panjang, lebar):
    luas = panjang * lebar
    print(f"=== Luas persegi panjang ===\nLuas = Panjang x Lebar\nLuas = {panjang} x {lebar}\nLuas = {luas}\n")

# Memanggil Luas Persegi
luas_persegi(10, 5)
luas_persegi(20, 10)

# Luas Persegi dengan return value
def luas_persegi1(panjang, lebar):
    luas = panjang * lebar
    return luas
    print()

# Luas linigkaran
def luas_lingkaran(radius):
    pi = 3.14
    luas = pi * radius ** 2
    print(f"=== Luas lingkaran ===\nLuas = π x r²\nLuas = {pi} x {radius}²\nLuas = {luas}\n")

# Memanggil Luas Lingkaran
luas_lingkaran(5)
luas_lingkaran(7)

# Function dengan return value Luas Lingkaran
def luas_lingkaran1(radius):
    pi = 3.14
    luas = pi * radius ** 2
    return luas

luas1 = luas_lingkaran1(5)
luas2 = luas_lingkaran1(7)

print("=== Luas Lingkaran Return ===")
print(f"Luas lingkaran radius 5 : {luas1}")
print(f"Luas lingkaran radius 7 : {luas2}")
print(f"Jumlah Luas lingkaran 5 dan 7 : {luas1 + luas2}\n")

# Default Parameter
def sapa(nama, nim, sapaan = "Ohayo"):
    print(sapaan, nama, "Sebagai : ", nim)

sapa("Nopal", 2502106)               # Default Parameter
sapa("Gagan", 2500001, "Halo")       # Menguan Parameter Default sapaan
sapa("Ajriel", 2502107, "Halo")      # Mengubah Parameter Default sapaan dan sapaan2
print()

# Keyword Argument
def perkenalan(nama, umur, asal):
    print(f"Nama : {nama}")
    print(f"Umur : {umur} tahun")
    print(f"Asal : {asal}")
    print()


perkenalan("Naufal", 20, "Tanjungari")                  # Posision Argument
perkenalan(asal="Tanjungari", nama="Naufal", umur=20)   # Keywoard Argument

# Keyword Argument Lanjutan
def profil(nama, umur, nim, prodi="Pendidikan Multimedia", fakultas="FMIPA"):
    print(f"=== PROFIL {nama.upper()} ===")
    print(f"Nama\t: {nama}")
    print(f"Umur\t: {umur} tahun")
    print(f"NIM\t: {nim}")
    print(f"Prodi\t: {prodi}")
    print(f"Fakultas: {fakultas}")
    print()

profil("Naufal", 20, 2502106,)                                                                      # Posision Argument
profil("Dimas", 19, 2504444, prodi="Teknik Informatika", fakultas="Teknik")                         # Mengubah Prodi dan Fakultas
profil(fakultas="Kampus UPI di Cibiru", prodi="PGPAUD", nim=2507777, umur=19, nama="Jhuan Valent")  # Keywoard Argument

# Global Variable
# GAGAL
pi = 3.15

def luas_lingkaran2(radius):
    pi = 3.14
    luas = pi * (radius ** 2)
    print(f"Luas Lingkaran: {luas}")

luas_lingkaran2(10)
luas_lingkaran2(15)
luas_lingkaran2(20)
print()

# Parameter Dinamis
def mylist(x, y):
    return x * y
   
mylist(5, 5)

# ==================

def yourlist(*list):
    for item in list:
        print(item)
        
yourlist(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print()

# ==================

def ourlist(**dict):
    for key, value in dict.items():
        print(f"{key}\t: {value}")
    print()

ourlist(nama="Naufal", nim="2502106", umur=20)


# ==================
# Kang Zidan
# ==================

def listfunc(*list):
    return list

print(listfunc(1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
print(type(listfunc()))

def tambahnilai(*list):
    x = 0
    for angka in list:
        x += angka 
    return x

print(tambahnilai(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print()

def deteksi_makanan(**dict):
    if "makanan" in dict:
        return f"Nama saya {dict["nama"]}, makanan kesukaan saya adalah {dict["makanan"]}"
    else:
        return f"Nama saya {dict["nama"]}, saya tidak memiliki makanan kesukaan"

print(deteksi_makanan(nama="Labib", makanan="cireng"))  # Punya makanan
print(deteksi_makanan(nama="Gagan"))                    # Tidak punya makanan

def gabungan(*list, **dict):
    print(list)
    print(dict)

print(gabungan(1, 2, 3, 4, 5, nomor="tujuh"))
print()

# Map and Filter
negara = ["Indonesia", "Malaysia", "Singapura", "Thailand", "Brunei"]

def str(x):
    return type(x) == str

print(list(filter(str, negara)))
print()

# Map
angka = [1, 2, 3, 4, 5]

hasil = list(map(lambda x : x * 2, angka))  # Mempersingkan list dengan lambda function
print(hasil)                                # [2, 4, 6, 8, 10]

# Filter
angka = [1, 2, 3, 4, 5]

hasil = list(filter(lambda x : x % 2 == 0, angka))  # Mempersingkan list dengan lambda function
print(hasil)                                        # [2, 4]