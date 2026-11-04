# Naufal Ilham Fauzan
# 2502106
# matematika.py

def tambah(a, b):
    """Menambahkan 2 angka"""
    return a + b

def kurang(a, b):
    """Mengurangkan 2 angka"""
    return a - b

def kali(a, b):
    """Mengalikan 2 angka"""
    return a * b

def bagi(a, b):
    """Membagi 2 angka"""
    if b != 0:
        return a / b
    else:
        return "Tidak dapat dibagi oleh nol!"

def pangkat(a, b):
    """Menghitung pangkat dari 2 angka"""
    return a ** b

def modul(a, b):
    """Menghitung modulus dari 2 angka"""
    return a % b

# Variabel yang dapat digunakan
PI = 3.14159
NAMA_PEMBUAT = "Matematikawan Jago"

if __name__ == "__main__":
    print("File ini adalah modul, tidak bisa dijalankan secara langsung!")