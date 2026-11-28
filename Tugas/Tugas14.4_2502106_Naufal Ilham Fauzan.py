# Naufal Ilham Fauzan
# 2502106
# Tugas 14 | Soal 4

# Soal 4: Implementasikan Linear Search dan Binary Search, lalu bandingkan jumlah pemeriksaannya.

def linear_search(data, target):
    # hitung berapa kali elemen list diperiksa
    pemeriksaan = 0
    # cek elemen secara berurutan dari indeks 0 sampai akhir
    for indeks, nilai in enumerate(data):
        pemeriksaan += 1
        # jika cocok, kembalikan posisi indeks dan jumlah pemeriksaan
        if nilai == target:
            return indeks, pemeriksaan
    # kembalikan -1 jika target tidak ditemukan
    return -1, pemeriksaan

def binary_search(data, target):
    # atur batas awal pencarian dari indeks paling kiri dan paling kanan
    kiri = 0
    kanan = len(data) - 1
    pemeriksaan = 0

    # ulangi selama rentang pencarian masih valid
    while kiri <= kanan:
        # ambil indeks tengah dari rentang saat ini
        tengah = (kiri + kanan) // 2
        pemeriksaan += 1

        # jika elemen tengah sama dengan target, pencarian selesai
        if data[tengah] == target:
            return tengah, pemeriksaan
        # jika target lebih besar, geser batas kiri ke kanan tengah
        elif data[tengah] < target:
            kiri = tengah + 1
        # jika target lebih kecil, geser batas kanan ke kiri tengah
        else:
            kanan = tengah - 1

    # kembalikan -1 jika target tidak ada di dalam list
    return -1, pemeriksaan

# uji pada list terurut berisi angka 1 sampai 100
data_urut = list(range(1, 101))

for target in [88, 200]:
    idx_lin, cek_lin = linear_search(data_urut, target)
    idx_bin, cek_bin = binary_search(data_urut, target)

    print(f"Cari target = {target} pada data 1..100:")
    print(f"Linear Search\t-> indeks: {idx_lin}, pemeriksaan: {cek_lin}x")
    print(f"Binary Search\t-> indeks: {idx_bin}, pemeriksaan: {cek_bin}x\n")

# Penjelasan:
# Linear Search mengecek elemen satu per satu dari awal, sehingga pada kasus terburuk perlu n pemeriksaan -> O(n).
# Binary Search bekerja pada data terurut dan membuang setengah ruang pencarian setiap langkah, sehingga jauh lebih sedikit -> O(log n).

# Penjelasan output:
# Saat mencari 88, Linear Search memeriksa 88 kali, sedangkan Binary Search hanya 3 kali. Saat mencari 200 (tidak ada), Linear Search memeriksa 100 kali sedangkan Binary Search hanya 7 kali.