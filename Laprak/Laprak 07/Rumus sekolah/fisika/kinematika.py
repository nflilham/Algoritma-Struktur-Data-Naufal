"""Modul kinematika: gerak lurus dan parabola."""
import math


def kecepatan(jarak, waktu):
    """Kecepatan v = s / t (m/s)."""
    if waktu <= 0:
        raise ValueError("Waktu harus positif.")
    return jarak / waktu


def percepatan(perubahan_kecepatan, waktu):
    """Percepatan a = delta_v / t (m/s^2)."""
    if waktu <= 0:
        raise ValueError("Waktu harus positif.")
    return perubahan_kecepatan / waktu


def glb_jarak(kecepatan, waktu):
    """GLB: s = v * t."""
    return kecepatan * waktu


def glbb_jarak(v0, a, t):
    """GLBB: s = v0*t + 0.5*a*t^2."""
    return v0 * t + 0.5 * a * (t ** 2)


def glbb_kecepatan(v0, a, t):
    """GLBB: vt = v0 + a*t."""
    return v0 + a * t


def glbb_kecepatan_kuadrat(v0, a, s):
    """GLBB: vt^2 = v0^2 + 2*a*s."""
    nilai = v0 ** 2 + 2 * a * s
    if nilai < 0:
        raise ValueError("Nilai di bawah akar negatif, gerak tidak fisik.")
    return math.sqrt(nilai)


def gerak_jatuh_bebas_jarak(waktu, g=9.8):
    """GJB: h = 0.5 * g * t^2."""
    return 0.5 * g * (waktu ** 2)


def gerak_jatuh_bebas_kecepatan(waktu, g=9.8):
    """GJB: v = g * t."""
    return g * waktu


def gerak_vertikal_ke_atas_tinggi_max(v0, g=9.8):
    """Tinggi maksimum: h_max = v0^2 / (2*g)."""
    return (v0 ** 2) / (2 * g)


def gerak_parabola_jarak_mendatar(v0, sudut_deg, g=9.8):
    """Jarak mendatar X = v0^2 * sin(2*theta) / g."""
    sudut_rad = math.radians(sudut_deg)
    return (v0 ** 2) * math.sin(2 * sudut_rad) / g


def gerak_parabola_tinggi_max(v0, sudut_deg, g=9.8):
    """Tinggi maksimum parabola: h = (v0*sin(theta))^2 / (2*g)."""
    sudut_rad = math.radians(sudut_deg)
    vy = v0 * math.sin(sudut_rad)
    return (vy ** 2) / (2 * g)
