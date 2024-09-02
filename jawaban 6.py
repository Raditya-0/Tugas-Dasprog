# Meminta input data
nilai_tujuan = (char := input("Enter desired grade : "))[0]
nilai_minimal = float(input("Enter minimum average required : "))
nilai_sekarang = float(input("Enter current average in course : "))
persen_ulangan_akhir = int(input("Enter how much the final counts as a percentage of the course grade : "))

# Dimasukkan ke dalam rumus data tadi
nilai_ulangan_akhir = (nilai_minimal - (nilai_sekarang * (100 - persen_ulangan_akhir) / 100)) / (persen_ulangan_akhir / 100)

# Tampilkan hasil
print(f"You need a score of {nilai_ulangan_akhir:.2f} on the final to get a {nilai_tujuan}.")