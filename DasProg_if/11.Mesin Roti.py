def tampilkan_instruksi(jenis_roti, ukuran_double, manual):
    """Menampilkan instruksi untuk proses pembuatan roti."""
    waktu_roti = {
        'W': {'kneading': 15, 'rising': 60, 'second_kneading': 18, 'second_rising': 20, 'shaping': 2, 'final_rising': 75, 'baking': 45, 'cooling': 30},
        'S': {'kneading': 20, 'rising': 60, 'second_kneading': 33, 'second_rising': 30, 'shaping': 2, 'final_rising': 75, 'baking': 35, 'cooling': 30}
    }

    waktu = waktu_roti[jenis_roti]

    if ukuran_double:
        faktor_ukuran = 1.5
    else:
        faktor_ukuran = 1

    for langkah, menit in waktu.items():
        if langkah != 'shaping':
            print(f"{langkah.replace('_', ' ').title()} selama {menit * faktor_ukuran} menit")
        else:
            print(f"{langkah.replace('_', ' ').title()} selama {menit * faktor_ukuran} detik")

    if manual:
        print("Proses pembuatan roti selesai. Angkat adonan dan panggang secara manual.")
    else:
        print("Proses pembuatan roti selesai.")

# Perulangan untuk input yang valid
while True:
    jenis_roti = input("Masukkan jenis roti (W untuk Putih, S untuk Manis): ").upper()
    if jenis_roti not in ['W', 'S']:
        print("Jenis roti tidak valid. Silakan coba lagi.")
        continue
    
    ukuran_double = input("Apakah ukuran roti double (Y/N)? ").upper()
    if ukuran_double not in ['Y', 'N']:
        print("Input tidak valid. Silakan coba lagi.")
        continue

    manual = input("Apakah pemanggangan manual (Y/N)? ").upper()
    if manual not in ['Y', 'N']:
        print("Input tidak valid. Silakan coba lagi.")
        continue

    ukuran_double = ukuran_double == 'Y'
    manual = manual == 'Y'

    tampilkan_instruksi(jenis_roti, ukuran_double, manual)
    break  # Keluar dari perulangan setelah input valid
