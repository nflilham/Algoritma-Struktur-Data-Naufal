angka = [1, 2, 2, 3, 3, 3]
angka = set(angka)

print(angka)

for i in angka:
    print(i)
    
print() 

bilangan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Bilangan ganjil:")
for i in bilangan:
    if i % 2 != 0:
        print(i)

print("Bilangan genap:")
for i in bilangan:
    if i % 2 == 0:
        print(i)
