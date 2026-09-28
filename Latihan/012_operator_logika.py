print("\n")
umur = int(input("Berapa umurmu\t\t\t\t: "))
punya_sim_A = input("Apakah kamu punya SIM A? (ya/tidak)\t: ").lower()
punya_sim_C = input("Apakah kamu punya SIM C? (ya/tidak)\t: ").lower()
psikologi = input("Apakah Lulus Tes Psikolog? (ya/tidak)\t: ").lower()
print("\n")

if umur >= 17 and psikologi == "ya" and punya_sim_A == "ya" and punya_sim_C == "ya":
    print("Anda BOLEH mengendarai Motor dan Mobil!")
elif umur >= 17 and psikologi == "ya" and punya_sim_A == "ya" and punya_sim_C == "tidak":
    print("Anda BOLEH mengendarai Mobil!")
elif umur >= 17 and psikologi == "ya" and punya_sim_A == "tidak" and punya_sim_C == "ya":
    print("Anda BOLEH mengendarai Motor!")
else:
    print("Anda TIDAK BOLEH berkendara!")
print("\n")