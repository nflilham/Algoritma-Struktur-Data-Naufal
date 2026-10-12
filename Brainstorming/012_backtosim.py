# Membuat SIM ke Polres

def header():
    print("=" * 40)
    print("Selamat datang di Polres".center(40))
    print("=" * 40)

header()

nama = input("Masukkan nama\t: ")
umur = int(input("masukkan umur\t: "))

ya = {"mau", "ya", "iya", "buat", "y"}
tidak = {"tidak", "engga", "ga", "g", "n"}

while umur >= 17:
    sim = input(f"Halo {nama}, apakah kamu mau membuat SIM? (ya/tidak) ").lower()
    if sim in ya:
        tes_psikologi = input("Apakah sudah tes psikologi? (ya/tidak) ").lower()
        if tes_psikologi in ya:
            tes_kesehatan = input("Apakah sudah tes kesehatan? (ya/tidak) ").lower()
            if tes_kesehatan in ya:
                sim_apa = input("Mau bikin SIM A / SIM C : ").lower()
                if sim_apa == "sim c":
                    print(f"Selamat {nama}, kamu berhasil membuat SIM C! kamu boleh mengendarai motor")
                    break
                elif sim_apa == "sim a":
                    print(f"Selamat {nama}, kamu berhasil membuat SIM A! kamu boleh mengendarai mobil")
                    break
                else:
                    print("Tidak valid! silahkan coba lagi!")
                    continue
            elif tes_kesehatan in tidak:
                print("Silahkan cek kesehatan di medis dan kembali lagi nanti")
                break
            else:
                print("Tidak valid! silahkan coba lagi!")
                continue
        elif tes_psikologi in tidak:
            print("Silahkan ke ruang tes psikolog dan kembali lagi ke sini")
            break
        else:
            print("Tidak valid! silahkan coba lagi!")
            continue
    elif sim in tidak:
        print("Terima kasih sudah mengunjungi polres")
        break
    else:
        print("Tidak valid! silahkan coba lagi!")
        continue
else:
    input("Apa yang dilakukan bocah sepertimu di polres? ")
    print("Pulanglah pada orang tuamu nak...")
    print()