boiling_points = {
    "Water": 100,
    "Mercury": 357,
    "Copper": 1187,
    "Silver": 2193,
    "Gold": 2660
}

# Fungsi untuk mengecek apakah data berada dalam x% dari nilai referensi
def within_x_percent(ref, data, x):
    return (ref - x / 100 * ref) <= data <= (ref + x / 100 * ref)

# Perulangan untuk meminta input yang valid
while True:
    try:
        observed_point = float(input("Masukkan titik didih yang diamati (°C): "))

        found = False
        for substance, bp in boiling_points.items():
            if within_x_percent(bp, observed_point, 5):
                print(f"Substansi: {substance}")
                found = True
                break
        
        if not found:
            print("Substansi tidak dikenal.")
        break  # Keluar dari perulangan jika input valid
    
    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.")
