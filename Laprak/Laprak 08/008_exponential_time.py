def kombinasi_biner(n):
    if n == 0:
        return [""]

    sebelumnya = kombinasi_biner(n-1)
    hasil = []

    for item in sebelumnya:
        hasil.append(item + "0")
        hasil.append(item + "1")

    return hasil

print(kombinasi_biner(3))