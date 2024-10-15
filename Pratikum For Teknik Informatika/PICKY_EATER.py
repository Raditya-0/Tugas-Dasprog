n = int(input())
list_buah = list(map(int, input().split()))

buah_counts = {}
for buah in list_buah:
    if buah in buah_counts:
        buah_counts[buah] += 1
    else:
        buah_counts[buah] = 1

modus = [fruit for fruit, count in buah_counts.items() if count == max(buah_counts.values())]

if len(modus) == 1:
    modus_0 = modus[0]
    perubahan = sum(count for fruit, count in buah_counts.items() if fruit != modus_0)
    print(modus_0)
    print(perubahan)
else:
    print(-1)