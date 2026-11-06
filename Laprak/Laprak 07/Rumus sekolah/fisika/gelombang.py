"""Modul gelombang mekanik."""
import math


def cepat_rambat_gelombang(frekuensi, panjang_gelombang):
    """Cepat rambat v = f * lambda (m/s)."""
    return frekuensi * panjang_gelombang


def panjang_gelombang(cepat_rambat, frekuensi):
    """Panjang gelombang lambda = v / f (m)."""
    if frekuensi <= 0:
        raise ValueError("Frekuensi harus positif.")
    return cepat_rambat / frekuensi


def frekuensi_gelombang(cepat_rambat, panjang_gelombang):
    """Frekuensi f = v / lambda (Hz)."""
    if panjang_gelombang <= 0:
        raise ValueError("Panjang gelombang harus positif.")
    return cepat_rambat / panjang_gelombang


def intensitas_gelombang(daya, luas):
    """Intensitas I = P / A (W/m^2)."""
    if luas <= 0:
        raise ValueError("Luas penampang harus positif.")
    return daya / luas


def taraf_intensitas_bunyi(intensitas, i0=1e-12):
    """Taraf intensitas TI = 10 * log10(I / I0) (dB)."""
    if intensitas <= 0 or i0 <= 0:
        raise ValueError("Intensitas harus positif.")
    return 10 * math.log10(intensitas / i0)


def efek_doppler_sumber_bergerak(f0, vs, v_bunyi, mendekati=True):
    """Efek Doppler sumber bergerak: f' = f0 * v / (v +/- vs)."""
    if mendekati:
        return f0 * v_bunyi / (v_bunyi - vs)
    else:
        return f0 * v_bunyi / (v_bunyi + vs)


def efek_doppler_pengamat_bergerak(f0, vp, v_bunyi, mendekati=True):
    """Efek Doppler pengamat bergerak: f' = f0 * (v +/- vp) / v."""
    if mendekati:
        return f0 * (v_bunyi + vp) / v_bunyi
    else:
        return f0 * (v_bunyi - vp) / v_bunyi
