# Input data jumlah penduduk
penduduk = int(input("Masukkan besarnya penduduk : "))

# Konstanta
flush_toilet_lama = 15
flush_toilet_baru = 2
harga_toilet_baru = 150
toilet_per_orang = 3
flush_per_hari = 14

# Perhitungan toilet dan biaya penghematan air
toilet = penduduk // toilet_per_orang
biaya = toilet * harga_toilet_baru

# Mencari selisih air yang berhasil di hemat
air_toilet_lama = toilet * flush_per_hari * flush_toilet_lama
air_toilet_baru = toilet * flush_per_hari * flush_toilet_baru
air_yang_dihemat = air_toilet_lama - air_toilet_baru

# Mengeluarkan hasil air yang dihemat dan biaya untuk merealisasikannya
print(f"dengan penduduk sebanyak {penduduk} orang, maka air yang dihemat adalah "
f"{air_yang_dihemat} liter/hari \ndengan biaya yaitu ${biaya} untuk membeli toilet baru.")

