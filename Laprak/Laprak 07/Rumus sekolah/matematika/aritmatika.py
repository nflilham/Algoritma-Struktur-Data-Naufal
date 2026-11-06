"""Modul aritmatika dan teori bilangan sekolah."""
import math


def fpb(a, b):
    """Faktor Persekutuan Terbesar dua bilangan."""
    return math.gcd(int(a), int(b))


def kpk(a, b):
    """Kelipatan Persekutuan Terkecil dua bilangan."""
    a, b = int(a), int(b)
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)


def is_prima(n):
    """Cek apakah bilangan prima."""
    if not isinstance(n, int) or n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def daftar_prima(sampai):
    """Hasilkan list bilangan prima hingga batas tertentu."""
    return [x for x in range(2, int(sampai) + 1) if is_prima(x)]


def faktor_bilangan(n):
    """Cari semua faktor pembagi dari n."""
    n = abs(int(n))
    faktor = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            faktor.add(i)
            faktor.add(n // i)
    return sorted(faktor)


def fibonacci(n):
    """Hasilkan n suku pertama deret Fibonacci."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    deret = [0, 1]
    while len(deret) < n:
        deret.append(deret[-1] + deret[-2])
    return deret


def desimal_ke_biner(n):
    """Konversi bilangan bulat desimal ke string biner."""
    return bin(int(n))[2:]


def desimal_ke_heksadesimal(n):
    """Konversi bilangan bulat desimal ke string heksadesimal."""
    return hex(int(n))[2:].upper()


def desimal_ke_oktal(n):
    """Konversi bilangan bulat desimal ke string oktal."""
    return oct(int(n))[2:]
