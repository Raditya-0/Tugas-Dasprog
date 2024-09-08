while True:
    try:
        # Membaca input angka
        input_numbers = list(map(int, input("Masukkan angka-angka (dengan spasi): ").strip().split()))
        
        # Membaca nilai b dan c
        b, c = map(int, input("Masukkan nilai Jumlah elemen yang rotasi dan Jumlah rotasi (dengan spasi): ").strip().split())
        
        # Membaca indeks/urutan yang diinginkan
        d, e, f = map(int, input("Masukkan indeks/urutan yang diinginkan (dengan spasi): ").strip().split())
        
        # Hitung panjang daftar angka
        length = len(input_numbers)
        
        # Hitung rotasi efektif
        effective_rotation = (b * c) % length
        
        # Lakukan rotasi
        rotated_numbers = input_numbers[-effective_rotation:] + input_numbers[:-effective_rotation]
        
        # Ambil nilai pada indeks yang ditentukan
        result = [rotated_numbers[idx] for idx in [d, e, f]]
        
        # Cetak hasil
        print(' '.join(map(str, result)))
        
        break  # Keluar dari loop setelah mendapatkan hasil
        
    except (ValueError, IndexError):
        print("Input tidak valid. Harap masukkan angka yang benar dan indeks yang valid.")
