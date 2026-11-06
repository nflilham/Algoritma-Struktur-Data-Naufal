"""Modul kemagnetan dan induksi elektromagnetik."""
import math


def gaya_lorentz(muatan, kecepatan, medan_magnet, sudut_deg=90):
    """Gaya Lorentz F = q * v * B * sin(theta) (Newton)."""
    sudut_rad = math.radians(sudut_deg)
    return muatan * kecepatan * medan_magnet * math.sin(sudut_rad)


def gaya_kawat_berarus(arus, panjang, medan_magnet, sudut_deg=90):
    """Gaya pada kawat berarus F = B * I * L * sin(theta) (Newton)."""
    sudut_rad = math.radians(sudut_deg)
    return medan_magnet * arus * panjang * math.sin(sudut_rad)


def induksi_magnetik_kawat_lurus(arus, jarak, mu0=4 * math.pi * 1e-7):
    """Induksi magnetik kawat lurus panjang B = (mu0 * I) / (2 * pi * a) (Tesla)."""
    if jarak <= 0:
        raise ValueError("Jarak harus positif.")
    return (mu0 * arus) / (2 * math.pi * jarak)


def induksi_magnetik_solenoida(arus, jumlah_lilitan, panjang_solenoida, mu0=4 * math.pi * 1e-7):
    """Induksi magnetik solenoida B = mu0 * n * I, n = N/L (Tesla)."""
    if panjang_solenoida <= 0:
        raise ValueError("Panjang solenoida harus positif.")
    n = jumlah_lilitan / panjang_solenoida
    return mu0 * n * arus


def fluks_magnetik(medan_magnet, luas, sudut_deg=0):
    """Fluks magnetik phi = B * A * cos(theta) (Weber)."""
    sudut_rad = math.radians(sudut_deg)
    return medan_magnet * luas * math.cos(sudut_rad)


def ggl_induksi(jumlah_lilitan, delta_fluks, delta_waktu):
    """GGL induksi (hukum Faraday) epsilon = -N * delta_phi / delta_t (Volt)."""
    if delta_waktu <= 0:
        raise ValueError("Waktu harus positif.")
    return -jumlah_lilitan * delta_fluks / delta_waktu


def induktansi_diri(ggl_induksi, delta_arus, delta_waktu):
    """Induktansi diri L = -epsilon / (dI/dt) (Henry)."""
    if delta_waktu <= 0:
        raise ValueError("Waktu harus positif.")
    return -ggl_induksi / (delta_arus / delta_waktu)
