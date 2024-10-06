while True:
  try:
    N, K = map(int, input().split())
    harga_buah = list(map(int, input().split()))
    if 1 <= N <= 10 ** 5 and 1 <= K <= 10 ** 12:
        break
    else:
       print("Masukan tidak valid")
       continue
  except ValueError:
     print("Masukkan harus berupa angka")

jumlah_buah = 0

for harga in harga_buah:
    if harga <= K:
        jumlah_buah += 1

print(jumlah_buah)