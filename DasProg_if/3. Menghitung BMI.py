# Input untuk berat badan dalam pound dan tinggi badan dalam inci
while True:
   try :
    berat_lb = float(input("Masukkan berat badan (dalam pound): "))
    tinggi_in = float(input("Masukkan tinggi badan (dalam inci): "))
    if (berat_lb <= 0) and (tinggi_in <= 0):
        print("Berat badan dan tinggi badan tidak valid. Coba lagi !\n")
    else :
         break
   except ValueError:
       print("Berat badan dan tinggi badan tidak valid")

# Menghitung BMI
bmi = round((703 * berat_lb) / (tinggi_in ** 2), 1)

# Menampilkan hasil BMI
print(f"\nBMI Anda adalah: {bmi}")

# Menentukan status berat badan berdasarkan nilai BMI
if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi <= 24.9:
    status = "Normal"
elif 25.0 <= bmi <= 29.9:
    status = "Overweight"
else:
    status = "Obese"

# Menampilkan status berat badan
print(f"Status berat badan Anda adalah: {status}")
