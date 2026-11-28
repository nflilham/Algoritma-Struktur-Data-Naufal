# Naufal Ilham Fauzan
# 2502106
# Tugas 14 | Soal 1

# Soal 1: Buat fungsi untuk mengambil elemen pertama list dan jelaskan mengapa kompleksitasnya O(1).

def ambil_pertama(data):
    # cek apakah list kosong agar tidak muncul IndexError saat akses indeks 0
    if not data:
        return None
    # langsung ambil elemen pada indeks ke-0
    return data[0]

# contoh penggunaan dengan list berisi angka dan list kosong
angka = [10, 20, 30, 40]
kosong = []

print(f"List angka\t: {angka}")
print(f"Elemen awal\t: {ambil_pertama(angka)}")
print(f"List kosong\t: {ambil_pertama(kosong)}")

# Penjelasan:
# Kompleksitasnya O(1) karena fungsi langsung mengakses indeks ke-0 (data[0]). List di Python menyimpan referensi elemen secara berurutan di memori, jadi program bisa langsung menuju posisi pertama tanpa menelusuri isi list. Berapapun panjang list, waktu eksekusinya tetap konstan.

# Penjelasan output:
# Pada list [10, 20, 30, 40], program mencetak elemen pertama yaitu 10.
# Pada list kosong [], fungsi mengembalikan None sebagai penanda tidak ada data.