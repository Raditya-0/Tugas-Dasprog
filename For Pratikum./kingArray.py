t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    Array_i = list(map(int, input().split()))
    q = int(input())
    if q==1:
        max_jumlah = float("-inf")
        for i in range(n):
            cek_jumlah = 0
            for j in range(i, min(i + k, n)):
                cek_jumlah += Array_i[j]
                max_jumlah = max(max_jumlah, cek_jumlah)
        print(max_jumlah)
        
    elif q==2:
        min_jumlah = float("inf")
        for i in range(n):
            cek_jumlah = 0
            for j in range(i, min(i + k, n)):
                cek_jumlah += Array_i[j]
                min_jumlah = min(min_jumlah, cek_jumlah)
        print(min_jumlah)
