"""Modul konversi suhu antar skala."""


def celsius_ke_fahrenheit(c):
    """Konversi Celsius ke Fahrenheit: F = (9/5)C + 32."""
    return (9 / 5) * c + 32


def celsius_ke_kelvin(c):
    """Konversi Celsius ke Kelvin: K = C + 273.15."""
    return c + 273.15


def celsius_ke_reamur(c):
    """Konversi Celsius ke Reamur: R = (4/5)C."""
    return (4 / 5) * c


def fahrenheit_ke_celsius(f):
    """Konversi Fahrenheit ke Celsius: C = (5/9)(F - 32)."""
    return (5 / 9) * (f - 32)


def kelvin_ke_celsius(k):
    """Konversi Kelvin ke Celsius: C = K - 273.15."""
    if k < 0:
        raise ValueError("Suhu Kelvin tidak boleh negatif.")
    return k - 273.15


def reamur_ke_celsius(r):
    """Konversi Reamur ke Celsius: C = (5/4)R."""
    return (5 / 4) * r
