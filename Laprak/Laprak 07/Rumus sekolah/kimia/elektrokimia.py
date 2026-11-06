"""Modul elektrokimia: sel volta, elektrolisis, Nernst."""
import math


def potensial_sel(e_katoda, e_anoda):
    """Potensial sel E_sel = E_katoda - E_anoda (volt)."""
    return e_katoda - e_anoda


def persamaan_nernst(e0, n_elektron, q, suhu_kelvin=298):
    """E = E0 - (RT / nF) * ln(Q)."""
    if n_elektron <= 0:
        raise ValueError("Jumlah elektron harus positif.")
    if q <= 0:
        raise ValueError("Konstanta Q harus positif.")
    R = 8.314  # J/(mol.K)
    F = 96485  # C/mol
    return e0 - (R * suhu_kelvin / (n_elektron * F)) * math.log(q)


def hukum_faraday_massa(i, t, mr, n_elektron):
    """Massa hasil elektrolisis m = (I * t * Mr) / (n * F)."""
    if n_elektron <= 0:
        raise ValueError("Jumlah elektron harus positif.")
    F = 96485
    return (i * t * mr) / (n_elektron * F)


def muatan_listrik(arus_ampere, waktu_detik):
    """Muatan Q = I * t (Coulomb)."""
    return arus_ampere * waktu_detik


def jumlah_faraday(muatan):
    """Jumlah Faraday = Q / F."""
    F = 96485
    return muatan / F
