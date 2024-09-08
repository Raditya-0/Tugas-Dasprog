while True:
    try:
        # Membaca input dari pengguna
        n = int(input("Masukkan angka: ").strip())
        
        # Ubah angka menjadi string
        str_n = str(n)
        
        # Periksa apakah ada digit '4' dalam string
        if '4' in str_n:
            print("SEVER")
        else:
            print("UNITE")
        
        break  # Keluar dari loop setelah mendapatkan hasil
        
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

