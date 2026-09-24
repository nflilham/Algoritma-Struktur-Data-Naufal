import random

pilihan = ["batu", "gunting", "kertas"]

# Simpan skor di luar perulangan agar tidak ter-reset
skor_user = 0
skor_bot = 0

print("==========================================")
print("     GAME BATU GUNTING KERTAS KAFE        ")
print("==========================================")

while True:
    pilihanuser = input("\nMasukkan pilihan (batu/gunting/kertas) atau 'q' untuk keluar: ").lower().strip()

    # Fitur keluar dari game
    if pilihanuser == 'q':
        print("\n==========================================")
        print("GAME SELESAI!")
        print(f"Skor Akhir -> Kamu: {skor_user} | Bot: {skor_bot}")
        
        if skor_user > skor_bot:
            print("Selamat! Kamu pemenang utamanya! 🎉")
        elif skor_user < skor_bot:
            print("Sayang sekali, Bot memenangkan game ini! 🤖")
        else:
            print("Hasil akhir Seri! 🤝")
            
        print("==========================================")
        break  # Menghentikan perulangan while

    # Validasi input
    if pilihanuser not in pilihan:
        print("Pilihan nggak valid! Masukkan batu, gunting, kertas, atau 'q'.")
        continue  # Kembali ke awal perulangan

    pilihanbot = random.choice(pilihan)
    print(f"Bot memilih: {pilihanbot}")

    # Menentukan Pemenang & Update Skor
    if pilihanuser == pilihanbot:
        print("Hasil: Seri! 🤝")
    elif (pilihanuser == "kertas" and pilihanbot == "batu") or \
         (pilihanuser == "batu" and pilihanbot == "gunting") or \
         (pilihanuser == "gunting" and pilihanbot == "kertas"):
        print("Hasil: KAMU MENANG! 🎉")
        skor_user += 1
    else:
        print("Hasil: Yahh kamu kalah... 😢")
        skor_bot += 1

    # Tampilkan skor terkini
    print(f"\n--- SKOR SAAT INI ---")
    print(f"Kamu: {skor_user} | Bot: {skor_bot}")
    print("==============================")

    #tes