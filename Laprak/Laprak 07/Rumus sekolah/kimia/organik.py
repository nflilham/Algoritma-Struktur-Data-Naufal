"""Modul kimia organik sederhana."""


def rumus_umum_alkana(n):
    """Rumus umum alkana CnH(2n+2)."""
    if n < 1:
        raise ValueError("Jumlah atom C harus minimal 1.")
    return f"C{n}H{2*n+2}"


def rumus_umum_alkena(n):
    """Rumus umum alkena CnH(2n)."""
    if n < 2:
        raise ValueError("Alkena minimal punya 2 atom C.")
    return f"C{n}H{2*n}"


def rumus_umum_alkuna(n):
    """Rumus umum alkuna CnH(2n-2)."""
    if n < 2:
        raise ValueError("Alkuna minimal punya 2 atom C.")
    return f"C{n}H{2*n-2}"


def nama_alkana(n):
    """Tatanama alkana dari jumlah atom C."""
    nama = {
        1: "metana", 2: "etana", 3: "propana", 4: "butana", 5: "pentana",
        6: "heksana", 7: "heptana", 8: "oktana", 9: "nonana", 10: "dekana"
    }
    return nama.get(n, f"C{n}H{2*n+2}")


def jumlah_ikatan_rangkap(n_karbon, n_hidrogen):
    """Hitung jumlah ikatan rangkap/cincin: DBE = (2C + 2 - H) / 2."""
    return (2 * n_karbon + 2 - n_hidrogen) / 2


def isomer_posisi(nama_senyawa):
    """Placeholder: kembalikan info isomer posisi (implementasi detail butuh struktur)."""
    return f"Isomer posisi dari {nama_senyawa}"
