while True:
    try:
        N, M = map(int, input("Masukkan dua bilangan N dan M : ").split())

        if M > N or N <= 0 or M <= 0:
            print("N harus lebih besar dari M dan keduanya harus positif.")
        else:
            break
    except ValueError:
        print("Input harus berupa angka bulat.")
        continue


for i in range(N):
    if i < M or i >= N - M:
        print('*' * N)
    else:
        print('*' * M + ' ' * (N - 2 * M) + '*' * M)

