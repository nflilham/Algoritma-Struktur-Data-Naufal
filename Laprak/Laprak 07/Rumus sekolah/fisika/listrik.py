"""Modul listrik: hukum Ohm dan rangkaian."""


def hukum_ohm_tegangan(arus, hambatan):
    """Hukum Ohm: V = I * R (Volt)."""
    return arus * hambatan


def hukum_ohm_arus(tegangan, hambatan):
    """Arus I = V / R (Ampere)."""
    if hambatan <= 0:
        raise ValueError("Hambatan harus positif.")
    return tegangan / hambatan


def hukum_ohm_hambatan(tegangan, arus):
    """Hambatan R = V / I (Ohm)."""
    if arus == 0:
        raise ZeroDivisionError("Arus tidak boleh nol.")
    return tegangan / arus


def hambatan_seri(*hambatan_list):
    """Hambatan seri Rs = R1 + R2 + ... + Rn."""
    return sum(hambatan_list)


def hambatan_paralel(*hambatan_list):
    """Hambatan paralel 1/Rp = 1/R1 + 1/R2 + ... + 1/Rn."""
    if any(r <= 0 for r in hambatan_list):
        raise ValueError("Semua hambatan harus positif.")
    return 1 / sum(1 / r for r in hambatan_list)


def daya_listrik(tegangan, arus):
    """Daya listrik P = V * I (Watt)."""
    return tegangan * arus


def daya_listrik_hambatan(tegangan, hambatan):
    """Daya P = V^2 / R (Watt)."""
    if hambatan <= 0:
        raise ValueError("Hambatan harus positif.")
    return (tegangan ** 2) / hambatan


def energi_listrik(daya, waktu):
    """Energi listrik W = P * t (Joule atau kWh jika t dalam jam)."""
    return daya * waktu


def muatan_listrik(arus, waktu):
    """Muatan Q = I * t (Coulomb)."""
    return arus * waktu


def kapasitor_seri(*kapasitansi_list):
    """Kapasitor seri 1/Cs = 1/C1 + 1/C2 + ... + 1/Cn."""
    if any(c <= 0 for c in kapasitansi_list):
        raise ValueError("Semua kapasitansi harus positif.")
    return 1 / sum(1 / c for c in kapasitansi_list)


def kapasitor_paralel(*kapasitansi_list):
    """Kapasitor paralel Cp = C1 + C2 + ... + Cn."""
    return sum(kapasitansi_list)


def energi_kapasitor(kapasitansi, tegangan):
    """Energi kapasitor E = 0.5 * C * V^2 (Joule)."""
    return 0.5 * kapasitansi * (tegangan ** 2)
