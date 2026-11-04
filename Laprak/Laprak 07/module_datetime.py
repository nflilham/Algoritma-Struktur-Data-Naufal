# Naufal Ilham Fauzan
# 2502106
# datetime

import datetime 

# Tanggal dan waktu lengkap
sekarang = datetime.datetime.now()
print("Sekarang:", sekarang)

# Hanya tanggal
hari_ini = datetime.date.today()
print("Hari ini:", hari_ini)

# Hanya waktu
waktu_sekarang = datetime.datetime.now().time()
print("Waktu sekarang:", waktu_sekarang)

# Membuat tanggal tertentu
ulang_tahun = datetime.date(2024, 12, 25)
print("Ulang tahun:", ulang_tahun)

# Membuat waktu tertentu
acara = datetime.datetime(2024, 6, 15, 14, 30, 0)
print("Waktu acara:", acara)

# Format Indonesia
print("Format ID:", sekarang.strftime("%d/%m/%Y %H:%M:%S"))

# Format panjang
print("Format panjang:", sekarang.strftime("%A, %d %B %Y"))

# Format custom
print("Format custom:", sekarang.strftime("%d-%m-%Y jam %H:%M"))