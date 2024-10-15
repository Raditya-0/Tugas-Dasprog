def prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

T = int(input())
N = list(map(int, input().split()))
list = {}
for harga in N:
    if harga in list:
        list[harga] += 1
    else:
        list[harga] = 1

max_list = max(list.values())
modus = [harga for harga, hitung in list.items() if hitung == max_list]
modus_max = max(modus)

print(f"Modus: {modus_max}")
if prima(modus_max):
    print("Wah, modusnya prima nihh.")
else:
    print("Yah, modusnya gak prima.")