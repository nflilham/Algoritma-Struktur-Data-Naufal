"""Modul rumus barisan dan deret aritmatika & geometri."""


def suku_ke_n_aritmatika(a, b, n):
    """Suku ke-n aritmatika: Un = a + (n - 1) * b."""
    if n <= 0:
        raise ValueError("Indeks suku n harus bilangan bulat positif.")
    return a + (n - 1) * b


def jumlah_n_aritmatika(a, b, n):
    """Jumlah n suku pertama aritmatika: Sn = (n / 2) * (2a + (n - 1) * b)."""
    if n <= 0:
        raise ValueError("Jumlah suku n harus positif.")
    return (n / 2) * (2 * a + (n - 1) * b)


def suku_ke_n_geometri(a, r, n):
    """Suku ke-n geometri: Un = a * r^(n - 1)."""
    if n <= 0:
        raise ValueError("Indeks suku n harus bilangan bulat positif.")
    return a * (r ** (n - 1))


def jumlah_n_geometri(a, r, n):
    """Jumlah n suku pertama geometri: Sn."""
    if n <= 0:
        raise ValueError("Jumlah suku n harus positif.")
    if r == 1:
        return a * n
    return a * (1 - r ** n) / (1 - r)


def jumlah_deret_tak_hingga(a, r):
    """Jumlah deret geometri tak hingga konvergen (|r| < 1): S_inf = a / (1 - r)."""
    if abs(r) >= 1:
        raise ValueError("Deret divergen, rasio |r| harus kurang dari 1.")
    return a / (1 - r)


def beda_aritmatika(u_awal, u_akhir, n):
    """Beda b = (Un - U1) / (n - 1)."""
    if n <= 1:
        raise ValueError("Nilai n harus lebih dari 1.")
    return (u_akhir - u_awal) / (n - 1)
