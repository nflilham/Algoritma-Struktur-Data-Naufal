"""Modul kombinatorika dan teori peluang."""
import math


def permutasi(n, r):
    """Hitung permutasi nPr = n! / (n - r)!."""
    if r < 0 or r > n:
        raise ValueError("Nilai r harus memenuhi 0 <= r <= n.")
    return math.perm(n, r)


def kombinasi(n, r):
    """Hitung kombinasi nCr = n! / (r! * (n - r)!)."""
    if r < 0 or r > n:
        raise ValueError("Nilai r harus memenuhi 0 <= r <= n.")
    return math.comb(n, r)


def peluang_klasik(n_kejadian, n_semesta):
    """Peluang = n(A) / n(S)."""
    if n_semesta <= 0:
        raise ValueError("Ruang sampel harus bernilai positif.")
    if n_kejadian < 0 or n_kejadian > n_semesta:
        raise ValueError("Jumlah kejadian harus di antara 0 dan n(S).")
    return n_kejadian / n_semesta


def peluang_komplemen(peluang_a):
    """Peluang komplemen P(A') = 1 - P(A)."""
    if not 0 <= peluang_a <= 1:
        raise ValueError("Nilai peluang harus antara 0 dan 1.")
    return 1 - peluang_a


def frekuensi_harapan(peluang_a, banyak_percobaan):
    """Fh = P(A) * n percobaan."""
    if not 0 <= peluang_a <= 1:
        raise ValueError("Nilai peluang harus antara 0 dan 1.")
    if banyak_percobaan < 0:
        raise ValueError("Banyak percobaan tidak boleh negatif.")
    return peluang_a * banyak_percobaan


def permutasi_siklis(n):
    """Permutasi siklis untuk n objek: (n - 1)!."""
    if n <= 0:
        raise ValueError("Jumlah objek harus positif.")
    return math.factorial(n - 1)
