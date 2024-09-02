'''
Diketahui :
h = tinggi
g = gravitasi
m = massa
MW = MegaWatt

'''

h = int(input("Masukkan tinggi : ")) # Masukkan nilai tinggi
meter_kubik = float(input("Masukkan meter kubik : ")) # Masukkan meter kubik

efisiensi = 0.9
g = 9.8

m = meter_kubik * 1000 # Merubah meter kubik menjadi massa
w = efisiensi*g*m*h/1e6 # Masukkan dalam rumus

print(f"Daya yang dihasilkan adalah {w:.2f}MW")
