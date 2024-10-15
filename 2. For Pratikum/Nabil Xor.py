N = int(input())

for _ in range(N):
    bilangan = list(map(int, input().split()))

    hasil = 1    
    for i in range(len(bilangan)):
        for k in range(i + 1, len(bilangan)):
            hasil_XOR = bilangan[i] ^ bilangan[k]

            
            if hasil_XOR == 0:
                hasil = 0  
                break  
            else:
                hasil *= hasil_XOR
    print(hasil)
    break
