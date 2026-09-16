nilai = input("Masukkan nilai boolean (1/0): ").strip()

if nilai == "1":
	x = True
elif nilai == "0":
	x = False
else:
	print("Input harus 1 atau 0.")
	raise SystemExit

print("Nilai x:", x)