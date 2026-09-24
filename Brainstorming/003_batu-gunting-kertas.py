print("\n==============================")
print("      KERTAS GUNTING BATU     ")
print("==============================")

import random

pilihan = ["batu", "gunting", "kertas"]

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

    elif pilihanuser == "kertas" and pilihanbot == "gunting":
        print("\nYahh kamu kalah :(")

    elif pilihanuser == "batu" and pilihanbot == "gunting":
        print("\nKAMU MENANG!")

    elif pilihanuser == "batu" and pilihanbot == "kertas":
        print("\nYahh kamu kalah :(")

    elif pilihanuser == "gunting" and pilihanbot == "kertas":
        print("\nKAMU MENANG!")

    elif pilihanuser == "gunting" and pilihanbot == "batu":
        print("\nYahh kamu kalah :(")

    print("==============================")

    #tes