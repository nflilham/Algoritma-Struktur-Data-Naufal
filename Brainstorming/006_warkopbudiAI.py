# =========================================================
# Tugas Studi Kasus - Pertemuan 1: Pengenalan Python
# Judul: "Warung Kopi Pak Budi" (Versi LOOPING)
# =========================================================
# Versi ini memakai while agar pembeli bisa pesan LEBIH DARI
# SATU menu dalam satu transaksi, sebelum akhirnya bayar.

# 1. Menampilkan nama warung dan pesan sambutan
nama_warung = "Warung Kopi Pak Budi"   # string
print("==============================")
print(nama_warung.center(30))
print("==============================")
print("Selamat datang! Silakan pesan menu favoritmu.\n")

nama_pembeli = input("Masukkan nama Anda\t: ")   # string
print(f"\nHalo, {nama_pembeli}! Berikut daftar menu kami:")
print("1. Kopi Hitam  - Rp8.000")
print("2. Kopi Susu   - Rp12.000")
print("3. Es Teh      - Rp6.000")
print("4. Gula Aren   - Rp15.000\n")

# Variabel penampung total belanja, dimulai dari 0
total_harga = 0.0          # float, akan terus bertambah tiap pesanan
daftar_pesanan = []        # list, untuk menyimpan rincian pesanan (buat struk nanti)

# -------------------------------------------------------
# LOOP UTAMA: berulang selama pembeli masih mau pesan
# -------------------------------------------------------
# "while True" artinya loop ini akan berjalan TERUS MENERUS,
# dan hanya berhenti kalau di dalamnya ada perintah "break".
while True:
    nama_menu = input("Menu yang dipesan (atau ketik 'selesai')\t: ")

    # Ini syarat untuk KELUAR dari loop
    if nama_menu.lower() == "selesai":
        print("\nBaik, pesanan diakhiri. Lanjut ke pembayaran...\n")
        break   # <- perintah ini yang menghentikan while

    # Menentukan harga satuan sesuai menu yang diketik
    if nama_menu.lower() == "kopi hitam":
        harga_satuan = 8000.0
    elif nama_menu.lower() == "kopi susu":
        harga_satuan = 12000.0
    elif nama_menu.lower() == "es teh":
        harga_satuan = 6000.0
    elif nama_menu.lower() == "gula aren":
        harga_satuan = 15000.0
    else:
        print("Menu tidak dikenali, coba tulis ulang ya.\n")
        continue   # <- lompat ke awal loop lagi, tanpa minta jumlah

    jumlah_pesanan = int(input("Jumlah pesanan\t\t: "))  # integer

    # Menghitung subtotal untuk pesanan menu ini
    subtotal = harga_satuan * jumlah_pesanan
    total_harga = total_harga + subtotal   # ditambahkan ke total keseluruhan

    # Menyimpan rincian pesanan ini ke dalam list, untuk dicetak nanti
    daftar_pesanan.append(f"{nama_menu} x{jumlah_pesanan} = Rp{subtotal:,.0f}")

    print(f"-> Ditambahkan: {nama_menu} x{jumlah_pesanan} (Rp{subtotal:,.0f})\n")
# -------------------------------------------------------
# Loop berhenti di sini setelah pembeli mengetik "selesai"
# -------------------------------------------------------

# 5. Meminta input uang yang dibayarkan, lalu menghitung kembalian
uang_bayar = float(input(f"Total belanja Rp{total_harga:,.0f}\nUang dibayarkan\t: Rp"))
kembalian = uang_bayar - total_harga

# 6. Menampilkan struk sederhana
print("\n==============================")
print("            STRUK             ")
print("==============================")
print(f"Nama\t\t: {nama_pembeli}")
print("Rincian pesanan:")

# Loop kedua: mencetak setiap item di daftar_pesanan satu per satu
for item in daftar_pesanan:
    print(f"  - {item}")

print("------------------------------")
print(f"Total Harga\t: Rp{total_harga:,.0f}")
print(f"Uang Dibayar\t: Rp{uang_bayar:,.0f}")
print(f"Kembalian\t: Rp{kembalian:,.0f}")
print("==============================")
print("     Terima kasih & datang lagi!     ")
print("==============================")


# =========================================================
# SOAL REFLEKSI
# =========================================================
# 1. Tipe data apa saja yang kamu gunakan dan kenapa?
#    String untuk nama_warung, nama_pembeli, dan nama_menu karena
#    berupa teks. Integer untuk jumlah_pesanan karena jumlah barang
#    selalu bilangan bulat. Float untuk harga_satuan, subtotal,
#    total_harga, uang_bayar, dan kembalian karena berkaitan dengan
#    nominal uang. List (daftar_pesanan) dipakai untuk menyimpan
#    banyak rincian pesanan sekaligus, karena jumlah pesanan bisa
#    berubah-ubah tergantung berapa kali loop berjalan.
#
# 2. Bagian mana yang paling sulit dipahami saat mengerjakan?
#    Bagian tersulit adalah memahami kapan loop harus berhenti (pakai
#    break) dan kapan loop harus melompat ke pengulangan berikutnya
#    tanpa menyelesaikan sisa kode di bawahnya (pakai continue),
#    misalnya saat menu yang diketik tidak dikenali.
#
# 3. Perbedaan int(), float(), dan str() menurut kata-kata sendiri:
#    - int() mengubah nilai menjadi bilangan bulat, dipakai untuk
#      hal yang tidak mungkin pecahan, seperti jumlah pesanan.
#    - float() mengubah nilai menjadi bilangan desimal, dipakai untuk
#      nilai uang yang bisa punya angka di belakang koma.
#    - str() mengubah nilai menjadi teks, supaya angka bisa digabung
#      dan ditampilkan bersama kalimat lain saat dicetak.