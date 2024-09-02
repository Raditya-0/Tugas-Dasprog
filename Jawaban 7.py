# Meminta data input
gallon_oil = int(input("Masukkan jumlah gallon : "))
efficiency = int(input("Masukkan berapa efisiensinya : "))

konversi = 5800000
# mengkonversi ke BTU dengan data input gallon dan efisiensi
BTU = ((gallon_oil/42) * konversi)*(efficiency/100)

# Hasil konversi 
print(f"Hasil akhir jumlah galon dengan efisiensi {efficiency}% adalah {BTU} BTU")
