print()
print("=== MENAMPILKAN DATA NILAI ===")
print()

file = open("nilai_mahasiswa.txt", "r")

# penjelasan: data[0] = nomor urut (dari file), sisanya geser satu index
for line in file:
    data = line.strip().split(",")
    print(f"-- Data {data[0]}")
    print(f"Nama Mahasiswa\t: {data[1]}")
    print(f"NIM\t\t: {data[2]}")
    print(f"Prodi\t\t: {data[3]}")
    print(f"Fakultas\t: {data[4]}")
    print(f"Universitas\t: {data[5]}")
    print(f"Nilai\t\t: {data[6]}")
    print(f"Semester\t: {data[7]}")
    print(f"Mata Kuliah\t: {data[8]}")
    print(f"Dosen\t\t: {data[9]}")
    print(f"Tahun Ajaran\t: {data[10]}")
    print("-" * 40)
    print()
    
file.close()

print("=== SELESAI ===")
print()
