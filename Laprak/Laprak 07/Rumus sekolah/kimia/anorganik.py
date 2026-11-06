"""Modul kimia anorganik: biloks dan reaksi redoks."""


def bilangan_oksidasi_unsur_bebas():
    """Biloks unsur bebas = 0."""
    return 0


def bilangan_oksidasi_ion_monoatomik(muatan):
    """Biloks ion monoatomik = muatan ionnya."""
    return muatan


def bilangan_oksidasi_oksigen_umum():
    """Biloks O biasanya -2 (kecuali peroksida -1, F2O +2)."""
    return -2


def bilangan_oksidasi_hidrogen_umum():
    """Biloks H biasanya +1 (kecuali hidrida logam -1)."""
    return +1


def cek_reaksi_redoks(perubahan_biloks):
    """Reaksi redoks terjadi jika ada perubahan biloks."""
    return perubahan_biloks != 0


def oksidator_dan_reduktor(zat_biloks_naik, zat_biloks_turun):
    """Reduktor = biloks naik (teroksidasi), oksidator = biloks turun (tereduksi)."""
    return {"reduktor": zat_biloks_naik, "oksidator": zat_biloks_turun}


def penyetaraan_redoks_setengah_reaksi(e_lepas, e_terima):
    """Penyetaraan e- lepas harus sama dengan e- terima."""
    if e_lepas != e_terima:
        return False, f"e- tidak setara: lepas {e_lepas}, terima {e_terima}"
    return True, "Reaksi setara"
