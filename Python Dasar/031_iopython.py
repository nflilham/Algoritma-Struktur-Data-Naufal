print("=== SIMPAN DATA NILAI ===")

with open("nilai_mahasiswa.txt", "a") as file:

    # penjelasan: hitung baris yang sudah ada agar nomor melanjutkan dari data sebelumnya
    try:
        with open("nilai_mahasiswa.txt", "r") as f:
            no = sum(1 for line in f if line.strip())
    except FileNotFoundError:
        no = 0

    while True:

        nama = input(f"Nama Mahasiswa ke-{no+1}\t: ")
        no += 1
        if nama == "":
            break

        try:
            nim = int(input("Masukkan NIM\t\t: "))
            if nim == "":
                break
        except ValueError:
            print("Masukkan angka yang valid!")
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

        try:
            nilai = int(input("Masukkan Nilai\t\t: "))
            if nilai == "":
                break
        except ValueError:
            print("Masukkan angka yang valid!")
            break

        # penjelasan: nomor ditulis sebagai field pertama tersendiri, bukan digabung ke nama
        file.write(f" No {no} :, {nama}, {nim}, {prodi}, {fakultas}, {univ}, {nilai}, {semester}, {matkul}, {dosen}, {tahun_ajaran}\n")
        print(f"Data nomor {no} atas nama {nama} berhasil disimpan!\n")

    file.close()
    print("Data telah disimpan ke file nilai_mahasiswa.txt\n")

    # nama, nim, prodi, fakultas, univ, nilai, matkul, dosen, tahun ajaran