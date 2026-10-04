print("\n")
umur = int(input("Berapa umurmu\t\t\t\t: "))
punya_sim_A = input("Apakah kamu punya SIM A? (ya/tidak)\t: ").lower()
punya_sim_C = input("Apakah kamu punya SIM C? (ya/tidak)\t: ").lower()
psikologi = input("Apakah Lulus Tes Psikolog? (ya/tidak)\t: ").lower()
print("\n")

ya = {"ya", "iya", "punya", "lulus", "lolos"}
tidak = {"tidak", "nggak", "gak", "ga", "ngga", "nggk", "gk"}


if umur >= 17 and psikologi in ya and punya_sim_A in ya and punya_sim_C in ya:
    print("Anda BOLEH mengendarai Motor dan Mobil!")
    if umur == 17:
        print("Keren! Baru 17 tahun sudah bisa mengendarai Motor dan Mobil!")
    elif umur >= 40 and umur <= 60:
        print("Wah, sudah berumur tapi masih bisa mengendarai Motor dan Mobil!")
elif umur >= 17 and psikologi in ya and punya_sim_A in ya and punya_sim_C in tidak:
    print("Anda BOLEH mengendarai Mobil!")
elif umur >= 17 and psikologi in ya and punya_sim_A in tidak and punya_sim_C in ya:
    print("Anda BOLEH mengendarai Motor!")
else:
    print("Anda TIDAK BOLEH berkendara!")
print("\n")