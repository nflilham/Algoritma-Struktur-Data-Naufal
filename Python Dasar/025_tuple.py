point = (1, 2, 3)

print(point[0])
print(point[1])
print(point[2])
print()

for i in point:
    print(i)
print()

# Untuk data yang tidak bisa diubah
tanggal_lahir = (8, 9, 2006)
print(f"Tanggal lahir\t: {tanggal_lahir[0]}\nBulan\t\t: {tanggal_lahir[1]}\nTahun\t\t: {tanggal_lahir[2]}" )
print()

for j in tanggal_lahir:
    print(j)
print()

for k in range(len(tanggal_lahir)):
    print(tanggal_lahir[k])