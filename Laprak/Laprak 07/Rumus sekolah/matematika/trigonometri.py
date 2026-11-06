"""Modul trigonometri derajat dan sudut."""
import math


def derajat_ke_radian(derajat):
    """Konversi sudut derajat ke radian."""
    return math.radians(derajat)


def radian_ke_derajat(radian):
    """Konversi sudut radian ke derajat."""
    return math.degrees(radian)


def sin_deg(derajat):
    """Hitung sinus dari sudut derajat."""
    return math.sin(math.radians(derajat))


def cos_deg(derajat):
    """Hitung kosinus dari sudut derajat."""
    return math.cos(math.radians(derajat))


def tan_deg(derajat):
    """Hitung tangen dari sudut derajat."""
    if (derajat - 90) % 180 == 0:
        raise ValueError("Tangen 90 + k*180 tidak terdefinisi.")
    return math.tan(math.radians(derajat))


def csc_deg(derajat):
    """Hitung cosecan sudut derajat (1/sin)."""
    s = sin_deg(derajat)
    if abs(s) < 1e-12:
        raise ValueError("Cosecan tidak terdefinisi saat sinus bernilai 0.")
    return 1 / s


def sec_deg(derajat):
    """Hitung secan sudut derajat (1/cos)."""
    c = cos_deg(derajat)
    if abs(c) < 1e-12:
        raise ValueError("Secan tidak terdefinisi saat kosinus bernilai 0.")
    return 1 / c


def cot_deg(derajat):
    """Hitung cotangen sudut derajat (1/tan)."""
    t = tan_deg(derajat)
    if abs(t) < 1e-12:
        raise ValueError("Cotangen tidak terdefinisi saat tangen bernilai 0.")
    return 1 / t


def aturan_sinus_sisi(a, sudut_A_deg, sudut_B_deg):
    """Aturan sinus: b = a * sin(B) / sin(A)."""
    sin_a = sin_deg(sudut_A_deg)
    if abs(sin_a) < 1e-12:
        raise ValueError("Sudut A tidak boleh kelipatan 180.")
    return a * sin_deg(sudut_B_deg) / sin_a


def aturan_cosinus_sisi(b, c, sudut_A_deg):
    """Aturan cosinus: a = sqrt(b^2 + c^2 - 2bc*cos(A))."""
    nilai = b ** 2 + c ** 2 - 2 * b * c * cos_deg(sudut_A_deg)
    if nilai < 0:
        raise ValueError("Kombinasi sisi dan sudut tidak membentuk segitiga valid.")
    return math.sqrt(nilai)
