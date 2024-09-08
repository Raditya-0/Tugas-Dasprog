def leap(year): # Ngecek tahun kabisat atau bukan
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 1
    else:
        return 0

def hari_ke(month, day, year): # Menghitung harinya
    # Jumlah hari di setiap bulan untuk tahun biasa
    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Periksa apakah tahun kabisat
    if leap(year) == 1:
        hari_per_bulan[1] = 29  # Jika iya maka Febuari diubah 29 hari

    # Menghitung nomor hari
    nomor_hari = sum(hari_per_bulan[:month-1]) + day
    return nomor_hari

def main():
    while True:
        try:
            month = int(input("Masukkan bulan (1-12): "))
            day = int(input("Masukkan tanggal (1-31): "))
            year = int(input("Masukkan tahun: "))

            # Validasi bulan
            if month < 1 or month > 12:
                print(f"Bulan {month} tidak valid. Harus antara 1 dan 12.")
                continue
            
            # Validasi tahun dan tanggal
            hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if leap(year) == 1:
                hari_per_bulan[1] = 29  # Februari memiliki 29 hari di tahun kabisat
            
            if day < 1 or day > hari_per_bulan[month-1]:
                print(f"Tanggal {day} tidak valid untuk bulan {month}.")
                continue

            # Semua data valid
            nomor_hari = hari_ke(month, day, year)
            print(f"{day}/{month}/{year} adalah hari ke-{nomor_hari} dalam tahun {year}.")
            break  # Keluar dari loop jika data valid
            
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")

if __name__ == "__main__":
    main()
