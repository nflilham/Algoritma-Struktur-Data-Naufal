"""Modul usaha dan energi."""


def usaha(gaya, perpindahan, sudut_deg=0):
    """Usaha W = F * s * cos(theta) (Joule)."""
    import math
    sudut_rad = math.radians(sudut_deg)
    return gaya * perpindahan * math.cos(sudut_rad)


def energi_kinetik(massa, kecepatan):
    """Energi kinetik Ek = 0.5 * m * v^2 (Joule)."""
    return 0.5 * massa * (kecepatan ** 2)


def energi_potensial(massa, tinggi, g=9.8):
    """Energi potensial Ep = m * g * h (Joule)."""
    return massa * g * tinggi


def energi_mekanik(ek, ep):
    """Energi mekanik Em = Ek + Ep."""
    return ek + ep


def daya(usaha, waktu):
    """Daya P = W / t (Watt)."""
    if waktu <= 0:
        raise ValueError("Waktu harus positif.")
    return usaha / waktu


def daya_dari_gaya(gaya, kecepatan):
    """Daya P = F * v (Watt)."""
    return gaya * kecepatan


def efisiensi(daya_output, daya_input):
    """Efisiensi eta = (P_out / P_in) * 100%."""
    if daya_input <= 0:
        raise ValueError("Daya input harus positif.")
    return (daya_output / daya_input) * 100
