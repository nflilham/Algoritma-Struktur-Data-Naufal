"""Modul sifat koligatif larutan."""


def kenaikan_titik_didih(kb, molalitas):
    """Delta_Tb = Kb * m (kenaikan titik didih larutan)."""
    return kb * molalitas


def penurunan_titik_beku(kf, molalitas):
    """Delta_Tf = Kf * m (penurunan titik beku larutan)."""
    return kf * molalitas


def tekanan_osmotik(molaritas, suhu_kelvin, R=0.082):
    """Tekanan osmotik pi = M * R * T (atm)."""
    if suhu_kelvin <= 0:
        raise ValueError("Suhu Kelvin harus positif.")
    return molaritas * R * suhu_kelvin


def penurunan_tekanan_uap(fraksi_mol_terlarut, tekanan_jenuh_pelarut):
    """Delta_P = x_terlarut * P*_pelarut (penurunan tekanan uap)."""
    if not 0 <= fraksi_mol_terlarut <= 1:
        raise ValueError("Fraksi mol harus antara 0 dan 1.")
    return fraksi_mol_terlarut * tekanan_jenuh_pelarut


def titik_didih_larutan(titik_didih_pelarut, delta_tb):
    """Titik didih larutan = titik didih pelarut + delta Tb."""
    return titik_didih_pelarut + delta_tb


def titik_beku_larutan(titik_beku_pelarut, delta_tf):
    """Titik beku larutan = titik beku pelarut - delta Tf."""
    return titik_beku_pelarut - delta_tf
