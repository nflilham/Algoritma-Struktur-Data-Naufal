import time

# Membuat list berisi 1 juta angka
data = list(range(1_000_000))
target = 999_999  # Elemen paling akhir atau terburuk

# Eksperimen 2: Linear search menggunakan operator 'in'
start_time = time.perf_counter()
found = target in data
end_time = time.perf_counter()
print(f"Waktu Operator 'in': {end_time - start_time:.6f} detik")
