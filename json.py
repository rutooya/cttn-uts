import json

data_a = 0
with open('daftar_belanja.json', 'r') as datafile:
    data = json.load(datafile)
    data_a = data
    
with open('daftar_belanja.json', 'w') as datafile:
    total_nominal = 0
    for idx, item in enumerate(data, start = 1):
        print(f"{idx}. {item['catatan']} - Rp {item['nominal']}")
        total_nominal = total_nominal + item['nominal']
    print(f"Total Nominal: Rp {total_nominal}")
    catatan = str(input('Masukkan catatan: '))
    nominal = int(input('Masukkan nominal: '))
    data_a.append({'catatan': catatan, 'nominal': nominal})
    json.dump(data, datafile)
    print('Data berhasil disimpan!')