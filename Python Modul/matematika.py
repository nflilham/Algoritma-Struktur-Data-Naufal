# Naufal Ilham Fauzan
# 2502106
# Python modul - 003
# matematika.py

def tambah(a, b):
    """Menamahkan dua angka"""
    return a + b

def kurang(a, b):
    """Mengurangkan dua angka"""
    return a - b

def kali(a, b):
    """Mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Membagi dua angka"""
    if b != 0:
        return a / b
    else:
        return "Tidak dapat dibagi oleh nol!"

def pangkat(a, b):
    """Menghitung pangkat dari dua angka"""
    return a ** b

def modul(a, b):
    """Menghitung modulus dari dua angka"""
    return a % b

# Variabel yang dapat digunakan
PI = 3.14159
NAMA_PEMBUAT = "Matematikawan Jago"

if __name__ == "__main__":
    print("Program ini tidak bisa dijalankan sebagai modul!")