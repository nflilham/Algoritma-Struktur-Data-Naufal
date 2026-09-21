#Tugas variabel dalam 1 biodata
#Nama: Naufal Ilham Fauzan
#NIM: 2502106

nama = input("Masukkan nama: ")
nim = int(input("Masukkan NIM: "))
umur = int(input("Masukkan umur: "))
jenis_kelamin = input("Masukkan jenis kelamin: ")
alamat = input("Masukkan alamat: ")
tinggi_badan = float(input("Masukkan tinggi badan (cm): "))
berat_badan = float(input("Masukkan berat badan (kg): "))
apakah_mahasiswa = bool(input("Apakah Anda seorang mahasiswa? (y/t): ") == 'y')
apakah_bekerja = bool(input("Apakah Anda bekerja? (y/t): ") == 'y')
apakah_menikah = bool(input("Apakah Anda menikah? (y/t): ") == 'y')
apakah_berpacaran = bool(input("Apakah Anda berpacaran? (y/t): ") == 'y')
hewan_peliharaan = input("Nama hewan peliharaan: ")
makanan_favorit = input("Masukkan makanan favorit: ")
minuman_favorit = input("Masukkan minuman favorit: ")
hobi = input("Masukkan hobi: ")
game_favorit = input("Masukkan game favorit: ")
film_favorit = input("Masukkan film favorit: ")
matakuliah_favorit = input("Masukkan mata kuliah favorit: ")
dosen_favorit = input("Masukkan nama dosen favorit: ")
kampus_favorit = input("Masukkan nama kampus favorit: ")
urlkampus = input("Masukkan URL kampus: ")
path = input("Masukkan Path file ini: ")

biodata = f"========================================\n          BIODATA SEDERHANA          \n========================================\n Nama \t\t: {nama}\n Nama panggilan\t: {nama[0:6]}\n Nama KTP\t: {nama.upper()}\n Umur\t\t: {umur}\n U taun depan\t: {umur+1}\n Jenis Kelamin\t: {jenis_kelamin}\n Tinggi badan\t: {tinggi_badan}\n Berat badan\t: {berat_badan}\n Mahasiswa?\t: {apakah_mahasiswa}\n Bekerja?\t: {apakah_bekerja}\n Menikah?\t: {apakah_menikah}\n Pacaran?\t: {apakah_berpacaran}\n Nama pet\t: {hewan_peliharaan}\n Makanan Fav\t: {makanan_favorit}\n Minuman Fav\t: {minuman_favorit}\n Hobi\t\t: {hobi}\n Game Fav\t: {game_favorit}\n Film fav\t: {film_favorit}\n Matkul Fav\t: {matakuliah_favorit}\n Dosen Fav\t: {dosen_favorit}\n Kampus Fav\t: {kampus_favorit}\n Url Kampus\t: {urlkampus}\n Path file\t: {path}\n========================================"
print(biodata)

#========================================\n          BIODATA SEDERHANA          \n========================================\n