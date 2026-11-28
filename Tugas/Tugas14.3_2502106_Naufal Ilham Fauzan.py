# Naufal Ilham Fauzan
# 2502106
# Tugas 14 | Soal 3

# Soal 3: Buat program menampilkan semua pasangan angka menggunakan nested loop, uji n = 5 dan n = 10.

def tampilkan_pasangan(n):
    # pastikan nilai n positif sebelum menjalankan perulangan
    if n <= 0:
        print("Nilai n harus lebih dari 0.")
        return

    jumlah_pasangan = 0
    print(f"Pasangan angka untuk n = {n}:")

    # loop luar menentukan angka pertama (i) dari 1 sampai n
    for i in range(1, n + 1):
        # loop dalam menentukan angka kedua (j) dari 1 sampai n untuk tiap i
        for j in range(1, n + 1):
            print(f"({i}, {j})", end=" ")
            jumlah_pasangan += 1
        # pindah baris setiap satu nilai i selesai dipasangkan
        print()

    print(f"Total pasangan: {jumlah_pasangan}\n")

# uji program untuk n = 5 dan n = 10
tampilkan_pasangan(5)
tampilkan_pasangan(10)

# Penjelasan:
# Untuk setiap 1 langkah di loop luar (n kali), loop dalam berjalan penuh sebanyak n kali juga. Total eksekusinya adalah n x n = n^2, sehingga kompleksitas waktunya adalah O(n^2).

# Penjelasan output:
# Pengujian n = 5 mencetak 5 x 5 = 25 pasangan dari (1, 1) hingga (5, 5).
# Pengujian n = 10 mencetak 10 x 10 = 100 pasangan dari (1, 1) hingga (10, 10).
