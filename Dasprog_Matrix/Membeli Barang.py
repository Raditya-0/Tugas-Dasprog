N, M = map(int, input().split())
barang = list(map(int, input().split()))
uang = list(map(int, input().split()))

min_barang = min(barang)
max_barang = max(barang)
min_uang = min(uang)
max_uang = max(uang)

hutang = 0

is_positive_barang = min_barang > 0 and max_barang > 0  
is_negative_barang = min_barang < 0 and max_barang < 0  
is_positive_uang = min_uang > 0 and max_uang > 0         
is_negative_uang = min_uang < 0 and max_uang < 0         


if is_positive_barang and is_positive_uang:
    hutang = min_uang - sum(barang)
elif is_negative_barang and is_negative_uang:
    hutang = sum(uang) - max_barang
elif is_negative_barang and is_positive_uang:
    hutang = min(uang) - max(barang)
else:
    belanja = sum(item for item in barang if item > 0)  
    bayar = sum(item for item in uang if item < 0)     
    hutang = bayar - belanja

print(hutang)
