data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}
# no1
print("Seluruh Data")
for r, h in data_panen.items():
    print(f"{r}: Nama Lokasi: {h['nama_lokasi']}, Hasil Panen: {h['hasil_panen']}")
print()
# no2
jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung dari lokasi2: {jagung_lokasi2}")
print()
#no3
lokasi_ke_3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {lokasi_ke_3}")
print()
#no4
jumlah_padi = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
jumlah_kedelai = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}

print("Jumlah hasil panen padi dari setiap lokasi")
print(jumlah_padi)
print()

print("Jumlah hasil panen kedelai dari setiap lokasi")
print(jumlah_kedelai)
print()
# #no5
print("Status perhatian tiap lokasi:")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    nama = data['nama_lokasi']
    #no6
    if padi > 1300 or jagung > 800:
        print(f"Lokasi {nama} memerlukan perhatian khusus (Padi: {padi}, Jagung: {jagung})")
    else:
        print(f"Lokasi {nama} dalam kondisi baik (Padi: {padi}, Jagung: {jagung})")



#commit ke 2