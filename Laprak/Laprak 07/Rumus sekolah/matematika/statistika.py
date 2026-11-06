"""Modul statistika deskriptif data tunggal."""
import math
from collections import Counter


def mean(data):
    """Hitung rata-rata hitung (mean) data."""
    if not data:
        raise ValueError("Data tidak boleh kosong.")
    return sum(data) / len(data)


def median(data):
    """Hitung nilai tengah (median) data."""
    if not data:
        raise ValueError("Data tidak boleh kosong.")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def modus(data):
    """Cari modus (nilai yang paling sering muncul)."""
    if not data:
        raise ValueError("Data tidak boleh kosong.")
    counts = Counter(data)
    max_count = max(counts.values())
    modi = [val for val, count in counts.items() if count == max_count]
    return modi


def jangkauan(data):
    """Jangkauan (range) = nilai maksimum - nilai minimum."""
    if not data:
        raise ValueError("Data tidak boleh kosong.")
    return max(data) - min(data)


def varians_populasi(data):
    """Hitung varians populasi data."""
    if not data:
        raise ValueError("Data tidak boleh kosong.")
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def varians_sampel(data):
    """Hitung varians sampel data (n-1)."""
    if len(data) < 2:
        raise ValueError("Varians sampel butuh minimal 2 data.")
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - 1)


def standar_deviasi_populasi(data):
    """Hitung simpangan baku populasi."""
    return math.sqrt(varians_populasi(data))


def standar_deviasi_sampel(data):
    """Hitung simpangan baku sampel."""
    return math.sqrt(varians_sampel(data))


def kuartil(data):
    """Kembalikan tuple (Q1, Q2, Q3) data tunggal."""
    if len(data) < 4:
        raise ValueError("Data minimal berjumlah 4 untuk hitung kuartil.")
    sorted_d = sorted(data)
    n = len(sorted_d)
    q2 = median(sorted_d)
    if n % 2 == 0:
        bawah = sorted_d[:n // 2]
        atas = sorted_d[n // 2:]
    else:
        bawah = sorted_d[:n // 2]
        atas = sorted_d[n // 2 + 1:]
    q1 = median(bawah)
    q3 = median(atas)
    return q1, q2, q3
