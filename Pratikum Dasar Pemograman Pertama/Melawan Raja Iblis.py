U = int(input())
K = int(input())
M = int(input())

# Minion
Minion_Sehat = M // 2 # Minion dibagi setengah karena kena beku
Damage_Minion = Minion_Sehat * 2
Serang_Minion = 100/100
Damage_Total_Minion = Damage_Minion * Serang_Minion
print(Damage_Total_Minion)

# Knight
Knight_sehat = K // 2 # Knight dibagi setengah karena kena beku
Damage_Knight = Knight_sehat * 5
Serang_Knight = 500/100
Damage_Total_Knight = Damage_Knight * Serang_Knight
print(Damage_Total_Knight)

# Raja Iblis
Damage_Raja_Iblis = 100
Health_Raja_Iblis = 1000 
Serang_Raja_Iblis = Health_Raja_Iblis / 100
Damage_Total_Raja_Iblis = Damage_Raja_Iblis * Serang_Raja_Iblis
print(Serang_Raja_Iblis)

Damage_Total = Damage_Total_Minion + Damage_Total_Knight + Damage_Total_Raja_Iblis
print(Damage_Total)

if U > Damage_Total:
    U -= Damage_Total
    print(f"Yey! Ucup Menang! HP tersisa: {round(U)}")
else:
    print('Yah! Ucup Meninggoy.')
