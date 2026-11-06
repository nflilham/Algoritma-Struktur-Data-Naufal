"""Modul stoikiometri reaksi kimia."""


def persen_massa_unsur(ar_unsur, jumlah_atom, mr_senyawa):
    """Persen massa unsur dalam senyawa: (Ar * jumlah / Mr) * 100."""
    if mr_senyawa <= 0:
        raise ValueError("Mr senyawa harus positif.")
    return (ar_unsur * jumlah_atom / mr_senyawa) * 100


def perbandingan_mol(mol1, mol2):
    """Perbandingan mol dua zat = mol1 / mol2."""
    if mol2 == 0:
        raise ZeroDivisionError("Mol pembanding tidak boleh nol.")
    return mol1 / mol2


def massa_ekuivalen(mr, valensi):
    """Massa ekuivalen = Mr / valensi."""
    if valensi <= 0:
        raise ValueError("Valensi harus positif.")
    return mr / valensi


def pereaksi_pembatas(mol_a, koef_a, mol_b, koef_b):
    """Tentukan pereaksi pembatas dari dua reaktan, kembalikan 'A' atau 'B'."""
    if koef_a <= 0 or koef_b <= 0:
        raise ValueError("Koefisien reaksi harus positif.")
    rasio_a = mol_a / koef_a
    rasio_b = mol_b / koef_b
    return "A" if rasio_a <= rasio_b else "B"


def hasil_teori(mol_pereaksi, koef_pereaksi, koef_produk, mr_produk):
    """Hitung massa produk teoritis dari pereaksi pembatas."""
    mol_produk = (mol_pereaksi / koef_pereaksi) * koef_produk
    return mol_produk * mr_produk


def rendemen(hasil_nyata, hasil_teoritis):
    """Rendemen reaksi (%) = (hasil nyata / hasil teoritis) * 100."""
    if hasil_teoritis <= 0:
        raise ValueError("Hasil teoritis harus positif.")
    return (hasil_nyata / hasil_teoritis) * 100
