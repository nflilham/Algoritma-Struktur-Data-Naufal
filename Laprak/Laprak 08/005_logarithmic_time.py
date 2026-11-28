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

angka = [4, 9, 16, 22, 34, 38, 46, 57, 68, 80]
target = 46

hasil_ada = binary_search(angka, target)
print(f"Angka {target} ditemukan di indeks ke: {hasil_ada}")