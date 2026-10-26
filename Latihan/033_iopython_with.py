print()
print("=== MENAMPILKAN DATA NILAI ===")

try:
    with open("nilai_mahasiswa.txt", "r") as file:
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
            print(data[77])
            print("-" * 40)
            print()

except FileNotFoundError:
    print("File tidak ditemukan!")
except IndexError:
    print("Index tidak Ditemukan!")
else:
    print("Periksa kembali file/data yang kamu miliki!")

print("=== SELESAI ===")
print()