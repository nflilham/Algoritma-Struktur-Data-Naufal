"""Modul gravitasi Newton dan gerak orbit."""
import math


def gaya_gravitasi(m1, m2, jarak, G=6.674e-11):
    """Gaya gravitasi Newton F = G * m1 * m2 / r^2 (N)."""
    if jarak <= 0:
        raise ValueError("Jarak harus positif.")
    return G * m1 * m2 / (jarak ** 2)


def percepatan_gravitasi(massa_planet, jarak, G=6.674e-11):
    """Percepatan gravitasi g = G * M / r^2 (m/s^2)."""
    if jarak <= 0:
        raise ValueError("Jarak harus positif.")
    return G * massa_planet / (jarak ** 2)


def energi_potensial_gravitasi(m1, m2, jarak, G=6.674e-11):
    """Energi potensial gravitasi U = -G * m1 * m2 / r (Joule)."""
    if jarak <= 0:
        raise ValueError("Jarak harus positif.")
    return -G * m1 * m2 / jarak


def kecepatan_orbit(massa_pusat, jari_jari_orbit, G=6.674e-11):
    """Kecepatan orbit satelit v = sqrt(G * M / r) (m/s)."""
    if jari_jari_orbit <= 0:
        raise ValueError("Jari-jari orbit harus positif.")
    return math.sqrt(G * massa_pusat / jari_jari_orbit)


def periode_orbit(jari_jari_orbit, massa_pusat, G=6.674e-11):
    """Periode orbit T = 2*pi*sqrt(r^3 / (G*M)) (detik)."""
    if jari_jari_orbit <= 0 or massa_pusat <= 0:
        raise ValueError("Jari-jari dan massa harus positif.")
    return 2 * math.pi * math.sqrt((jari_jari_orbit ** 3) / (G * massa_pusat))


def hukum_kepler_3(T, a):
    """Hukum Kepler III: T^2 / a^3 = konstanta."""
    if a <= 0:
        raise ValueError("Sumbu semi-mayor harus positif.")
    return (T ** 2) / (a ** 3)
