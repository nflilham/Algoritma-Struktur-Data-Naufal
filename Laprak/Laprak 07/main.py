"""Demo lengkap package Rumus Sekolah: Matematika, Kimia, Fisika."""

import sys
sys.path.insert(0, '.')
from Rumus_sekolah import matematika, kimia, fisika


def demo_matematika():
    """Demo fungsi-fungsi matematika."""
    print("\n" + "=" * 60)
    print("DEMO MATEMATIKA")
    print("=" * 60)
    
    # Dasar
    print("\n--- Dasar ---")
    print(f"2 + 3 = {matematika.dasar.tambah(2, 3)}")
    print(f"10 / 2 = {matematika.dasar.bagi(10, 2)}")
    print(f"2^5 = {matematika.dasar.pangkat(2, 5)}")
    print(f"Faktorial 5 = {matematika.dasar.faktorial(5)}")
    
    # Aritmatika
    print("\n--- Aritmatika ---")
    print(f"FPB(24, 36) = {matematika.aritmatika.fpb(24, 36)}")
    print(f"KPK(12, 18) = {matematika.aritmatika.kpk(12, 18)}")
    print(f"Apakah 17 prima? {matematika.aritmatika.is_prima(17)}")
    print(f"Fibonacci(10): {matematika.aritmatika.fibonacci(10)}")
    
    # Geometri
    print("\n--- Geometri ---")
    print(f"Luas persegi (s=5): {matematika.geometri.luas_persegi(5)}")
    print(f"Luas lingkaran (r=7): {matematika.geometri.luas_lingkaran(7):.2f}")
    print(f"Volume kubus (s=3): {matematika.geometri.volume_kubus(3)}")
    print(f"Volume bola (r=5): {matematika.geometri.volume_bola(5):.2f}")
    
    # Statistika
    print("\n--- Statistika ---")
    data = [5, 7, 8, 8, 9, 10, 12]
    print(f"Data: {data}")
    print(f"Mean: {matematika.statistika.mean(data):.2f}")
    print(f"Median: {matematika.statistika.median(data)}")
    print(f"Modus: {matematika.statistika.modus(data)}")
    print(f"Standar deviasi: {matematika.statistika.standar_deviasi_populasi(data):.2f}")
    
    # Trigonometri
    print("\n--- Trigonometri ---")
    print(f"sin(30°) = {matematika.trigonometri.sin_deg(30):.2f}")
    print(f"cos(60°) = {matematika.trigonometri.cos_deg(60):.2f}")
    print(f"tan(45°) = {matematika.trigonometri.tan_deg(45):.2f}")
    
    # Aljabar
    print("\n--- Aljabar ---")
    x1, x2 = matematika.aljabar.akar_persamaan_kuadrat(1, -5, 6)
    print(f"Akar x^2 - 5x + 6 = 0: x1={x1}, x2={x2}")
    xp, yp = matematika.aljabar.titik_puncak_parabola(1, -4, 3)
    print(f"Titik puncak y=x^2-4x+3: ({xp}, {yp})")
    
    # Peluang
    print("\n--- Peluang ---")
    print(f"Permutasi P(5,3) = {matematika.peluang.permutasi(5, 3)}")
    print(f"Kombinasi C(5,3) = {matematika.peluang.kombinasi(5, 3)}")
    print(f"Peluang klasik 3/6 = {matematika.peluang.peluang_klasik(3, 6):.2f}")
    
    # Barisan Deret
    print("\n--- Barisan & Deret ---")
    print(f"Suku ke-5 aritmatika (a=2, b=3): {matematika.barisan_deret.suku_ke_n_aritmatika(2, 3, 5)}")
    print(f"Jumlah 10 suku aritmatika (a=1, b=2): {matematika.barisan_deret.jumlah_n_aritmatika(1, 2, 10)}")
    
    # Matriks
    print("\n--- Matriks ---")
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    print(f"Det(m1) = {matematika.matriks.determinan_2x2(m1)}")
    m_sum = matematika.matriks.tambah_matriks_2x2(m1, m2)
    print(f"m1 + m2 = {m_sum}")


def demo_kimia():
    """Demo fungsi-fungsi kimia."""
    print("\n" + "=" * 60)
    print("DEMO KIMIA")
    print("=" * 60)
    
    # Suhu
    print("\n--- Konversi Suhu ---")
    print(f"25°C ke Fahrenheit: {kimia.suhu.celsius_ke_fahrenheit(25):.1f}°F")
    print(f"25°C ke Kelvin: {kimia.suhu.celsius_ke_kelvin(25):.1f} K")
    
    # Mol
    print("\n--- Mol & Partikel ---")
    print(f"60 gram H2O (Mr=18) = {kimia.mol.gram_ke_mol(60, 18):.2f} mol")
    print(f"2 mol = {kimia.mol.mol_ke_partikel(2):.2e} partikel")
    print(f"2 mol gas di STP = {kimia.mol.volume_gas_stp(2):.1f} L")
    
    # Konsentrasi
    print("\n--- Konsentrasi ---")
    print(f"Molaritas (0.5 mol, 1 L): {kimia.konsentrasi.molaritas(0.5, 1)} M")
    print(f"Molalitas (0.5 mol, 0.5 kg): {kimia.konsentrasi.molalitas(0.5, 0.5)} m")
    print(f"Persen massa (10g zat, 100g larutan): {kimia.konsentrasi.persen_massa(10, 100):.1f}%")
    
    # Larutan
    print("\n--- Sifat Koligatif Larutan ---")
    print(f"Kenaikan titik didih (Kb=0.5, m=1): {kimia.larutan.kenaikan_titik_didih(0.5, 1):.2f}°C")
    print(f"Penurunan titik beku (Kf=1.86, m=1): {kimia.larutan.penurunan_titik_beku(1.86, 1):.2f}°C")
    
    # Asam Basa
    print("\n--- Asam Basa ---")
    print(f"pH dari [H+] 0.001 M: {kimia.asam_basa.ph_dari_h(0.001):.1f}")
    print(f"pH asam kuat (0.1 M): {kimia.asam_basa.ph_asam_kuat(0.1):.1f}")
    print(f"pH basa kuat (0.01 M): {kimia.asam_basa.ph_basa_kuat(0.01):.1f}")
    
    # Elektrokimia
    print("\n--- Elektrokimia ---")
    print(f"Potensial sel (E+0.8V, E-0.4V): {kimia.elektrokimia.potensial_sel(0.8, -0.4):.1f} V")
    
    # Termokimia
    print("\n--- Termokimia ---")
    print(f"Kalor reaksi (m=100g, c=4.18, ΔT=10): {kimia.termokimia.kalor_reaksi(100, 4.18, 10):.0f} J")
    
    # Stoikiometri
    print("\n--- Stoikiometri ---")
    print(f"Rendemen (80g hasil, 100g teoritis): {kimia.stoikiometri.rendemen(80, 100):.1f}%")
    
    # Organik
    print("\n--- Kimia Organik ---")
    print(f"Rumus umum alkana (n=5): {kimia.organik.rumus_umum_alkana(5)}")
    print(f"Nama alkana (n=4): {kimia.organik.nama_alkana(4)}")
    
    # Anorganik
    print("\n--- Kimia Anorganik ---")
    print(f"Biloks unsur bebas: {kimia.anorganik.bilangan_oksidasi_unsur_bebas()}")


def demo_fisika():
    """Demo fungsi-fungsi fisika."""
    print("\n" + "=" * 60)
    print("DEMO FISIKA")
    print("=" * 60)
    
    # Kinematika
    print("\n--- Kinematika ---")
    print(f"Kecepatan (s=100m, t=5s): {fisika.kinematika.kecepatan(100, 5)} m/s")
    print(f"GLBB jarak (v0=10, a=2, t=5): {fisika.kinematika.glbb_jarak(10, 2, 5)} m")
    print(f"GJB kecepatan (t=2s): {fisika.kinematika.gerak_jatuh_bebas_kecepatan(2):.1f} m/s")
    
    # Dinamika
    print("\n--- Dinamika ---")
    print(f"Gaya (m=10kg, a=2m/s²): {fisika.dinamika.hukum_newton_2(10, 2)} N")
    print(f"Gaya sentripetal (m=1kg, v=10m/s, r=5m): {fisika.dinamika.gaya_sentripetal(1, 10, 5):.1f} N")
    print(f"Berat (m=50kg): {fisika.dinamika.berat(50):.1f} N")
    
    # Usaha & Energi
    print("\n--- Usaha & Energi ---")
    print(f"Usaha (F=10N, s=5m): {fisika.usaha_energi.usaha(10, 5)} J")
    print(f"Energi kinetik (m=2kg, v=5m/s): {fisika.usaha_energi.energi_kinetik(2, 5)} J")
    print(f"Energi potensial (m=1kg, h=10m): {fisika.usaha_energi.energi_potensial(1, 10):.1f} J")
    print(f"Daya (W=100J, t=5s): {fisika.usaha_energi.daya(100, 5):.1f} W")
    
    # Momentum
    print("\n--- Momentum ---")
    print(f"Momentum (m=2kg, v=5m/s): {fisika.momentum.momentum(2, 5)} kg.m/s")
    print(f"Impuls (F=10N, t=2s): {fisika.momentum.impuls(10, 2)} N.s")
    
    # Gravitasi
    print("\n--- Gravitasi ---")
    gaya_grav = fisika.gravitasi.gaya_gravitasi(1e24, 1e24, 1e8)
    print(f"Gaya gravitasi (2 benda 1e24 kg, jarak 1e8 m): {gaya_grav:.2e} N")
    
    # Getaran
    print("\n--- Getaran ---")
    print(f"Periode bandul (L=1m): {fisika.getaran.periode_bandul(1):.2f} s")
    print(f"Frekuensi (T=0.5s): {fisika.getaran.frekuensi_dari_periode(0.5)} Hz")
    
    # Gelombang
    print("\n--- Gelombang ---")
    print(f"Cepat rambat gelombang (f=5Hz, λ=2m): {fisika.gelombang.cepat_rambat_gelombang(5, 2)} m/s")
    print(f"Intensitas bunyi (P=10W, A=2m²): {fisika.gelombang.intensitas_gelombang(10, 2):.1f} W/m²")
    
    # Optik
    print("\n--- Optik ---")
    print(f"Hukum Snellius (n1=1, θ1=30°, n2=1.5): {fisika.optik.hukum_snellius(1, 30, 1.5):.2f}°")
    
    # Listrik
    print("\n--- Listrik ---")
    print(f"Hukum Ohm V (I=2A, R=10Ω): {fisika.listrik.hukum_ohm_tegangan(2, 10)} V")
    print(f"Hambatan seri (R1=10Ω, R2=20Ω): {fisika.listrik.hambatan_seri(10, 20)} Ω")
    print(f"Hambatan paralel (R1=10Ω, R2=10Ω): {fisika.listrik.hambatan_paralel(10, 10):.1f} Ω")
    print(f"Daya listrik (V=220V, I=5A): {fisika.listrik.daya_listrik(220, 5):.0f} W")
    
    # Magnet
    print("\n--- Magnet & Elektromagnetik ---")
    print(f"Gaya Lorentz (q=1C, v=10m/s, B=0.5T): {fisika.magnet.gaya_lorentz(1, 10, 0.5):.1f} N")
    
    # Termodinamika
    print("\n--- Termodinamika ---")
    print(f"Kalor (m=100g, c=4.18J/g°C, ΔT=10°C): {fisika.termodinamika.kalor(100, 4.18, 10):.0f} J")
    print(f"Efisiensi Carnot (Tt=500K, Tr=300K): {fisika.termodinamika.efisiensi_mesin_carnot(500, 300):.1f}%")
    
    # Fluida
    print("\n--- Fluida ---")
    print(f"Tekanan hidrostatis (ρ=1000, h=2m): {fisika.fluida.tekanan_hidrostatis(1000, 2):.0f} Pa")
    print(f"Gaya Archimedes (ρ=1000, V=0.1m³): {fisika.fluida.gaya_archimedes(1000, 0.1):.0f} N")


if __name__ == "__main__":
    print("\n" + "█" * 60)
    print("█" + " " * 58 + "█")
    print("█" + "  DEMO PACKAGE RUMUS SEKOLAH (MATEMATIKA, KIMIA, FISIKA)  ".center(58) + "█")
    print("█" + " " * 58 + "█")
    print("█" * 60)
    
    demo_matematika()
    demo_kimia()
    demo_fisika()
    
    print("\n" + "█" * 60)
    print("█" + "  DEMO SELESAI  ".center(58) + "█")
    print("█" * 60 + "\n")
