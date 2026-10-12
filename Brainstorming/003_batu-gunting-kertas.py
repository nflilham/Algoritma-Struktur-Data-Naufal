print("=" * 40)
print("KERTAS GUNTING BATU".center(40))
print("=" * 40)

import random
pilihan = ["batu", "gunting", "kertas"]

poin_player = 0
poin_bot = 0

while True:
    pilihanuser = input("Masukkan pilihanmu\n(kertas/gunting/batu) : ").lower()
    if pilihanuser not in pilihan:
        print("TIDAK VALID!")
        continue

    pilihanbot = random.choice(pilihan)

    print("\nPilihanmu\t= ", pilihanuser, "\nPilihan bot\t= ", pilihanbot)
    if pilihanuser == pilihanbot:
        print("\nYahhh sama-sama", pilihanuser)

    elif pilihanuser == "kertas" and pilihanbot == "batu":
        print("\nKAMU MENANG!")
        poin_player += 1

    elif pilihanuser == "kertas" and pilihanbot == "gunting":
        print("\nYahh kamu kalah :(")
        poin_bot += 1

    elif pilihanuser == "batu" and pilihanbot == "gunting":
        print("\nKAMU MENANG!")
        poin_player += 1

    elif pilihanuser == "batu" and pilihanbot == "kertas":
        print("\nYahh kamu kalah :(")
        poin_bot += 1

    elif pilihanuser == "gunting" and pilihanbot == "kertas":
        print("\nKAMU MENANG!")
        poin_player += 1

    elif pilihanuser == "gunting" and pilihanbot == "batu":
        print("\nYahh kamu kalah :(")
        poin_bot += 1

    print(f"Poin kamu = {poin_player}")
    print(f"Poin bot  = {poin_bot}")
    print("=" * 40)    #tes