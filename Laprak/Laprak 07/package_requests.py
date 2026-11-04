# Naufal Ilham Fauzan
# 2502106  
# requests

import requests
response = requests.get("https://github.com/nflilham")

if response.status_code == 200:
    data = response.json()
    print("Nama Pengguna\t\t: ", data['login'])
    print("Jumlah Followers\t: ", data['followers'])
    print("Jumlah Repositori\t: ", data['public_repos'])
else:
    print("Gagal mengambil data")