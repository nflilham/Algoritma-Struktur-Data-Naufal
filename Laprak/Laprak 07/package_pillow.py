# Naufal Ilham Fauzan
# 2502106
# Pillow

from PIL import Image, ImageDraw

""" Operasi dasar gambar """
print("=== IMAGE PROCESSING ===") 

# Membuat kanvas gambar baru
img = Image.new("RGB", (400, 200), color="lightblue")

# Tambahkan teks
draw = ImageDraw.Draw(img)  # Membuat objek draw untuk menggambar
draw.text((50, 50), "Halo Nopal!", fill="black")    # Menambahkan teks di kanvas
draw.rectangle([50, 100, 350, 200], outline="red", width=3) # Menggambar kotak
draw.ellipse([100, 150, 300, 250], fill="yellow")   # Menggambar lingkaran

# Simpan gambar
img.save("gambar-nopal.png")    # Menyimpan gambar ke file bernama gambar-nopal.png
print("v gambar-nopal disimpan")