"""Fungsi logaritma dan sifat-sifatnya."""
import math


def logaritma(x, basis=10):
    """Logaritma x dengan basis tertentu (default 10)."""
    if x <= 0:
        raise ValueError("x harus positif")
    if basis <= 0 or basis == 1:
        raise ValueError("Basis harus positif dan tidak sama dengan 1")
    return math.log(x, basis)


def logaritma_natural(x):
    """Logaritma natural (ln) dari x."""
    if x <= 0:
        raise ValueError("x harus positif")
    return math.log(x)


def logaritma_basis_10(x):
    """Logaritma basis 10 (log10) dari x."""
    if x <= 0:
        raise ValueError("x harus positif")
    return math.log10(x)


def sifat_log_perkalian(a, b, basis=10):
    """log(a*b) = log(a) + log(b)."""
    return logaritma(a, basis) + logaritma(b, basis)


def sifat_log_pembagian(a, b, basis=10):
    """log(a/b) = log(a) - log(b)."""
    return logaritma(a, basis) - logaritma(b, basis)


def sifat_log_pangkat(a, n, basis=10):
    """log(a^n) = n * log(a)."""
    return n * logaritma(a, basis)
