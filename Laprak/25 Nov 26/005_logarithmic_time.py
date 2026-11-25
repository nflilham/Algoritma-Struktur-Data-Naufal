def binary_search(data, target):
    kiri, kanan = 0, len(data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah] == target:
            return tengah
        elif data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1

angka = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91, 100, 123, 125, 122, 111, 123]

hasil_ada = binary_search(angka, int(input("Masukkan angka: ")))
print(f"Angka {hasil_ada} ditemukan di indeks ke: {hasil_ada}")
