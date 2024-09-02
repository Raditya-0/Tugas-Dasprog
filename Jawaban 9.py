# Input data panjang dan lebar
panjang = int(input("Masukkan Panjang dalam feet (ft) : "))
lebar = int(input("Masukkan lebar dalam feet (ft) : "))

# Memasukkan ke dalam rumus untuk mengetahui waktu potong rumput
waktu_motong_rumput = (panjang * lebar)/2

# Mengeluarkan hasil hitungan untuk memotong rumput
print(f"Waktu yang dibutuhkan untuk memotong rumput adalah {waktu_motong_rumput:.2f} detik")