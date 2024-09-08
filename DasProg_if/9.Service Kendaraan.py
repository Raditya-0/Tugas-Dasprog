while True:
    print("Pilih layanan gratis:")
    print("(1) Layanan Gratis Pertama")
    print("(2) Layanan Gratis Kedua")
    
    try:
        # Meminta input jumlah mobil
        jumlah_mobil = int(input("Masukkan Jumlah Mobil : "))
        i = 0
        
        # Memproses setiap mobil berdasarkan jumlah yang dimasukkan
        while i < jumlah_mobil:
            # Meminta input layanan gratis
            layanan = int(input("Masukkan nomor layanan gratis (1 atau 2)>> "))
            
            # Meminta input jumlah mil
            mil = int(input("Masukkan jumlah mil>> "))
            
            # Validasi input mil
            if mil < 0:
                print("Jumlah mil tidak valid. Harus angka positif!")
                continue
            
            # Tentukan apakah kendaraan perlu diservis
            if layanan == 1:
                if 1500 < mil <= 3000:
                    print("Kendaraan harus diservis.")
                else:
                    print("Gratis servis tidak berlaku.")
            elif layanan == 2:
                if 3001 < mil <= 4500:
                    print("Kendaraan harus diservis.")
                else:
                    print("Gratis servis tidak berlaku.")
            else:
                print("Layanan tidak valid. Silakan pilih 1 atau 2.")
                continue
            
            # Setelah validasi, lanjut ke mobil berikutnya
            i += 1

        # Setelah semua mobil selesai diproses, keluar dari loop
        break

    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.")


