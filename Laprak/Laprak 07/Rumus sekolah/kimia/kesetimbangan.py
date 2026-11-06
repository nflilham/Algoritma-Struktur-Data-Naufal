"""Modul kesetimbangan kimia."""
import math


def konstanta_kc(konsentrasi_produk_list, koef_produk_list, konsentrasi_reaktan_list, koef_reaktan_list):
    """Hitung Kc = [produk]^koef / [reaktan]^koef."""
    produk_term = 1
    for c, k in zip(konsentrasi_produk_list, koef_produk_list):
        produk_term *= c ** k
    reaktan_term = 1
    for c, k in zip(konsentrasi_reaktan_list, koef_reaktan_list):
        reaktan_term *= c ** k
    if reaktan_term == 0:
        raise ZeroDivisionError("Konsentrasi reaktan tidak boleh nol.")
    return produk_term / reaktan_term


def konstanta_kp(tekanan_produk_list, koef_produk_list, tekanan_reaktan_list, koef_reaktan_list):
    """Hitung Kp = (P produk)^koef / (P reaktan)^koef."""
    produk_term = 1
    for p, k in zip(tekanan_produk_list, koef_produk_list):
        produk_term *= p ** k
    reaktan_term = 1
    for p, k in zip(tekanan_reaktan_list, koef_reaktan_list):
        reaktan_term *= p ** k
    if reaktan_term == 0:
        raise ZeroDivisionError("Tekanan reaktan tidak boleh nol.")
    return produk_term / reaktan_term


def hubungan_kp_kc(kc, delta_n, R, T):
    """Kp = Kc * (RT)^(delta_n), delta_n = mol produk gas - mol reaktan gas."""
    return kc * (R * T) ** delta_n


def derajat_disosiasi(mol_terdisosiasi, mol_awal):
    """Alpha = n terdisosiasi / n awal."""
    if mol_awal <= 0:
        raise ValueError("Mol awal harus positif.")
    if mol_terdisosiasi < 0 or mol_terdisosiasi > mol_awal:
        raise ValueError("Mol terdisosiasi tidak valid.")
    return mol_terdisosiasi / mol_awal
