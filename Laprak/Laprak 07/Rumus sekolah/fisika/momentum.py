"""Modul momentum dan impuls."""


def momentum(massa, kecepatan):
    """Momentum p = m * v (kg.m/s)."""
    return massa * kecepatan


def impuls(gaya, waktu):
    """Impuls I = F * t (N.s)."""
    return gaya * waktu


def impuls_dari_momentum(p_akhir, p_awal):
    """Impuls I = delta_p = p2 - p1."""
    return p_akhir - p_awal


def kecepatan_setelah_tumbukan_lenting_sempurna(m1, v1, m2, v2):
    """Tumbukan lenting sempurna (e=1), kembalikan (v1', v2')."""
    v1_akhir = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2_akhir = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return v1_akhir, v2_akhir


def kecepatan_setelah_tumbukan_tidak_lenting(m1, v1, m2, v2):
    """Tumbukan tidak lenting (e=0), benda menyatu: v' = (m1*v1 + m2*v2) / (m1+m2)."""
    return (m1 * v1 + m2 * v2) / (m1 + m2)


def koefisien_restitusi(v_pisah, v_dekati):
    """Koefisien restitusi e = |v_pisah| / |v_dekati|."""
    if v_dekati == 0:
        raise ZeroDivisionError("Kecepatan mendekati tidak boleh nol.")
    return abs(v_pisah / v_dekati)


def hukum_kekekalan_momentum(m1, v1, m2, v2):
    """Momentum awal = m1*v1 + m2*v2."""
    return m1 * v1 + m2 * v2
