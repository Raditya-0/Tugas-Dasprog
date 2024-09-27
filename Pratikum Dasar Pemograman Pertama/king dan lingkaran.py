x1, y1 = map(int, input().split())  
xs, ys = map(int, input().split())
xf, yf = map(int, input().split()) 

if (-10**25 <= x1 <= 10**25) and (-10**25 <= y1 <= 10**25) and (-10**25 <= xs <= 10**25) and (-10**25 <= ys <= 10**25) and (-10**25 <= xf <= 10**25) and (-10**25 <= yf <= 10**25):
    jarak_king = ((xs - xf) ** 2 + (ys - yf) ** 2) 
    jarak_lingkaran_ke_akhir = ((x1 - xf) ** 2 + (y1 - yf) ** 2) 

if jarak_lingkaran_ke_akhir > jarak_king:    
    print("Yes")
else:
    print("No")