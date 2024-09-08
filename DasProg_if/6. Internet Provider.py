# Input dari pengguna: jumlah data yang digunakan

while True:
  try :
    n = float(input("Masukkan jumlah data yang digunakan (dalam Gbs): "))
# n = data yang dipakai

# Memeriksa jumlah data dan menentukan biaya
    if 0.0 < n <= 1.0:  
        Biaya = 250
        break
    elif 1.0 < n <= 2.0:  
        Biaya = 500
        break
    elif 2.0 < n <= 5.0:
        Biaya = 1000
        break
    elif 5.0 < n <= 10.0:
        Biaya = 1500
        break
    elif n > 10.0:
        Biaya = 2000
        break
    else:
        print("Data tidak valid\n")
  
  except ValueError:
    print("Input harus angka!\n")
    

# Menampilkan biaya jika data valid
print(f"Biaya yang harus dibayar: Rp {Biaya}")
