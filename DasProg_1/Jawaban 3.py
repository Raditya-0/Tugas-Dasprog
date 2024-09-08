# Input waktu sebagai satu angka (misalnya 230 untuk 2 jam 30 menit)
time_input = int(input("Masukkan waktu sejak mati listrik dalam format HHMM (misalnya 230 untuk 2 jam 30 menit): "))

jam = time_input // 100   # Bagian jam
menit = time_input % 100  # Bagian menit

# Menghitung total waktu dalam jam
waktu_lampu_mati = jam + (menit / 60)

# Menghitung suhu freezer
Temperature = (4 * (waktu_lampu_mati**2) / (waktu_lampu_mati + 2)) - 20

print(f"Suhu di dalam freezer kira-kira {Temperature:.2f} derajat Celcius")
