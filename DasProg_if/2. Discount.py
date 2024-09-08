# Input nilai variabel
while True:
  try :
   Total_beli = float(input("Masukkan total pembelian : "))
   status = bool(input("Status Mahasiswa (Jika tidak dikosongin) : "))
   if Total_beli < 0:
        print("Total pembelian tidak boleh negatif. Silakan coba lagi !\n")
   else:
        break  # Keluar dari loop 
  except ValueError:
     print("Masukkan angka dengan benar.Ulangi lagi !\n")

# Cetak Total Pembelian Awal
print(f"\n{'Total Pembelian':<30}: {Total_beli:>10.2f}")
    
# Jika status mahasiswa, hitung diskon 20%
if status == True:
    Diskon = Total_beli * 0.2
    print(f"{'Diskon (20 %)':<30}: {Diskon:>10.2f}")
    Total_beli -= Diskon
    print(f"{'Total diskon' :<30}: {Total_beli:>10.2f}")
    
# Hitung Pajak (5%)
Pajak = round((Total_beli * 5) / 100 , 2)
print(f"{'Pajak (5%)':<30}: {Pajak:>10.2f}")
    
# Hitung Total Bayar
Total_bayar = Total_beli + Pajak
print(f"{'Total Bayar':<30}: {Total_bayar:>10.2f}")


