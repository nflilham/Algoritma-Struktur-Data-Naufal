print("\n")
umur = int(input("Berapa umurmu\t\t\t\t: "))
punya_sim_A = input("Apakah kamu punya SIM A? (ya/tidak)\t: ").lower()
punya_sim_C = input("Apakah kamu punya SIM C? (ya/tidak)\t: ").lower()
psikologi = input("Apakah Lulus Tes Psikolog? (ya/tidak)\t: ").lower()
print("\n")

if umur >= 17 and psikologi in ["ya", "iya", "punya", "lulus", "lolos"] and punya_sim_A in ["ya", "iya", "punya", "lulus", "lolos"] and punya_sim_C in ["ya", "iya", "punya", "lulus", "lolos"]:
    print("Anda BOLEH mengendarai Motor dan Mobil!")
elif umur >= 17 and psikologi in ["ya", "iya", "punya", "lulus", "lolos"] and punya_sim_A in ["ya", "iya", "punya", "lulus", "lolos"] and punya_sim_C in ["tidak", "nggak", "gak", "ga", "ngga", "nggk", "gk"]:
    print("Anda BOLEH mengendarai Mobil!")
elif umur >= 17 and psikologi in ["ya", "iya", "punya", "lulus", "lolos"] and punya_sim_A in ["tidak", "nggak", "gak", "ga", "ngga", "nggk", "gk"] and punya_sim_C in ["ya", "iya", "punya", "lulus", "lolos"]:
    print("Anda BOLEH mengendarai Motor!")
else:
    print("Anda TIDAK BOLEH berkendara!")
print("\n") 