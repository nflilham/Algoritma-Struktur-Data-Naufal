"""Modul optik geometri: cermin dan lensa."""


def persamaan_cermin_lensa(f, s):
    """Persamaan cermin/lensa: 1/f = 1/s + 1/s', return s'."""
    if f == 0:
        raise ValueError("Fokus tidak boleh nol.")
    if s == 0:
        raise ValueError("Jarak benda tidak boleh nol.")
    return (f * s) / (s - f)


def perbesaran(jarak_bayangan, jarak_benda):
    """Perbesaran linear M = -s' / s."""
    if jarak_benda == 0:
        raise ValueError("Jarak benda tidak boleh nol.")
    return -jarak_bayangan / jarak_benda


def hukum_snellius(n1, sudut1_deg, n2):
    """Hukum Snellius pembiasan: n1*sin(theta1) = n2*sin(theta2), return theta2."""
    import math
    if n2 <= 0:
        raise ValueError("Indeks bias harus positif.")
    sudut1_rad = math.radians(sudut1_deg)
    sin_theta2 = (n1 * math.sin(sudut1_rad)) / n2
    if abs(sin_theta2) > 1:
        raise ValueError("Pembiasan total internal (sin > 1).")
    return math.degrees(math.asin(sin_theta2))


def sudut_kritis(n1, n2):
    """Sudut kritis pembiasan total: sin(theta_c) = n2/n1."""
    import math
    if n1 <= n2:
        raise ValueError("Tidak ada sudut kritis jika n1 <= n2.")
    return math.degrees(math.asin(n2 / n1))


def kekuatan_lensa(fokus_meter):
    """Kekuatan lensa P = 1 / f (dioptri)."""
    if fokus_meter == 0:
        raise ValueError("Fokus tidak boleh nol.")
    return 1 / fokus_meter
