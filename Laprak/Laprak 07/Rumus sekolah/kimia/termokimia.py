"""Modul termokimia: entalpi dan kalor reaksi."""


def kalor_reaksi(massa, kalor_jenis, delta_suhu):
    """Kalor reaksi q = m * c * delta_T (Joule)."""
    return massa * kalor_jenis * delta_suhu


def entalpi_reaksi(sum_entalpi_produk, sum_entalpi_reaktan):
    """Delta H = sum(H produk) - sum(H reaktan)."""
    return sum_entalpi_produk - sum_entalpi_reaktan


def hukum_hess(delta_h_list):
    """Hukum Hess: jumlahkan delta H beberapa tahap reaksi."""
    return sum(delta_h_list)


def energi_ikatan(energi_pemutusan, energi_pembentukan):
    """Delta H = total energi pemutusan - total energi pembentukan."""
    return energi_pemutusan - energi_pembentukan


def kalor_ke_kj(joule):
    """Konversi Joule ke kilojoule."""
    return joule / 1000


def kalor_ke_kalori(joule):
    """Konversi Joule ke kalori (1 kal = 4.184 J)."""
    return joule / 4.184
