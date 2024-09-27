batas = 10**6  
prima = [True] * (batas + 1) 
prima[0] = prima[1] = False 


for i in range(2, int(batas**0.5) + 1):
    if prima[i]: 
        for j in range(i * i, batas + 1, i):  
            prima[j] = False

primas = []
for i in range(batas + 1):
    if prima[i]: 
        primas.append(i) 

jumlah_kasus = int(input().strip())  

kasus_uji = []
for _ in range(jumlah_kasus):
    A, B = map(int, input().split())  
    kasus_uji.append((A, B))  


for t in range(1, jumlah_kasus + 1):
    A, B = kasus_uji[t-1]  
    print(f"Kasus Uji #{t} :") 
    
    
    for indeks in range(A-1, B):
        if indeks != B-1:
            print(primas[indeks], end=" ")  
        else:
            print(primas[indeks])  
