while True:
    try:
        # Membaca input dari pengguna
        input_data = input("Masukkan jarak antar pilar (dengan spasi) : ").strip()
        
        # Mengonversi input menjadi daftar angka
        distances = list(map(int, input_data.split()))
        
        # Memastikan jumlah jarak yang diberikan benar (1 jarak maksimum + 4 jarak antar pilar)
        if len(distances) != 5:
            print("Input harus berisi 5 angka (1 jarak maksimum dan 4 jarak antar pilar).")
            continue
        
        # Jarak maksimum yang bisa dilompati
        max_jump = distances[0]
        
        # Jarak antara pilar-pilar (A -> B -> C -> D -> E)
        pillar_distances = distances[1:]
        
        # Mengecek apakah B bisa melompat antar pilar
        can_jump = all(distance <= max_jump for distance in pillar_distances)
        
        # Jika semua jarak sesuai dengan batas maksimum lompatan
        if can_jump:
            print("YES HE CAN")
        else:
            print("NO HE CAN'T")
        
        break  # Keluar dari loop jika input valid dan hasil sudah dicetak
    
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang valid yang dipisahkan oleh spasi.")
