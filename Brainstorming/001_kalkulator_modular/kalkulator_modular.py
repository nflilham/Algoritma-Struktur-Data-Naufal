# Naufal Ilham Fauzan
# 2502106
# Kalkulator Modular | Kelompok 2
# kalkulator-modular.py

def tambah(a, b):
    """Berfungsi untuk menjumlahkan duan bilangan"""
    return a + b

def kurang(a, b):
    """Berfugnsi untuk mengurangkan dua bilangan"""
    return a - b

def kali(a, b):
    """Berfungsi untuk mengurangkan dua bilangan"""
    return a * b

def bagi(a, b):
    """berfungsi untuk membagi dua bilangan"""
    if b != 0:
        return a / b
    else:
        print("Tidak bisa membagi dengan angka 0!")

def pangkat(a, b):
    """Berfungsi untuk mempangkatkan dua bilangan"""
    return a ** b

def modulus(a, b):
    """Berfungsi untuk menghitung sisa bagi dua bilangan"""
    return a % b

if __name__ == "__main__":
    print("File ini adalah module")
