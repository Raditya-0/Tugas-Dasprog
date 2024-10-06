N, r, c = map(int, input().split())
posisi = [list(map(int, input().split())) for _ in range(N)]
matrix = [[0] * c for _ in range(r)]

for murid, baris_index, kolom_index in posisi:
    matrix[baris_index - 1][kolom_index - 1] = murid

for murid, baris_index, kolom_index in posisi:
    baris = baris_index - 1  
    kolom = kolom_index - 1  
    
    if kolom > 0 and matrix[baris][kolom - 1] != 0:
        print(matrix[baris][kolom - 1])
    elif kolom < c - 1 and matrix[baris][kolom + 1] != 0:
        print(matrix[baris][kolom + 1])
    else:
        print(0)

