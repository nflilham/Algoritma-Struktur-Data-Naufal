# Naufal Ilham Fauzan
# 2502106
# Tugas 14 | Soal 2

# Soal 2: Buat fungsi menghitung total isi list tanpa sum() dan tentukan Big-O.

def hitung_total(data):
    # siapkan variabel penampung total mulai dari 0
    total = 0
    # telusuri setiap angka di dalam list satu per satu
    for angka in data:
        # tambahkan nilai angka saat ini ke variabel total
        total += angka
    # kembalikan hasil akhir penjumlahan
    return total

# contoh penggunaan dengan list berisi data dan list kosong
nilai = [5, 10, 15, 20, 25]
kosong = []

print(f"List nilai\t: {nilai}")
print(f"Total\t\t: {hitung_total(nilai)}")
print(f"Total kosong\t: {hitung_total(kosong)}")

# Penjelasan:
# Time Complexity: O(n), karena perulangan for membaca dan menjumlahkan setiap elemen satu kali mengikuti panjang list (n).
# Space Complexity: O(1), karena hanya memakai satu variabel tambahan (total)yang ukurannya tidak bergantung pada panjang list.

# Penjelasan output:
# Total dari [5, 10, 15, 20, 25] adalah 75, sedangkan list kosong menghasilkan 0.