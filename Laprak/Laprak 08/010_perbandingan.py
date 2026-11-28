import time

def konstan(data):
    return data[0]

def linear(data):
    total = 0
    for x in data:
        total += x
    return total

def kuadrat(data):
    total = 0
    for x in data:
        for y in data:
            total += x * y
        return total

for n in (100, 500, 1000, 2000):
    data = list(range(n))
    for fungsi in (konstan, linear, kuadrat):
        start_time = time.perf_counter()
        fungsi(data)
        end_time = time.perf_counter()
        print(f"n={n:<5} {fungsi.__name__:<8} {end_time - start_time:.6f} detik")