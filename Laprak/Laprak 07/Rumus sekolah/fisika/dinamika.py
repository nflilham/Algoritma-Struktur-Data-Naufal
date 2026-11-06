"""Modul dinamika: gaya dan hukum Newton."""


def hukum_newton_2(massa, percepatan):
    """Hukum Newton II: F = m * a (Newton)."""
    return massa * percepatan


def percepatan_dari_gaya(gaya, massa):
    """Percepatan a = F / m."""
    if massa <= 0:
        raise ValueError("Massa harus positif.")
    return gaya / massa


def gaya_gesek(koefisien, gaya_normal):
    """Gaya gesek f = mu * N."""
    return koefisien * gaya_normal


def gaya_sentripetal(massa, kecepatan, jari_jari):
    """Gaya sentripetal F = m * v^2 / r."""
    if jari_jari <= 0:
        raise ValueError("Jari-jari harus positif.")
    return massa * (kecepatan ** 2) / jari_jari


def berat(massa, g=9.8):
    """Berat w = m * g (Newton)."""
    return massa * g


def resultan_gaya_searah(f1, f2):
    """Resultan gaya searah F = F1 + F2."""
    return f1 + f2


def resultan_gaya_berlawanan(f1, f2):
    """Resultan gaya berlawanan F = |F1 - F2|."""
    return abs(f1 - f2)


def resultan_gaya_tegak_lurus(f1, f2):
    """Resultan dua gaya tegak lurus: F = sqrt(F1^2 + F2^2)."""
    return (f1 ** 2 + f2 ** 2) ** 0.5
