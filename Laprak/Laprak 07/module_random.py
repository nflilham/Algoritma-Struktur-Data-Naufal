# Naufal Ilham Fauzan
# 2502106
# random

import random

# Angka integer random
print("Random 1-10:", random.randint(1, 10))
print("Random 0-100:", random.randint(0, 100))

# Angka float random
print("Random 0.0-1.0:", random.random())
print("Random 1.5-10.5:", random.uniform(1.5, 10.5))

# Pilih satu item
buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]
pilihan = random.choice(buah)
print("Buah terpilih:", pilihan)