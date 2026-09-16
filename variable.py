#Mencoba variabel di python
#Nama: Naufal Ilham Fauzan
#NIM: 2502106

x = int(input("Masukkan nilai x: "))                                       #Membuat variabel x dengan nilai 7
y = float(input("Masukkan nilai y: "))                                     #Membuat variabel y dengan nilai 7.7
nama = input("Masukkan nama: ")                           #Membuat variabel nama dengan nilai "Naufal Ilham Fauzan"
nim = input("Masukkan NIM: ")                             #Membuat variabel nim dengan nilai "2502106"
alamat = input("Masukkan alamat: ")                         #Membuat variabel alamat dengan nilai "Dusun Awisurat, Desa Tanjungsari"
is_student = bool(input("Mahasiswa? (True/False): "))                           #Membuat variabel is_student dengan nilai True

print("Nilai x   :", x)         #Menampilkan nilai dari variabel x
print("Nilai y   :", y)         #Menampilkan nilai dari variabel y
print("Nama      :", nama)      #Menampilkan nilai variabel nama
print("NIM       :", nim)       #Menampilkan nilai variabel nim
print("Alamat    :", alamat)    #Menampilkan nilai variabel alamat
print("Mahasiswa?:", is_student)#Menampilkan nilai variabel is_student

print(type(x))           #Menampilkan tipe data dari variabel x
print(type(y))           #Menampilkan tipe data dari variabel y
print(type(nama))        #Menampilkan tipe data dari variabel nama
print(type(nim))         #Menampilkan tipe data dari variabel nim
print(type(alamat))      #Menampilkan tipe data dari variabel alamat
print(type(is_student))  #Menampilkan tipe data dari variabel is_student