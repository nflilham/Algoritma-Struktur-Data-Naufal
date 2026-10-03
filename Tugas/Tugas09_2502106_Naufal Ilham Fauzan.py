# ====================================================================
# Tugas 9 - Studi Kasus
# Naufal Ilham Fauzan
# 2502106
# ====================================================================
# Ketentuan Tugas   :
# While Loop        : Game Loop Utama
# While Else        : Mini game brankas
# For Loop          : Menampilkan isi Tas
# For String        : Dekripsi gangguan karakter di Sinyal Radio
# Break & Continue  : Hampir semua if-else ada
# Nested Loop       : Mencetak Grid radar
# ====================================================================

# Studi kasus ini saya bereksperimen untuk membuat sebuah game survival kiamat zombie dengan berbagai fitur
# SYARAT berhasil memenangkan game ini adalah pemain harus menuju Helipad dan berhasil mendekripsi sinyal radio untuk kabur dari kota

# Tahap 0 : Dimulai dari membuat variabel pemain
darah = 100
hari = 0
pemain_hidup = True

# Header
print("\n========================================")
print("||           KIAMAT ZOMBIE            ||")
print("========================================")

# Pilihan 1
# Dibuat agar Pilihan 1 saat mengeksplorasi tidak ke 1 tempat saja
import random
pilihan_1 = ["Kamu menyusuri bangunan kosong", "Kamu menyusuri hutan penuh darah", "Kamu menyusuri rumah sakit", "Kamu menyusuri perumahan warga yang terbengkalai"]
pilihan_1_random = random.choice(pilihan_1)

# Pilihan 2
# Dibuat agar Pilihan 2 bisa mengecek isi Tas pemain
# Pemain memiliki starter pack sebagai berikut
tas = ["Roti", "Air Minum", "Obat", "Senter Rusak", "Baterai Senter", "Nasi Padang"]

# Pilihan 3
# Dibuat agar Pilihan 3 bisa membobol brankas dan mendapat barang
brankas_terbuka = False
bobol_harian = False
pin_brankas = str(random.randint(1, 5))

# Pilihan 4
# Dibuat untuk Pilihan 4, sinyal radio dengan noise, jika terbaca jelas permainan selesai dan pemain menang
# Dekripsi harian hanya bisa menghapus 2 gangguan (#) per harinya
sinyal_radio = "S#O#S#_#H#E#L#I#P#A#D#_#A#M#A#N#_#K#O#D#E#:#7#7#7"
dekripsi_harian = False

# Pilihan 5
# Dibuat untuk koordinat Peta 2D (Baris dan Kolom) dengan ukuran 5x5
# Berikut posisi awal pemain dan zombie serta posisi fiks helipad (di ujung kanan atas)
posisi_pemain = [2, 2]
posisi_helipad = [0, 4]
posisi_zombie = [3, 1]

# ====================================================================
# KETENTUAN "WHILE LOOP"
# ====================================================================
while pemain_hidup and darah > 0:
    print("========================================")
    print(f"[ Hari ke {hari} ] | [ Darah kamu : {darah} ]")
    print("========================================")
    print("Pilihan Kegiatan:")
    print("1 : Jelajah Area")
    print("2 : Cek Inventory")
    print("3 : Bobol Brankas Suplai")
    print("4 : Cek Transmisi Radio")
    print("5 : Lihat Radar Peta 2D")
    print("6 : Menyerah")

    pilihan_kegiatan = input("\nMasukkan pilihan aksi (1-6): ")

# ====================================================================
# PILIHAN 1 : JELAJAH AREA
# ====================================================================
    if pilihan_kegiatan == "1":
        print("\n=== NAVIGASI PERGERAKAN PETA ===")
        print("Arah Gerak: [W] Atas | [S] Bawah | [A] Kiri | [D] Kanan")
        arah = input("Pilih arah bergerak (W/A/S/D): ").upper()

        if arah == "W" and posisi_pemain[0] > 0:
            posisi_pemain[0] -= 1
        elif arah == "S" and posisi_pemain[0] < 4:
            posisi_pemain[0] += 1
        elif arah == "A" and posisi_pemain[1] > 0:
            posisi_pemain[1] -= 1
        elif arah == "D" and posisi_pemain[1] < 4:
            posisi_pemain[1] += 1
        else:
            print("\n[!] Kamu menabrak tembok! Tidak bisa lewat.") 

        arah_zombie = random.choice([[-1, 0], [1, 0], [0, -1], [0, 1]])
        z_baris_baru = posisi_zombie[0] + arah_zombie[0]
        z_kolom_baru = posisi_zombie[1] + arah_zombie[1]

        if 0 <= z_baris_baru <= 4 and 0 <= z_kolom_baru <= 4:
            if [z_baris_baru, z_kolom_baru] != posisi_helipad:
                posisi_zombie = [z_baris_baru, z_kolom_baru]
    
        print(f"\n[!] {pilihan_1_random}")
        dekripsi_harian = False
        bobol_harian = False
        pin_brankas = str(random.randint(1, 5))
        print("[!] Hari telah berganti! Tranmisi radio dapat digunakan!")
        print("[!] Kamu dapat membobol brankas!\n")

        print(f"[!] Pemain berpindah ke : Baris {posisi_pemain[0]}, Kolom {posisi_pemain[1]}")
        print(f"[!] Zombie juga bergerak! (Cek radar di Menu 5)\n")

        if posisi_pemain == posisi_zombie:
            print("\n==================================================")
            print("[GAWAT!] ZOMBIE MENYERGAPMU DI TITIK YANG SAMA!")
            print("[!] Zombie menggigitmu dengan ganas! HP berkurang -35.")
            print("==================================================\n")
            hp -= 25

        if "#" in sinyal_radio:
            print("[!] PERINGATAN: Sinyal transmisi radio belum terdekripsi sepenuhnya!")
            print("[!] Kamu belum memiliki kode evakuasi resmi dari radio untuk memanggil helikopter.")
            print("[!] Dekripsi radio (Menu 4) terlebih dahulu sebelum kembali ke sini.")
        else:
            kode_input = input("Masukkan Kode Rahasia Evakuasi Radio: ")
            if kode_input == "777":
                print("\n==================================================")
                print(" [SELAMAT!] Helikopter mendarat dan menyelamatkanmu!")
                print(" KAMU BERHASIL TAMAT & SELAMAT DARI KOTA ZOMBIE!")
                print("==================================================")
                break
            else:
                print("\n[X] KODE SALAH! Helikopter mengabaikan sinyalmu.")

        hari += 1
        darah -= 15
        if darah <= 0:
            print("\nGAME OVER! Darah kamu habis dan kamu berubah jadi ZOMBIE!")
            break

# ====================================================================
# PILIHAN 2 : TAS
# KETENTUAN FOR LOOP, FOR ELSE
# ====================================================================
    elif pilihan_kegiatan == "2":       
        print("\n=== ISI TAS KAMU ===")
        if not tas:
            print("Tas Kamu kosong")
        else:
            no = 1
            for barang in tas:
                print(f"{no}. {barang}")
                no += 1

            cari_barang = input("\nMasukkan nama barang yang ingin digunakan : ")

            for barang in tas:
                if barang.lower() == cari_barang.lower():
                    if barang in ["Roti", "Air Minum", "Obat", "Nasi Padang"]:
                        print(f"\n[+] Kamu menggunakan {barang}! Darah bertambah +15")
                        darah = min(100, darah + 15)
                        tas.remove(barang)
                    else:
                        print(f"\n[-] {barang} tidak bisa dimakan/digunakan untuk menyembuhkan.")
                    break
            else:
                print(f"\n[X] Barang '{cari_barang}' tidak ditemukan di dalam tas kamu!")

# ====================================================================
# PILIHAN 3 : MINI GAME BOBOL BRANKAS
# KETENTUAN WHILE ELSE
# ====================================================================
    elif pilihan_kegiatan == "3":
        if bobol_harian:
            print("\n[-] Brankas ini sudah dibobol!")
            print("[!] Menjelajahlah untuk menemukan brankas baru!")
            continue

        print("\n=== BOBOL BRANKAS ===\n")
        print("Tebak 1 angka yang menjadi PIN brankas (1-5)!\nKamu punya 3x keempatan!")

        kesempatan = 3

        while kesempatan > 0:
            tebakan = input(f"Sisa kesempatan = {kesempatan}x! Tebak PIN brankas : ")

            if tebakan == pin_brankas:
                print("\n[+] CRACK! Kamu berhasil membobol brankas! Kamu mendapat Nasi Padang dan Roti\n")
                tas.append("Nasi Padang")
                tas.append("Roti")
                tas.append("Obat")
                bobol_harian = True
                break
            else:
                kesempatan -= 1
                print(f"Tebakan kamu salah! PIN \'{tebakan}\' bukan jawabannya!")

        else:
            print("\n[!] Kesempatan Menebak Habis! Alarm brankas berbunyi dan gerombolan zombie mulai berdatangan!!!")
            print(f"[!] PIN yang benar adalah : \'{pin_brankas}\'")
            print("[!] Darah kamu berkurang -25")
            bobol_harian = True
            darah -= 25
            if darah <= 0:
                print("\nGAME OVER! Darah kamu habis dan kamu berubah jadi ZOMBIE!")
                break

# ====================================================================
# PILIHAN 4 : DEKRIPSI GANGGUAN
# KETENTUAN FOR STRING, CONTINUE
# ====================================================================
    elif pilihan_kegiatan == "4":
        if dekripsi_harian:
            print("\n[!] Kamu sudah membersihkan 2 gangguan hari ini!")
            print("[!] Tunggu besok hari untuk lanjut membersihkan gangguan!")
            continue

        if "#" not in sinyal_radio:
            print("\n[+] Transimi Radio sudah 100% Di Dekripsi!")
            print(f"Pesannya adalah : {sinyal_radio}")

        print("\n=== DEKRIPSI TRANSMISI RADIO ===")
        print(f"Sinyal Sebelum : {sinyal_radio}")
        
        sinyal_baru = ""
        gangguan_dihilangkan = 0
        
        for karakter in sinyal_radio:
            if karakter == "#" and gangguan_dihilangkan < 2:
                gangguan_dihilangkan += 1
                continue
            
            sinyal_baru += karakter

        sinyal_radio = sinyal_baru
        dekripsi_harian = True

        print(f"Sinyal Sesudah : {sinyal_radio}")
        print(f"\n[+] Berhasil membersihkan {gangguan_dihilangkan} simbol '#' hari ini!")

# ====================================================================
# PILIHAN 5 : MENAMPILKAN PETA
# KETENTUAN NESTED LOOP
# ====================================================================
    elif pilihan_kegiatan == "5":
        print("\n=== RADAR PETA 2D AREA KARANTINA (5x5) ===")
        print("Keterangan: [P] = Pemain | [H] = Helipad Evakuasi | [Z] = Zombie | [.] = Kosong\n")

        for x in range(5):
            for y in range(5):
                posisi_saat_ini = [x, y]
                
                if posisi_saat_ini == posisi_pemain:
                    print("[P]", end=" ")
                elif posisi_saat_ini == posisi_helipad:
                    print("[H]", end=" ")
                elif posisi_saat_ini == posisi_zombie:
                    print("[Z]", end=" ")
                else:
                    print("[.]", end=" ")
            
            print() 

# ====================================================================
# PILIHAN 6 : MENYERAH DAN KELUAR DARI GAME
# ====================================================================
    elif pilihan_kegiatan == "6":
        print("\n========================================")
        print("[!] Kamu menyerah dan dimakan zombie")
        print("========================================\n")
        break

# ====================================================================
# ERROR | JIKA MEMILIH DILUAR ANGKA 1-6
# ====================================================================
    else:
        print("[X] Pilihan tidak Valid! Pilih (1-6)!")
        continue

print("\n==================================================")
print("       TERIMA KASIH TELAH MEMAINKAN GAME INI      ")
print("==================================================\n")