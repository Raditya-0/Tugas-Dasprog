# Meminta input bilangan bulat m dan n
m = int(input("Masukkan bilangan bulat pertama (m): "))
n = int(input("Masukkan bilangan bulat kedua (n): "))

# Menghitung side 1, side 2, dan hypotenusa menggunakan rumus yang diberikan
side1 = (m * m) - (n * n)
side2 = 2 * (m * n)
hypotenuse = (m * m) + (n * n)

# Menampilkan hasil triple Pythagoras
print(f"Triple Pythagoras dari bilangan-bilangan ini adalah {side1}, {side2}, dan {hypotenuse}")
