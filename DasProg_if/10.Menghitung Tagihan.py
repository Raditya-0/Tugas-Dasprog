while True:
    try:
        # Input nilai dari pengguna
        weekday_minutes = int(input("Masukkan jumlah menit weekday: "))
        night_minutes = int(input("Masukkan jumlah menit malam: "))
        weekend_minutes = int(input("Masukkan jumlah menit akhir pekan: "))

        # Validasi input
        if weekday_minutes < 0 or night_minutes < 0 or weekend_minutes < 0:
            print("Jumlah menit tidak valid. Harus angka positif. Silakan coba lagi.")
            continue
        
        # Tarif dan biaya
        base_rate = 3999  # dalam sen
        included_minutes = 600
        additional_rate = 40  # per menit dalam sen
        tax_rate = 5.25 / 100

        # Hitung biaya tambahan jika jumlah menit weekday melebihi yang termasuk
        if weekday_minutes > included_minutes:
            additional_charge = (weekday_minutes - included_minutes) * additional_rate
        else:
            additional_charge = 0

        # Hitung tagihan sebelum pajak dan pajak
        pretax_bill = base_rate + additional_charge
        tax_amount = round(pretax_bill * tax_rate)
        total_bill = pretax_bill + tax_amount

        # Hitung rata-rata biaya per menit sebelum pajak
        total_minutes = weekday_minutes + night_minutes + weekend_minutes
        if total_minutes > 0:
            avg_cost = round(pretax_bill / total_minutes, 2)
        else:
            avg_cost = 0

        # Cetak hasil
        print(f"\nJumlah menit weekday: {weekday_minutes}")
        print(f"Jumlah menit malam: {night_minutes}")
        print(f"Jumlah menit akhir pekan: {weekend_minutes}")
        print(f"Tagihan sebelum pajak: ${pretax_bill / 100:.2f}")
        print(f"Rata-rata biaya per menit sebelum pajak: ${avg_cost / 100:.2f}")
        print(f"Pajak yang dibayar: ${tax_amount / 100:.2f}")
        print(f"Total tagihan: ${total_bill / 100:.2f}")
        break  # Keluar dari loop jika semua input valid
    
    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar. Silakan coba lagi.")
