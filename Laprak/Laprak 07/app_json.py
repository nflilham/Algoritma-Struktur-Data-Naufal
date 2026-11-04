# Naufal Ilham Fauzan
# 2502106
# json

import json 

mahasiswa = {
    "nama": "Naufal Ilham Fauzan",
    "umur": 20,
    "jurusan": "Statistika - FMIPA UNPAD"
}

text_json = json.dumps(mahasiswa)
print(text_json)
# Output : {"nama": "Naufal Ilham Fauzan", "umur": 20, "jurusan": "Statistika - FMIPA UNPAD"}

json_string = '{"nama": "Naufal Ilham Fauzan", "umur": 20, "jurusan": "Statistika - FMIPA UNPAD"}'
data_json = json.loads(json_string)
# Output : {'nama': 'Naufal Ilham Fauzan', 'umur': 20, 'jurusan': 'Statistika - FMIPA UNPAD'}
print(data_json.get("nama"))
print(data_json.get("umur"))
print(data_json.get("jurusan"))