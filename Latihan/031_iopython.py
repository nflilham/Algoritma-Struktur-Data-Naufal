print("=== SIMPAN DATA NILAI ===")

with open("nilai_mahasiswa.txt", "a") as file:

    no = 0
    while True:

        nama = input(f"Nama Mahasiswa ke-{no+1}\t: ")
        no += 1
        if nama == "":
            break

        nim = int(input("Masukkan NIM\t\t: "))
        if nim == "":
            break

        prodi = input("Masukkan Prodi\t\t: ")
        if prodi == "":
            break

        fakultas = input("Masukkan Fakultas\t: ")
        if fakultas == "":
            break

        univ = input("Masukkan Universitas\t: ")
        if univ == "":
            break

        matkul = input("Masukkan Mata Kuliah\t: ")
        if matkul == "":
            break

        dosen = input("Masukkan Dosen\t\t: ")
        if dosen == "":
            break

        tahun_ajaran = input("Masukkan Tahun Ajaran\t: ")
        if tahun_ajaran == "":
            break

        semester = input("Masukkan Semester\t: ")
        if semester == "":
            break
        
        nilai = int(input("Masukkan Nilai\t\t: "))
        if nilai == "":
            break
        
        # Tulis ke file
        file.write(f" {no}. {nama}, {nim}, {prodi}, {fakultas}, {univ}, {nilai}, {semester}, {matkul}, {dosen}, {tahun_ajaran}\n")
        print(f"Data nomor {no} atas nama {nama} berhasil disimpan!\n")

    print("Data telah disimpan ke file nilai_siswa.txt\n")

    # nama, nim, prodi, fakultas, univ, nilai, matkul, dosen, tahun ajaran