# Try-Except-Finally
try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input tidak valid!")
finally:
    print("Program selesai dijalankan")