while True:
    try:
        # Membaca input dari pengguna
        input_data = input("Masukkan jumlah mobil (M, N) dan waktu (T) dipisahkan oleh spasi: ").strip()
        
        # Mengonversi input menjadi tiga angka
        M, N, T = map(int, input_data.split())
        
        # Validasi input
        if M < 0 or N < 0 or T < 0:
            print("Input tidak valid. Pastikan M, N, dan T adalah angka positif.")
            continue
        
        # Waktu siklus lampu lalu lintas
        red_time = 20
        yellow_time = 5
        green_time = 60
        total_cycle_time = red_time + yellow_time + green_time
        
        # Hitung jumlah siklus lengkap dalam waktu T
        num_full_cycles = T // total_cycle_time
        remaining_time = T % total_cycle_time
        
        # Hitung jumlah mobil yang dapat lewat dalam satu siklus hijau
        cars_passed_per_cycle = green_time // 5
        
        # Hitung total mobil yang bisa lewat dalam waktu T
        total_cars_passed = num_full_cycles * cars_passed_per_cycle
        
        # Tambahkan mobil yang dapat lewat pada sisa waktu
        if remaining_time > red_time + yellow_time:
            additional_green_time = remaining_time - (red_time + yellow_time)
            total_cars_passed += additional_green_time // 5
        
        # Hitung mobil yang tersisa
        total_cars = M + N + 1
        cars_left = total_cars - total_cars_passed
        
        if cars_left <= 0:
            print("YES! 0")
        else:
            print(f"NO! {cars_left}")
        
        break  # Keluar dari loop jika input valid dan hasil sudah dicetak
    
    except ValueError:
        print("Input tidak valid. Harap masukkan tiga angka yang valid dipisahkan oleh spasi.")

