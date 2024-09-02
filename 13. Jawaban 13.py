# Meminta input jumlah siswa yang terdaftar
jumlah_siswa = int(input("Masukkan jumlah siswa yang terdaftar: "))

# Jumlah siswa per kelas
siswa_per_kelas = 30

# Menghitung jumlah kelas yang dibutuhkan
jumlah_kelas = jumlah_siswa // siswa_per_kelas

# Menghitung jumlah siswa yang tersisa
sisa_siswa = jumlah_siswa % siswa_per_kelas

# Menampilkan hasil
print(f"Dengan {jumlah_siswa} siswa yang terdaftar, {jumlah_kelas} kelas dibutuhkan, dengan {sisa_siswa} siswa yang tersisa.")
