"""Modul fluida: tekanan dan hukum Archimedes."""


def tekanan_hidrostatis(massa_jenis, kedalaman, g=9.8):
    """Tekanan hidrostatis P = rho * g * h (Pascal)."""
    return massa_jenis * g * kedalaman


def tekanan_total(tekanan_udara, tekanan_hidrostatis):
    """Tekanan total = P_udara + P_hidrostatis."""
    return tekanan_udara + tekanan_hidrostatis


def hukum_pascal(gaya_input, luas_input, luas_output):
    """Hukum Pascal: F_out = F_in * (A_out / A_in)."""
    if luas_input <= 0:
        raise ValueError("Luas input harus positif.")
    return gaya_input * (luas_output / luas_input)


def gaya_archimedes(massa_jenis_fluida, volume_tercelup, g=9.8):
    """Gaya Archimedes F_a = rho_fluida * V_tercelup * g (Newton)."""
    return massa_jenis_fluida * volume_tercelup * g


def massa_jenis(massa, volume):
    """Massa jenis rho = m / V (kg/m^3)."""
    if volume <= 0:
        raise ValueError("Volume harus positif.")
    return massa / volume


def persamaan_kontinuitas(luas1, kecepatan1, luas2):
    """Persamaan kontinuitas A1*v1 = A2*v2, return v2."""
    if luas2 <= 0:
        raise ValueError("Luas 2 harus positif.")
    return (luas1 * kecepatan1) / luas2


def persamaan_bernoulli_kecepatan(tekanan1, tekanan2, rho, ketinggian1, ketinggian2, g=9.8):
    """Bernoulli sederhana untuk cari v2 dari v1=0: v2 = sqrt(2*(P1-P2)/rho + 2*g*(h1-h2))."""
    import math
    delta_p = tekanan1 - tekanan2
    delta_h = ketinggian1 - ketinggian2
    nilai = 2 * delta_p / rho + 2 * g * delta_h
    if nilai < 0:
        raise ValueError("Nilai di bawah akar negatif.")
    return math.sqrt(nilai)


def viskositas_hukum_stokes(gaya, koef_viskositas, jari_jari, kecepatan):
    """Hukum Stokes F = 6 * pi * eta * r * v."""
    import math
    return 6 * math.pi * koef_viskositas * jari_jari * kecepatan
