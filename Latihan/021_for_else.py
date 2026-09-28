# Mencari huruf dalam kata
kata = input("Masukkan kata : ").lower()
huruf_dicari = input("Masukkan huruf yang dicari (a-z) : ").lower()

for huruf in kata:
    if huruf == huruf_dicari:
        print("Huruf", huruf_dicari, "telah ditemukan")
else:
    print("Huruf yang anda cari tidak ditemukan!")