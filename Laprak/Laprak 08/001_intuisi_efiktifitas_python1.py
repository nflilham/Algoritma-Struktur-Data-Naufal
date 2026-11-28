# Naufal Ilham Fauzan
# 2502106

import time

#Membuat lis berisi 1 juta angka
data = list(range(1_000_000))
target = 999_999    # Elemen paling akhir atay terburuk

# Eksperimen 1: Linear search manual
start_time = time.perf_counter()

found = False
for item in data:
    if item == target:
        found = True
        break
        
end_time = time.perf_counter()
print(f"Waktu Linear Search: {end_time - start_time:.6f} detik")