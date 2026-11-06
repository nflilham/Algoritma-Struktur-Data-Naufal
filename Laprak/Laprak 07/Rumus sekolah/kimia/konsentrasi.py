"""Modul konsentrasi larutan."""


def molaritas(mol_zat_terlarut, volume_liter):
    """Molaritas M = n / V (mol/L)."""
    if volume_liter <= 0:
        raise ValueError("Volume harus positif.")
    return mol_zat_terlarut / volume_liter


def molalitas(mol_zat_terlarut, massa_pelarut_kg):
    """Molalitas m = n / p (mol/kg)."""
    if massa_pelarut_kg <= 0:
        raise ValueError("Massa pelarut harus positif.")
    return mol_zat_terlarut / massa_pelarut_kg


def persen_massa(massa_terlarut, massa_larutan):
    """Persen massa (%m/m) = (m_terlarut / m_larutan) * 100."""
    if massa_larutan <= 0:
        raise ValueError("Massa larutan harus positif.")
    return (massa_terlarut / massa_larutan) * 100


def ppm(massa_terlarut_mg, volume_larutan_liter):
    """Konsentrasi ppm = mg/L (mg zat terlarut per liter larutan)."""
    if volume_larutan_liter <= 0:
        raise ValueError("Volume harus positif.")
    return massa_terlarut_mg / volume_larutan_liter


def pengenceran(m1, v1, v2):
    """Hitung konsentrasi setelah pengenceran M2 = M1*V1/V2."""
    if v2 <= 0:
        raise ValueError("Volume akhir harus positif.")
    if v2 < v1:
        raise ValueError("Volume akhir pengenceran harus >= volume awal.")
    return (m1 * v1) / v2
