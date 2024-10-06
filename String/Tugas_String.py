# Create String
String_nama = "Raditya Akmal"
String_NRP = "5054241027"
String_asal = "Surabaya"

# Print String Data
print("Nama Saya :" + String_nama)
print("NRP Saya :" + String_NRP)
print("Asal Saya :" + String_asal)

# Access Character In String
print("Inisial Saya :" + String_nama[0] + String_nama[8])

# String Slicing
print("Nama Belakang :" + String_nama[8:])
print("Nama Awal :" + String_nama[:8])

# Reverse String
print("Reverse NRP :" + String_NRP[::-1])

# Update String
String_RKA = "Saya Mahasiswa RKA"
#ubah Menjadi "Saya bukan mahasiswa RPL"
list_RKA = list(String_RKA)
list_RKA[4] = ' Bukan '
String_Bukan = ''.join(list_RKA)
print(String_Bukan)

String_RPL = String_Bukan[0:21] + "RPL"
print(String_RPL)

# Tugas Implementasi

print("\n====1. Deleting a character====\n")

List_Kota = list(String_asal)
del List_Kota[4:]
String_Kota_Hapus = ''.join(List_Kota)
print(String_Kota_Hapus)

print("\n====2. Escape Sequencing in python + Example====\n")

# Contoh String Biasa
String_Initial = '''Halo Aku "Radit"'''
print(String_Initial)

# Contoh String dengan kutip satu
String_Single_Quote = 'Mari Sholat Jum\'at'
print(String_Single_Quote)

# Contoh String dengan kutip dua
String_Double_Qoute = "Bersama saya ,\"Radit\""
print(String_Double_Qoute)

# Contoh String dengan Backlash
String_Backslash = "C:\\\\user\\\\Radit"
print(String_Backslash)

# Contoh String dengan Tab
String_Tab = "\t \t \tTab"
print(String_Tab)

# Cara membuat baris baru di string
String_New_Line = "\nBaris pertama \nBaris kedua"
print(String_New_Line)

# Cara memnggunakan multiline di string
print('''
Baris satu
Baris dua
Baris tiga
''')

# String di Oktal
# Mencetak "Halo Namaku Radit" dengan "Radit" dalam Oktal
String_Octal = "Halo Namaku \122\141\144\151\164"
print(String_Octal)

# Menggunakan raw String untuk melihat mentahannya
String_Octal_Raw = r"Halo Namaku \122\141\144\151\164"
print(String_Octal_Raw)

# String di Hex
# Mencetak "Halo Namaku Radit" dengan "Radit" dalam HEX
String_Hex = "Halo Namaku \x52\x61\x64\x69\x74"
print(String_Hex)

# Menggunakan raw String untuk melihat mentahannya
String_Hex_Raw = r"Halo Namaku \x52\x61\x64\x69\x74"
print(String_Hex_Raw)


print("\n====3. Python String Formatting====\n")

# Urutan default
String_Default = "{} {} {}".format('Vivat', 'Hidup', 'ITS')
print(String_Default)

# Pemformatan Posisi
String_Format = "{1} {0} {2}".format('Vivat', 'Hidup', 'ITS')
print(String_Format)

# Pemformatan dengan Kata Kunci
String_Key_Words = "{h} {u} {g}".format(g='Vivat', u='Hidup', h='ITS')
print(String_Key_Words)

# Pemformatan Bilangan Bulat
String_Format_Bulat = "{0:b}".format(20)
print(String_Format_Bulat)

# Pemformatan Bilangan Desimal
String_Format_String = "{0:e}".format(9028.138493284)
print(String_Format_String)

# Pembulatan Bilangan
String_Pembulatan = "{0:.2f}".format(22/7)
print(String_Pembulatan)

# Penyelarasan String
String_Selaras = "|{:<8}|{:^10}|{:>8}|".format('Vivat','Hidup', 'ITS')
print(String_Selaras)

# Untuk menunjukkan penyelarasan spasi
String_Selaras_Spasi = "\n{0:^10} didirikan pada tahun {1:<3}!".format("ITS",1957)
print(String_Selaras_Spasi)

# Pemformatan Gaya Lama untuk Bilangan Bulat

Integer = 9028.13849328
print('Nilai dari Integer1 adalah %3.2f' % Integer)
print('Nilai dari Integer1 adalah %3.4f' % Integer)
