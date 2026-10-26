print()
print("=== MENAMPILKAN DATA NILAI ===")

file = open("nilai_mahasiswa.txt", "r")

for line in file:
    data = line.strip().split(",")
    print(f"Nama Mahasiswa\t: {data[0]}")
    print(f"NIM\t\t: {data[1]}")
    print(f"Prodi\t\t: {data[2]}")
    print(f"Fakultas\t: {data[3]}")
    print(f"Universitas\t: {data[4]}")
    print(f"Nilai\t\t: {data[5]}")
    print(f"Semester\t: {data[6]}")
    print(f"Mata Kuliah\t: {data[7]}")
    print(f"Dosen\t\t: {data[8]}")
    print(f"Tahun Ajaran\t: {data[9]}")
    print("-" * 40)
    print()
    
file.close()

print("=== SELESAI ===")
print()