# ============================================================
#   ☕  WARKOP BUDI - Sistem Pemesanan
# ============================================================

# --- Data Menu ---
menu_makan = {
    1:  {"nama": "Nasi Goreng Spesial", "harga": 15000},
    2:  {"nama": "Mie Goreng Jawa",     "harga": 13000},
    3:  {"nama": "Ayam Bakar",           "harga": 18000},
    4:  {"nama": "Nasi Uduk + Lauk",     "harga": 14000},
    5:  {"nama": "Lontong Sayur",        "harga": 12000},
}

menu_minum = {
    6:  {"nama": "Kopi Hitam",           "harga": 5000},
    7:  {"nama": "Kopi Susu",            "harga": 8000},
    8:  {"nama": "Teh Manis",            "harga": 4000},
    9:  {"nama": "Es Jeruk",             "harga": 6000},
    10: {"nama": "Jus Alpukat",          "harga": 10000},
}

menu_dessert = {
    11: {"nama": "Es Krim Coklat",       "harga": 9000},
    12: {"nama": "Puding Susu",          "harga": 7000},
    13: {"nama": "Pisang Goreng Keju",   "harga": 8000},
    14: {"nama": "Roti Bakar Selai",     "harga": 6000},
    15: {"nama": "Bubur Kacang Hijau",   "harga": 5000},
}

# Gabungkan semua menu
semua_menu = {**menu_makan, **menu_minum, **menu_dessert}

# Daftar pesanan: {nomor_menu: jumlah}
pesanan = {}


# ============================================================
# FUNGSI HELPER
# ============================================================

def tampilkan_menu():
    print("\n" + "=" * 45)
    print("        ☕  WARKOP BUDI - DAFTAR MENU")
    print("=" * 45)

    print("\n🍽️  MAKANAN")
    print("-" * 45)
    for no, item in menu_makan.items():
        print(f"  [{no:2}] {item['nama']:<25} Rp {item['harga']:>7,}")

    print("\n🥤  MINUMAN")
    print("-" * 45)
    for no, item in menu_minum.items():
        print(f"  [{no:2}] {item['nama']:<25} Rp {item['harga']:>7,}")

    print("\n🍮  DESSERT")
    print("-" * 45)
    for no, item in menu_dessert.items():
        print(f"  [{no:2}] {item['nama']:<25} Rp {item['harga']:>7,}")

    print("=" * 45)


def tampilkan_pesanan():
    if not pesanan:
        print("\n⚠️  Belum ada pesanan.")
        return

    print("\n" + "=" * 45)
    print("         🛒  PESANAN ANDA SAAT INI")
    print("=" * 45)
    total = 0
    for no_menu, qty in pesanan.items():
        item = semua_menu[no_menu]
        subtotal = item["harga"] * qty
        total += subtotal
        print(f"  {item['nama']:<25} x{qty}  Rp {subtotal:>7,}")
    print("-" * 45)
    print(f"  {'TOTAL':<30} Rp {total:>7,}")
    print("=" * 45)
    return total


def hitung_total():
    total = 0
    for no_menu, qty in pesanan.items():
        total += semua_menu[no_menu]["harga"] * qty
    return total


def cetak_struk(nama_pelanggan):
    from datetime import datetime
    print("\n")
    print("=" * 45)
    print("          ☕  WARKOP BUDI")
    print("      Jl. Kopi Nusantara No. 88")
    print("          Telp: 021-1234567")
    print("=" * 45)
    print(f"  Pelanggan: {nama_pelanggan}")
    print(f"  Tanggal : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("-" * 45)
    print(f"  {'ITEM':<20} {'QTY':>4}  {'HARGA':>10}")
    print("-" * 45)

    total = 0
    for no_menu, qty in pesanan.items():
        item = semua_menu[no_menu]
        subtotal = item["harga"] * qty
        total += subtotal
        print(f"  {item['nama']:<20} {qty:>4}x  Rp {subtotal:>7,}")

    print("-" * 45)
    print(f"  {'TOTAL':<26} Rp {total:>7,}")

    # Input nominal uang
    while True:
        try:
            bayar = int(input(f"\n  💵  Masukkan nominal uang : Rp "))
            if bayar < total:
                print(f"  ❌  Uang kurang! Kurang Rp {total - bayar:,}")
            else:
                kembalian = bayar - total
                print(f"  ✅  Uang bayar           : Rp {bayar:>7,}")
                print(f"  ✅  Kembalian            : Rp {kembalian:>7,}")
                break
        except ValueError:
            print("  ⚠️  Masukkan angka yang valid!")

    print("=" * 45)
    print(f"     Makasih, {nama_pelanggan}! 😊")
    print("     Terima kasih sudah mampir!")
    print("     Sampai jumpa kembali! ☕")
    print("=" * 45)


# ============================================================
# MAIN PROGRAM - WHILE TRUE LOOP
# ============================================================

print("\n" + "=" * 45)
print("    Selamat datang di ☕  WARKOP BUDI!")
print("=" * 45)
nama_pelanggan = input("  Masukkan nama Anda : ").strip()
if not nama_pelanggan:
    nama_pelanggan = "Pelanggan"
print(f"  Halo, {nama_pelanggan}! Silakan memesan. ☕")

while True:
    print("\n┌─────────────────────────────────┐")
    print("│        MENU UTAMA               │")
    print("│  [1] Pesan Makanan/Minuman      │")
    print("│  [2] Cek Pesanan                │")
    print("│  [3] Bayar & Pulang             │")
    print("└─────────────────────────────────┘")

    pilihan = input("  Pilih menu [1/2/3]: ").strip()

    # ── PILIHAN 1: PESAN ─────────────────────────────────
    if pilihan == "1":
        tampilkan_menu()

        while True:
            try:
                no = int(input("\n  Masukkan nomor menu (0 = selesai pesan): "))
                if no == 0:
                    print("  ✅  Selesai memilih menu.")
                    break
                elif no not in semua_menu:
                    print("  ⚠️  Nomor menu tidak tersedia, coba lagi.")
                else:
                    qty = int(input(f"  Berapa porsi '{semua_menu[no]['nama']}'? : "))
                    if qty <= 0:
                        print("  ⚠️  Jumlah harus lebih dari 0.")
                    else:
                        if no in pesanan:
                            pesanan[no] += qty
                        else:
                            pesanan[no] = qty
                        print(f"  🛒  Ditambahkan: {semua_menu[no]['nama']} x{qty}")
            except ValueError:
                print("  ⚠️  Masukkan angka yang valid!")

    # ── PILIHAN 2: CEK PESANAN ───────────────────────────
    elif pilihan == "2":
        tampilkan_pesanan()

    # ── PILIHAN 3: BAYAR & PULANG ────────────────────────
    elif pilihan == "3":
        if not pesanan:
            print("\n  ⚠️  Tidak ada pesanan. Silakan pesan terlebih dahulu.")
        else:
            cetak_struk(nama_pelanggan)
            print("\n  👋  Sampai jumpa!\n")
            break

    else:
        print("  ⚠️  Pilihan tidak valid. Masukkan 1, 2, atau 3.")