while True:
    try:
        # Membaca input dari pengguna
        n = int(input("Masukkan nilai Jumlah bola yang diberikan : "))
        c = int(input("Lili atau Lala duluan (1 = Lala dan 2 = Lili): "))

        # Validasi input
        if n <= 0 or c not in (1, 2):
            print("Input tidak valid. Masukkan nilai jumlah bola positif dan pilih lili atau lala duluan (1 atau 2).")
            continue
        
        # Memulai permainan
        current_player = c

        while n > 0:
            # Pemain saat ini mengambil bola
            if n > 5:
                n -= 5
            elif n > 2:
                n -= 2
            else:
                n -= 1
            
            # Berganti pemain
            current_player = 1 if current_player == 2 else 2

        # Pemain yang terakhir kali bergerak sebelum bola habis adalah pemenangnya
        # Ketika loop selesai, current_player adalah pemain yang bergerak setelah bola habis
        # Jadi pemenangnya adalah pemain sebelumnya
        winner = 1 if current_player == 2 else 2
        
        # Menampilkan hasil
        print("Pemenang adalah Lala" if winner == 1 else "Pemenang adalah Lili")
        
        break  # Keluar dari loop jika input valid dan hasil sudah dicetak
    
    except ValueError:
        print("Input tidak valid. Harap masukkan dua angka yang valid yang dipisahkan oleh spasi.")
