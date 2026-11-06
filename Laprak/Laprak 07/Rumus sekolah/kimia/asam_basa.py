"""Modul asam basa dan pH."""
import math


def ph_dari_h(konsentrasi_h):
    """Hitung pH = -log10([H+])."""
    if konsentrasi_h <= 0:
        raise ValueError("Konsentrasi [H+] harus positif.")
    return -math.log10(konsentrasi_h)


def poh_dari_oh(konsentrasi_oh):
    """Hitung pOH = -log10([OH-])."""
    if konsentrasi_oh <= 0:
        raise ValueError("Konsentrasi [OH-] harus positif.")
    return -math.log10(konsentrasi_oh)


def ph_ke_poh(ph, suhu_25=True):
    """pOH = 14 - pH pada suhu 25°C."""
    return 14 - ph


def ph_asam_kuat(molaritas, valensi=1):
    """pH asam kuat = -log10(M * valensi)."""
    h = molaritas * valensi
    return ph_dari_h(h)


def ph_basa_kuat(molaritas, valensi=1):
    """pH basa kuat via pOH = -log10(M * valensi), lalu pH = 14 - pOH."""
    oh = molaritas * valensi
    poh = poh_dari_oh(oh)
    return 14 - poh


def ph_asam_lemah(ka, molaritas):
    """pH asam lemah = -log10(sqrt(Ka * M))."""
    if ka <= 0 or molaritas <= 0:
        raise ValueError("Ka dan molaritas harus positif.")
    h = math.sqrt(ka * molaritas)
    return ph_dari_h(h)


def ph_basa_lemah(kb, molaritas):
    """pH basa lemah = 14 + log10(sqrt(Kb * M))."""
    if kb <= 0 or molaritas <= 0:
        raise ValueError("Kb dan molaritas harus positif.")
    oh = math.sqrt(kb * molaritas)
    return 14 - poh_dari_oh(oh)


def h_dari_ph(ph):
    """Konsentrasi [H+] dari pH: [H+] = 10^(-pH)."""
    return 10 ** (-ph)
