# Nafual Ilham Fauzan
# 2502106

import time

n = 10000 
data = list(range(n))

start_time = time.perf_counter()

pair_count = 0
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] + data[j] == 999999:
            pair_count += 1

end_time = time.perf_counter()
print(f"Waktu hasil eksekusi untuk N={n} : {end_time - start_time:.4f} detik")