''' 
Diketahui :
v = kecepatan
t = waktu
a = percepatan
s = jarak
'''
# Meminta input untuk kecepatan dan jarak
v = float(input("Masukkan kecepatan lepas landas jet (dalam km/jam): "))
s = float(input("Masukkan jarak (dalam meter) di mana katapel mempercepat jet: "))

# Menghitung waktu (dalam detik) menggunakan rumus t = 2s/v
t = (2 * s) / (v * (1000 / 3600))

# Menghitung percepatan (dalam m/s^2) menggunakan rumus a = v/t
a = (v * (1000 / 3600)) / t

# Menampilkan hasil perhitungan waktu dan percepatan
print(f"Waktu yang dibutuhkan jet untuk mencapai kecepatan lepas landas adalah {t:.2f} detik.")
print(f"Percepatan konstan jet adalah {a:.2f} m/s^2.")
