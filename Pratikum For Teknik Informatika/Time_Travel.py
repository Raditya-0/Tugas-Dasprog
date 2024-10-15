def save_world_or_fail(N, M, F):
    for K in range(F + 1):
        max_travel = (N ^ K) - 1
        if max_travel >= M:
            print("HAHAHA, I CAN SAVE THE WORLD")
            return
    print("OH NOOO, I FAILED")

N, M, F = map(int, input().split())
save_world_or_fail(N, M, F)
