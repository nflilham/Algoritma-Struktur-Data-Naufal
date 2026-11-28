# Naufal Ilham Fauzan
# 2502106
# Tugas 14 | Soal 5

# Soal 5: Buktikan bahwa 4n^2 + 3n + 8 termasuk O(n^2) dengan menentukan c dan n0.

# Pembuktian Matematis:
# Definisi Big-O: f(n) termasuk O(g(n)) jika ada konstanta c > 0 dan n0 >= 1 sehingga berlaku f(n) <= c * g(n) untuk semua n >= n0.

# Diketahui:
# f(n) = 4n^2 + 3n + 8
# g(n) = n^2

# Untuk setiap n >= 1, berlaku:
# 3n <= 3n^2   (karena n <= n^2)
# 8  <= 8n^2   (karena 1 <= n^2)

# Jumlahkan seluruh suku:
# 4n^2 + 3n + 8 <= 4n^2 + 3n^2 + 8n^2
# 4n^2 + 3n + 8 <= 15n^2

# Jadi, dapat dipilih konstanta c = 15 dan n0 = 1.

def cek_big_o(c, n0, batas_uji):
    # uji pertidaksamaan f(n) <= c * n^2 untuk n dari n0 sampai batas_uji
    semua_valid = True
    for n in range(n0, batas_uji + 1):
        f_n = 4 * (n ** 2) + 3 * n + 8
        batas_atas = c * (n ** 2)
        if f_n > batas_atas:
            semua_valid = False
            break
    return semua_valid

c = 15
n0 = 1

print(f"Konstanta: c = {c}, n0 = {n0}")
print(f"Terbukti untuk n = 1..100: {cek_big_o(c, n0, 100)}")

# cetak beberapa sampel nilai n untuk melihat perbandingannya secara langsung
for n in [1, 2, 5, 10]:
    f_n = 4 * (n ** 2) + 3 * n + 8
    batas_atas = c * (n ** 2)
    print(f"n = {n:2d} -> f(n) = {f_n:4d} <= {c}*n^2 = {batas_atas:4d} ({f_n <= batas_atas})")

# Penjelasan:
# Karena pertidaksamaan 4n^2 + 3n + 8 <= 15n^2 selalu benar untuk setiap n >= 1, syarat definisi Big-O terpenuhi dengan c = 15 dan n0 = 1.

# Penjelasan output:
# Program memverifikasi n = 1 sampai 100 dan mengembalikan True, lalu menampilkan perbandingan angka konkret untuk n = 1, 2, 5, dan 10.