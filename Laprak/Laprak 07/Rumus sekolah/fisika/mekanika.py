"""Modul mekanika: momen inersia dan torsi."""
import math


def momen_inersia_partikel(massa, jarak):
    """Momen inersia partikel I = m * r^2 (kg.m^2)."""
    return massa * (jarak ** 2)


def momen_inersia_batang_pusat(massa, panjang):
    """Momen inersia batang homogen poros di tengah I = (1/12) * m * L^2."""
    return (1 / 12) * massa * (panjang ** 2)


def momen_inersia_batang_ujung(massa, panjang):
    """Momen inersia batang homogen poros di ujung I = (1/3) * m * L^2."""
    return (1 / 3) * massa * (panjang ** 2)


def momen_inersia_silinder_pejal(massa, jari_jari):
    """Momen inersia silinder pejal poros di pusat I = (1/2) * m * r^2."""
    return 0.5 * massa * (jari_jari ** 2)


def momen_inersia_bola_pejal(massa, jari_jari):
    """Momen inersia bola pejal I = (2/5) * m * r^2."""
    return (2 / 5) * massa * (jari_jari ** 2)


def torsi(gaya, lengan, sudut_deg=90):
    """Torsi tau = F * r * sin(theta) (N.m)."""
    sudut_rad = math.radians(sudut_deg)
    return gaya * lengan * math.sin(sudut_rad)


def hukum_newton_rotasi(momen_inersia, percepatan_sudut):
    """Torsi tau = I * alpha (N.m)."""
    return momen_inersia * percepatan_sudut


def momentum_sudut(momen_inersia, kecepatan_sudut):
    """Momentum sudut L = I * omega (kg.m^2/s)."""
    return momen_inersia * kecepatan_sudut


def kesetimbangan_torsi(*torsi_list):
    """Syarat kesetimbangan rotasi: sum(torsi) = 0."""
    return sum(torsi_list)


def energi_kinetik_rotasi(momen_inersia, kecepatan_sudut):
    """Energi kinetik rotasi Ek = 0.5 * I * omega^2 (Joule)."""
    return 0.5 * momen_inersia * (kecepatan_sudut ** 2)
