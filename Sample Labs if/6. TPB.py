while True:
    try:
        # Membaca input dari pengguna
        n = int(input("Masukkan angka: ").strip())
        
        # Validasi dan pemeriksaan bilangan prima
        if n <= 1:
            is_prime = False
        elif n <= 3:
            is_prime = True
        elif n % 2 == 0 or n % 3 == 0:
            is_prime = False
        else:
            # Memeriksa bilangan prima
            i = 5
            is_prime = True
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    is_prime = False
                    break
                i += 6
            
        if is_prime:
            print(f"{n} adalah bilangan prima")
        else:
            print(f"{n} bukan bilangan prima")
        
        break  # Keluar dari loop setelah mendapatkan hasil
        
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")
