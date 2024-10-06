r, c, n = list(map(int, input().split()))
peta = []
for _ in range(r):
    peta.append(list(map(int, input().split())))
moves = input()
pos_i, pos_j = 0, 0
jum_gold = peta[0][0]
gerakansalah = False

def is_valid(i, j):
    return 0 <= i <= r and 0 <= j <= c

for move in moves:
    if move == 'L':
        pos_j -= 1
        if is_valid(pos_i, pos_j):
            jum_gold -= 2
    elif move == 'R':
        pos_j += 1
        if is_valid(pos_i, pos_j):
            jum_gold += 3
    elif move == 'U':
        pos_i -= 1
        if is_valid(pos_i, pos_j):
            jum_gold += 3
    elif move == 'D':
        pos_i += 1
        if is_valid(pos_i, pos_j):
            jum_gold -= 2
    
    if not is_valid(pos_i, pos_j):
        gerakansalah = True
        break
    
    jum_gold += peta[pos_i][pos_j]

if gerakansalah:
    print("gerakanmu salah bung!")
    print(f"Jumlah gold Pak Dengklek : {jum_gold}")
else:
    print(f"Jumlah gold Pak Dengklek : {jum_gold}")