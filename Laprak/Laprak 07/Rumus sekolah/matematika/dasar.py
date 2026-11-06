"""Modul operasi matematika dasar."""
import math


def tambah(a, b):
    """Jumlahkan dua bilangan."""
    return a + b


def kurang(a, b):
    """Kurangkan bilangan a dengan b."""
    return a - b


def kali(a, b):
    """Kalikan dua bilangan."""
    return a * b


def bagi(a, b):
    """Bagi bilangan a dengan b."""
    if b == 0:
        raise ZeroDivisionError("Pembagi tidak boleh nol.")
    return a / b


def bagi_bulat(a, b):
    """Pembagian bulat a dengan b."""
    if b == 0:
        raise ZeroDivisionError("Pembagi tidak boleh nol.")
    return a // b


def modulo(a, b):
    """Sisa hasil bagi a dibagi b."""
    if b == 0:
        raise ZeroDivisionError("Pembagi tidak boleh nol.")
    return a % b


def pangkat(bilangan, eksponen):
    """Hitung pangkat bilangan."""
    return bilangan ** eksponen


def akar_kuadrat(bilangan):
    """Hitung akar kuadrat bilangan."""
    if bilangan < 0:
        raise ValueError("Bilangan negatif tidak punya akar riil.")
    return math.sqrt(bilangan)


def akar_n(bilangan, n):
    """Hitung akar pangkat n bilangan."""
    if n == 0:
        raise ZeroDivisionError("Derajat akar n tidak boleh nol.")
    if bilangan < 0 and n % 2 == 0:
        raise ValueError("Akar genap bilangan negatif bukan bilangan riil.")
    return bilangan ** (1 / n)


def faktorial(n):
    """Hitung n faktorial (n!)."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Faktorial hanya untuk bilangan bulat tak-negatif.")
    return math.factorial(n)


def nilai_mutlak(bilangan):
    """Kembalikan nilai mutlak suatu bilangan."""
    return abs(bilangan)
