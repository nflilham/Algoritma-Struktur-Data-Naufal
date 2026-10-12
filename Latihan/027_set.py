buah = {"apel", "jeruk", "anggur", "markisa", "mangga"}
print(buah)

# Menambah Value di set
buah.add("semangka")
buah.add("nanas")
print(buah)

# Menghapus Value di set
buah.remove("anggur")
buah.remove("jeruk")
print(buah)
print()

print("Buah yang dimiliki :")
no = 1
for i in buah:
    print(f"{no}. {i}")
    no += 1
print()