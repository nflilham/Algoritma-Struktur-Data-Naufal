# Naufal Ilham Fauzan
# 2520106
# os

import os

# Informasi direktori
print("Direktori kerja saat ini:", os.getcwd())

# Informasi sistem ('nt' untuk Windows, 'posix' untuk Unix/Linux/Mac)
print("Nama sistem:", os.name)

# Cek apakah file/direktori ada
print("File ada:", os.path.exists("test.txt"))
print("Direktori ada:", os.path.exists("my_folder"))

# Informasi file
if os.path.exists("test.txt"):
    print("Adalah file:", os.path.isfile("test.txt"))
    print("Adalah direktori:", os.path.isdir("test.txt"))
    print("Ukuran file:", os.path.getsize("test.txt"), "bytes")

# Path operations
file_path = "/Users/khannedy/documents/file.txt"
print("Direktori:", os.path.dirname(file_path))
print("Nama file:", os.path.basename(file_path))
print("Nama tanpa ekstensi:", os.path.splitext(file_path)[0])
print("Ekstensi:", os.path.splitext(file_path)[1]) 