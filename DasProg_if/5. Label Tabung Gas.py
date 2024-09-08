# Program untuk melaporkan isi dari tabung gas berdasarkan warna

# Input warna tabung dari pengguna
while True:
   try :
     warna = input("Masukkan huruf pertama warna tabung : ").lower()

# Memeriksa warna tabung dan melaporkan isinya
     if warna == 'o':
      print("Isi tabung: Amonia (Ammonia)")
      break
     elif warna == 'b':
         print("Isi tabung: Karbon monoksida (Carbon Monoxide)")
         break
     elif warna == 'y':
         print("Isi tabung: Hidrogen (Hydrogen)")
         break
     elif warna == 'g':
         print("Isi tabung: Oksigen (Oxygen)")
         break
     else:
         print("Isi tabung tidak diketahui (Contents unknown). Coba pilih antara Y, O, B, G\n")
    
   except ValueError:
      print("Input yang anda masukkan bukan huruf. Coba ulangi.")
