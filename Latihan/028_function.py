def halo():
    print("Halo bang!")

# Memanggil function
halo()
halo()
halo()
print()

# Function dengan parameter
def sapa_nama(nama, asal):
    print("Halo", nama)
    print("Kamu dari", asal, "ya")

sapa_nama("opal", "Tanjungsari")
sapa_nama("gagan", "Cilembu")
sapa_nama("ajril", "Ciwidey")
print()

# Function dengan return Value
def luas_lingkaran(radius):
    pi = 3.14
    luas = pi *  radius * radius
    return luas

luas1 = luas_lingkaran(5)
print(luas1)
print()

# Default Parameter
def sapaan(nama, say = "Hello"):
    print(say, nama)

sapaan("nopal")
sapaan("nopal", "hi")
sapaan("nopal", "adios")
print()

# Keyword argument
def perkenalan(nama, umur, kota):
    print("Nama :", nama)
    print("Umur :", umur, "tahun")
    print("Kota :", kota)

perkenalan("Naufal", 31, "Norway\n")
perkenalan(kota="Majalaya", nama="Piwpiw", umur=100)
print()

def buat_profil(nama, umur, kota ="Sumedang", pekerjaan="Mahasiswa"):
    print(f"=== PROFIL {nama.upper()} ===")
    print(f"Umur\t\t: {umur} tahun")
    print(f"Kota\t\t: {kota}")
    print(f"Pekerjaan\t: {pekerjaan}")
    print()

buat_profil("Nopal", 20)
buat_profil("Ajriel", 19)
buat_profil("Ghaniar", 77)
print()

# Local variabel
def test():
    x = 10
    print("Nilai x = ", x)

test()
print()

# Global variabel
nama_global = "Alice"

def tampilkan_nama():
    print("Nama : ", nama_global)

def ubah_nama():
    global nama_global
    nama_global = "Balmond"

tampilkan_nama()
ubah_nama()
tampilkan_nama()
print()

# Parameter dinamis
def cetak_list(*list):
    for item in list:
        print(item)

cetak_list(1, 2, 3, 4, 5)

def cetak_dict(**dict):
    for key, value in dict.items():
        print(f"{key}: {value}")

cetak_dict(nama="Nopal", umur=20, kota="Sumedang")