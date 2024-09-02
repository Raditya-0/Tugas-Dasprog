# Meminta input koordinat dari dua titik dalam satu baris
x1, y1, x2, y2 = map(float, input("Masukkan koordinat x1, y1, x2, y2 (misal: 2.0 -4.0 7.0 -2.0): ").split())

# Menampilkan koordinat yang dimasukkan dan persamaan sumbu tegak lurus
print(f"Koordinat yang dimasukkan adalah ({x1}, {y1}) dan ({x2}, {y2}).")

# Cek apakah garis tersebut adalah garis vertikal, garis horizontal, atau garis miring

if x1 == x2: # Jika garis vertikal maka akan menjalankan if ini
    print("Garis yang menghubungkan dua titik adalah garis vertikal, sehingga sumbu tegak lurus adalah garis horizontal.")
    print(f"Persamaan sumbu tegak lurus: y = {(y1 + y2) / 2:.2f}")
    
elif y1 == y2: # Jika garis horizontal maka akan menjalankan elif ini
    print("Garis yang menghubungkan dua titik adalah garis horizontal, sehingga sumbu tegak lurus adalah garis vertikal.")
    print(f"Persamaan sumbu tegak lurus: x = {(x1 + x2) / 2:.2f}")

else : # Jika miring akan menjalankan else
    # Menghitung kemiringan sumbu tegak lurus dengan mengambil kebalikan negatif
    kemiringan = -1/((y2 - y1) / (x2 - x1))

    # Menghitung titik tengah dari segmen garis antara dua titik
    xtengah = (x1 + x2) / 2
    ytengah = (y1 + y2) / 2

    # Menghitung intersep y dari sumbu tegak lurus
    intersep = ytengah - (kemiringan * xtengah)

    # Hasilnya
    print(f"Persamaan sumbu tegak lurus dari garis tersebut adalah y = {kemiringan:.2f}x + {intersep:.2f}")
