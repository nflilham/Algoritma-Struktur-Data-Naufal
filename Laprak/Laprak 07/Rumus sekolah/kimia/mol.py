"""Modul konsep mol dan partikel."""

BILANGAN_AVOGADRO = 6.022e23  # partikel/mol


def gram_ke_mol(massa_gram, mr):
    """Hitung mol dari massa zat: n = m / Mr."""
    if mr <= 0:
        raise ValueError("Mr harus bernilai positif.")
    return massa_gram / mr


def mol_ke_gram(mol, mr):
    """Hitung massa zat dari mol: m = n * Mr."""
    if mr <= 0:
        raise ValueError("Mr harus bernilai positif.")
    return mol * mr


def mol_ke_partikel(mol):
    """Hitung jumlah partikel dari mol: N = n * NA."""
    return mol * BILANGAN_AVOGADRO


def partikel_ke_mol(partikel):
    """Hitung mol dari jumlah partikel: n = N / NA."""
    return partikel / BILANGAN_AVOGADRO


def volume_gas_stp(mol):
    """Volume gas pada STP (0°C, 1 atm) = n * 22.4 L."""
    return mol * 22.4


def mol_dari_volume_stp(volume_liter):
    """Hitung mol dari volume gas di STP: n = V / 22.4."""
    return volume_liter / 22.4
