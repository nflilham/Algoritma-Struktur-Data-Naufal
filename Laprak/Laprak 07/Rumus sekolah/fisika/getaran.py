"""Modul getaran harmonik."""
import math


def periode_dari_frekuensi(frekuensi):
    """Periode T = 1 / f (detik)."""
    if frekuensi <= 0:
        raise ValueError("Frekuensi harus positif.")
    return 1 / frekuensi


def frekuensi_dari_periode(periode):
    """Frekuensi f = 1 / T (Hz)."""
    if periode <= 0:
        raise ValueError("Periode harus positif.")
    return 1 / periode


def periode_pegas(massa, konstanta_pegas):
    """Periode getaran pegas T = 2*pi*sqrt(m/k)."""
    if massa <= 0 or konstanta_pegas <= 0:
        raise ValueError("Massa dan konstanta pegas harus positif.")
    return 2 * math.pi * math.sqrt(massa / konstanta_pegas)


def periode_bandul(panjang, g=9.8):
    """Periode bandul sederhana T = 2*pi*sqrt(L/g)."""
    if panjang <= 0:
        raise ValueError("Panjang tali harus positif.")
    return 2 * math.pi * math.sqrt(panjang / g)


def simpangan(amplitudo, omega, t, fase=0):
    """Simpangan getaran y = A * sin(omega*t + fase)."""
    return amplitudo * math.sin(omega * t + fase)


def kecepatan_getaran(amplitudo, omega, t, fase=0):
    """Kecepatan getaran v = A*omega*cos(omega*t + fase)."""
    return amplitudo * omega * math.cos(omega * t + fase)


def energi_getaran(konstanta_pegas, amplitudo):
    """Energi total getaran E = 0.5 * k * A^2 (Joule)."""
    return 0.5 * konstanta_pegas * (amplitudo ** 2)
