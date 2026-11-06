"""Modul aljabar: fungsi linier dan kuadrat."""
import math


def diskriminan(a, b, c):
    """Hitung nilai diskriminan D = b^2 - 4ac."""
    return b ** 2 - 4 * a * c


def akar_persamaan_kuadrat(a, b, c):
    """Cari akar persamaan kuadrat ax^2 + bx + c = 0."""
    if a == 0:
        raise ValueError("Nilai a tidak boleh nol pada persamaan kuadrat.")
    d = diskriminan(a, b, c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x, x
    else:
        riil = -b / (2 * a)
        imajiner = math.sqrt(-d) / (2 * a)
        return complex(riil, imajiner), complex(riil, -imajiner)


def titik_puncak_parabola(a, b, c):
    """Kembalikan tuple (xp, yp) titik puncak parabola."""
    if a == 0:
        raise ValueError("Nilai a tidak boleh nol.")
    xp = -b / (2 * a)
    yp = -diskriminan(a, b, c) / (4 * a)
    return xp, yp


def gradien_dua_titik(x1, y1, x2, y2):
    """Hitung gradien m dari dua titik: (y2 - y1) / (x2 - x1)."""
    if x2 == x1:
        raise ZeroDivisionError("Garis vertikal tidak memiliki gradien terdefinisi.")
    return (y2 - y1) / (x2 - x1)


def persamaan_linear_1_variabel(a, b):
    """Selesaikan persamaan linear ax + b = 0 -> x = -b/a."""
    if a == 0:
        raise ValueError("Nilai a tidak boleh nol.")
    return -b / a


def spldv_cramer(a1, b1, c1, a2, b2, c2):
    """Selesaikan SPLDV a1*x + b1*y = c1 dan a2*x + b2*y = c2."""
    det_utama = a1 * b2 - a2 * b1
    if det_utama == 0:
        raise ValueError("Sistem persamaan tidak punya solusi unik (D = 0).")
    det_x = c1 * b2 - c2 * b1
    det_y = a1 * c2 - a2 * c1
    return det_x / det_utama, det_y / det_utama
