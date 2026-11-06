"""Modul operasi matriks 2x2 sederhana."""


def tambah_matriks_2x2(m1, m2):
    """Penjumlahan dua matriks 2x2: [[a,b],[c,d]]."""
    return [
        [m1[0][0] + m2[0][0], m1[0][1] + m2[0][1]],
        [m1[1][0] + m2[1][0], m1[1][1] + m2[1][1]],
    ]


def kurang_matriks_2x2(m1, m2):
    """Pengurangan dua matriks 2x2."""
    return [
        [m1[0][0] - m2[0][0], m1[0][1] - m2[0][1]],
        [m1[1][0] - m2[1][0], m1[1][1] - m2[1][1]],
    ]


def kali_skalar_matriks(k, m):
    """Kalikan matriks 2x2 dengan skalar k."""
    return [
        [k * m[0][0], k * m[0][1]],
        [k * m[1][0], k * m[1][1]],
    ]


def kali_matriks_2x2(m1, m2):
    """Perkalian dua matriks 2x2."""
    return [
        [
            m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0],
            m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1],
        ],
        [
            m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0],
            m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1],
        ],
    ]


def determinan_2x2(m):
    """Determinan matriks 2x2: ad - bc."""
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def transpose_2x2(m):
    """Transpose matriks 2x2."""
    return [
        [m[0][0], m[1][0]],
        [m[0][1], m[1][1]],
    ]


def invers_2x2(m):
    """Invers matriks 2x2 = (1/det) * adj(m)."""
    det = determinan_2x2(m)
    if det == 0:
        raise ValueError("Matriks singular (determinan = 0), tidak punya invers.")
    return [
        [m[1][1] / det, -m[0][1] / det],
        [-m[1][0] / det, m[0][0] / det],
    ]
