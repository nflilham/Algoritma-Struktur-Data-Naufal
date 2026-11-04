# Naufal Ilham Fauzan
# 2502106
# qrcode

import qrcode

img = qrcode.make("https://github.com/nflilham")
with open("qr_code.png", "wb") as qr:           # Menyimpan gambar QR Code ke file bernama qr_code.png
    img.save(qr)                                # Menyimpan gambar ke file bernama qr_code.png

print("v qr_code disimpan") 