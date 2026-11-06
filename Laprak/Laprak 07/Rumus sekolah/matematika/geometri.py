"""Modul rumus bangun datar dan bangun ruang geometri."""
import math


# --- Bangun Datar ---

def luas_persegi(sisi):
    """Luas persegi = sisi * sisi."""
    return sisi ** 2


def keliling_persegi(sisi):
    """Keliling persegi = 4 * sisi."""
    return 4 * sisi


def luas_persegi_panjang(panjang, lebar):
    """Luas persegi panjang = panjang * lebar."""
    return panjang * lebar


def keliling_persegi_panjang(panjang, lebar):
    """Keliling persegi panjang = 2 * (panjang + lebar)."""
    return 2 * (panjang + lebar)


def luas_segitiga(alas, tinggi):
    """Luas segitiga = 0.5 * alas * tinggi."""
    return 0.5 * alas * tinggi


def keliling_segitiga(a, b, c):
    """Keliling segitiga = a + b + c."""
    return a + b + c


def luas_segitiga_heron(a, b, c):
    """Luas segitiga dengan rumus Heron via 3 sisi."""
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def luas_lingkaran(jari_jari):
    """Luas lingkaran = pi * r^2."""
    return math.pi * (jari_jari ** 2)


def keliling_lingkaran(jari_jari):
    """Keliling lingkaran = 2 * pi * r."""
    return 2 * math.pi * jari_jari


def luas_trapesium(alas_a, alas_b, tinggi):
    """Luas trapesium = 0.5 * (a + b) * t."""
    return 0.5 * (alas_a + alas_b) * tinggi


def luas_jajar_genjang(alas, tinggi):
    """Luas jajar genjang = alas * tinggi."""
    return alas * tinggi


def luas_belah_ketupat(d1, d2):
    """Luas belah ketupat = 0.5 * d1 * d2."""
    return 0.5 * d1 * d2


def luas_layang_layang(d1, d2):
    """Luas layang-layang = 0.5 * d1 * d2."""
    return 0.5 * d1 * d2


# --- Bangun Ruang ---

def volume_kubus(sisi):
    """Volume kubus = s^3."""
    return sisi ** 3


def luas_permukaan_kubus(sisi):
    """Luas permukaan kubus = 6 * s^2."""
    return 6 * (sisi ** 2)


def volume_balok(panjang, lebar, tinggi):
    """Volume balok = p * l * t."""
    return panjang * lebar * tinggi


def luas_permukaan_balok(p, l, t):
    """Luas permukaan balok = 2 * (pl + pt + lt)."""
    return 2 * (p * l + p * t + l * t)


def volume_tabung(jari_jari, tinggi):
    """Volume tabung = pi * r^2 * t."""
    return math.pi * (jari_jari ** 2) * tinggi


def luas_permukaan_tabung(jari_jari, tinggi):
    """Luas permukaan tabung = 2 * pi * r * (r + t)."""
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)


def volume_kerucut(jari_jari, tinggi):
    """Volume kerucut = (1/3) * pi * r^2 * t."""
    return (1 / 3) * math.pi * (jari_jari ** 2) * tinggi


def luas_permukaan_kerucut(jari_jari, garis_pelukis):
    """Luas permukaan kerucut = pi * r * (r + s)."""
    return math.pi * jari_jari * (jari_jari + garis_pelukis)


def volume_bola(jari_jari):
    """Volume bola = (4/3) * pi * r^3."""
    return (4 / 3) * math.pi * (jari_jari ** 3)


def luas_permukaan_bola(jari_jari):
    """Luas permukaan bola = 4 * pi * r^2."""
    return 4 * math.pi * (jari_jari ** 2)


def phytagoras_miring(alas, tinggi):
    """Cari sisi miring segitiga siku-siku (c = sqrt(a^2 + b^2))."""
    return math.hypot(alas, tinggi)


def phytagoras_sisi_tegak(sisi_miring, sisi_lain):
    """Cari sisi tegak segitiga siku-siku (a = sqrt(c^2 - b^2))."""
    if sisi_miring <= sisi_lain:
        raise ValueError("Sisi miring harus lebih panjang dari sisi lainnya.")
    return math.sqrt(sisi_miring ** 2 - sisi_lain ** 2)
