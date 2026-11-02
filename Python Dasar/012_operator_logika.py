# Operator Logika
# Naufal Ilham Fauzan
# 2502106

umur = int(input("Masukkan umurmu : "))
punya_sim = input("Apakah kamu punya SIM? (ya/tidak): ").lower()

if umur >= 17 and punya_sim == "ya":
    print("Kamu dapat berkendara!")
else:
    print("Kamu TIDAK DAPAT berkendara!")