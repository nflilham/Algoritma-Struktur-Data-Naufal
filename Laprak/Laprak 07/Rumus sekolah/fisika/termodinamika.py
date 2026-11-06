"""Modul termodinamika: kalor dan gas ideal."""


def kalor(massa, kalor_jenis, delta_suhu):
    """Kalor Q = m * c * delta_T (Joule)."""
    return massa * kalor_jenis * delta_suhu


def kapasitas_kalor(massa, kalor_jenis):
    """Kapasitas kalor C = m * c (J/K)."""
    return massa * kalor_jenis


def kalor_lebur(massa, kalor_lebur_zat):
    """Kalor lebur Q = m * L (Joule)."""
    return massa * kalor_lebur_zat


def kalor_uap(massa, kalor_uap_zat):
    """Kalor uap Q = m * U (Joule)."""
    return massa * kalor_uap_zat


def asas_black(q_lepas, q_terima):
    """Asas Black: Q_lepas = Q_terima."""
    return abs(q_lepas - q_terima) < 1e-6


def pemuaian_panjang(panjang_awal, koef_muai, delta_suhu):
    """Pemuaian panjang delta_L = L0 * alpha * delta_T."""
    return panjang_awal * koef_muai * delta_suhu


def pemuaian_volume(volume_awal, koef_muai_volume, delta_suhu):
    """Pemuaian volume delta_V = V0 * gamma * delta_T."""
    return volume_awal * koef_muai_volume * delta_suhu


def hukum_gas_ideal(tekanan, volume, n_mol, R=8.314, suhu_kelvin=None):
    """Hukum gas ideal PV = nRT, return T jika None."""
    if suhu_kelvin is None:
        if n_mol <= 0 or R <= 0:
            raise ValueError("n dan R harus positif.")
        return (tekanan * volume) / (n_mol * R)
    return tekanan * volume - n_mol * R * suhu_kelvin


def usaha_gas(tekanan, delta_volume):
    """Usaha gas W = P * delta_V (Joule)."""
    return tekanan * delta_volume


def hukum_1_termodinamika(delta_u, usaha):
    """Hukum I termodinamika: Q = delta_U + W."""
    return delta_u + usaha


def efisiensi_mesin_carnot(suhu_tinggi_kelvin, suhu_rendah_kelvin):
    """Efisiensi mesin Carnot eta = 1 - (Tr / Tt) * 100%."""
    if suhu_tinggi_kelvin <= 0 or suhu_rendah_kelvin <= 0:
        raise ValueError("Suhu harus dalam Kelvin (positif).")
    if suhu_rendah_kelvin >= suhu_tinggi_kelvin:
        raise ValueError("Suhu tinggi harus lebih besar dari suhu rendah.")
    return (1 - suhu_rendah_kelvin / suhu_tinggi_kelvin) * 100
