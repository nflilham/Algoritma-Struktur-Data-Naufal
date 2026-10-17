# Sistem manajemen data mahasiswa menggunakan list of dict

data_mahasiswa = []

while True:
    print("\n=== MENU DATA MAHASISWA ===")
    print("1. Tambah Data Mahasiswa")
    print("2. Lihat Data Mahasiswa")
    print("3. Hapus Data Mahasiswa")
    print("4. Keluar")

    pilihan = input("\nPilih menu (1-4): ")

    if pilihan == "1":
        print("\n--- Tambah Data Mahasiswa ---")
        nama = input("Nama       : ")
        nim  = input("NIM        : ")
        umur = input("Umur       : ")
        prodi = input("Prodi      : ")
        alamat = input("Alamat     : ")

        mahasiswa = {
            "Nama": nama,
            "NIM": nim,
            "Umur": umur,
            "Prodi": prodi,
            "Alamat": alamat
        }
        data_mahasiswa.append(mahasiswa)
        print(f"\nData '{nama}' berhasil disimpan!")

    elif pilihan == "2":
        print("\n--- Daftar Data Mahasiswa ---")
        if len(data_mahasiswa) == 0:
            print("Belum ada data mahasiswa.")
        else:
            for i, mhs in enumerate(data_mahasiswa):
                print(f"\nMahasiswa ke-{i + 1}:")
                for key, value in mhs.items():
                    print(f"  {key:<12}: {value}")

    elif pilihan == "3":
        print("\n--- Hapus Data Mahasiswa ---")
        if len(data_mahasiswa) == 0:
            print("Belum ada data yang bisa dihapus.")
        else:
            for i, mhs in enumerate(data_mahasiswa):
                print(f"{i + 1}. {mhs['Nama']} (NIM: {mhs['NIM']})")

            try:
                nomor = int(input("\nMasukkan nomor mahasiswa yang ingin dihapus: "))
                if 1 <= nomor <= len(data_mahasiswa):
                    dihapus = data_mahasiswa.pop(nomor - 1)
                    print(f"Data '{dihapus['Nama']}' berhasil dihapus.")
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")

    elif pilihan == "4":
        print("\nProgram selesai. Sampai jumpa!")
        break

    else:
        print("Pilihan tidak valid. Masukkan angka 1-4.")
    pilihan = input("\nPilih menu (1-4): ")

    if pilihan == "1":
        print("\n--- Tambah Data Mahasiswa ---")
        nama = input("Nama       : ")
        nim  = input("NIM        : ")
        umur = input("Umur       : ")
        prodi = input("Prodi      : ")
        alamat = input("Alamat     : ")

        mahasiswa = {
            "Nama": nama,
            "NIM": nim,
            "Umur": umur,
            "Prodi": prodi,
            "Alamat": alamat
        }
        data_mahasiswa.append(mahasiswa)
        print(f"\nData '{nama}' berhasil disimpan!")

    elif pilihan == "2":
        print("\n--- Daftar Data Mahasiswa ---")
        if len(data_mahasiswa) == 0:
            print("Belum ada data mahasiswa.")
        else:
            for i, mhs in enumerate(data_mahasiswa):
                print(f"\nMahasiswa ke-{i + 1}:")
                for key, value in mhs.items():
                    print(f"  {key:<12}: {value}")

    elif pilihan == "3":
        print("\n--- Hapus Data Mahasiswa ---")
        if len(data_mahasiswa) == 0:
            print("Belum ada data yang bisa dihapus.")
        else:
            for i, mhs in enumerate(data_mahasiswa):
                print(f"{i + 1}. {mhs['Nama']} (NIM: {mhs['NIM']})")

            try:
                nomor = int(input("\nMasukkan nomor mahasiswa yang ingin dihapus: "))
                if 1 <= nomor <= len(data_mahasiswa):
                    dihapus = data_mahasiswa.pop(nomor - 1)
                    print(f"Data '{dihapus['Nama']}' berhasil dihapus.")
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")

    elif pilihan == "4":
        print("\nProgram selesai. Sampai jumpa!")
        break

    else:
        print("Pilihan tidak valid. Masukkan angka 1-4.")