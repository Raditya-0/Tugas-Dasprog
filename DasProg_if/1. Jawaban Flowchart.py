# Input nilai variabel umur_min dan umur_max
umur_min = 0  
umur_max = 100  

# Loop untuk meminta input hingga umur valid diberikan
while True:
  try :
    # Input nilai variabel
    age = int(input("Masukkan umur : "))
    work_status = bool(input("Work status (jika tidak bekerja diisi kosong) : ")) 

    # Cek apakah umur dalam batas yang valid
    if age < umur_min or age > umur_max:
        print(f"Umur di luar batas yang diizinkan ({umur_min} - {umur_max}). Ulangi lagi !\n")
    else:
        # Keluar dari loop jika umur valid
        break
  except ValueError:
      print("Input umur menggunakan angka. Silahkan coba lagi !")

if age > 59: 
    if work_status:  # Cek apakah bekerja
        print("Working Senior")
    else:
        print("Retired Senior")
else:
    if age < 12:  # Cek apakah termasuk Child
        print("Child")
    elif age >= 12 and age <= 20:  # Cek apakah termasuk Teen
        print("Teen")
    else:  # Jika tidak keduanya, maka adult
        print("Adult")


