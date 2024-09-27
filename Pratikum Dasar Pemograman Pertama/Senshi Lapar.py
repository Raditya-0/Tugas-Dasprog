X, Y = input().split()
x, y = input().split()
X, Y = int(X), int(Y)
x, y = int(x), int(y)
M = int(input())
if (x == 0 and y == 0) or (x == 0 and y == Y) or (x == X and y == 0) or (x == X and y == Y):
    kk = 3
elif(x == 0) or (y == 0) or (x == X) or (y == Y):
    kk = 5
else:
    kk = 8

makan = bool(True)

if M == 1:
    x1, y1 = input().split()
    x1, y1 = int(x1), int(y1)
    makan = True
elif M == 2:
    x1, y1 = input().split()
    x1, y1 = int(x1), int(y1)
    x2, y2 = input().split()
    x2, y2 = int(x2), int(y2)
    makan = True
elif M == 3:
    x1, y1 = input().split()
    x1, y1 = int(x1), int(y1)
    x2, y2 = input().split()
    x2, y2 = int(x2), int(y2)
    x3, y3 = input().split()
    x3, y3 = int(x3), int(y3)
    if (x+1 == x1 or x-1 == x1) or (y+1 == y1 or y-1 == y1):
        kk -= 1
    if (x+1 == x2 or x-1 == x2) or (y+1 == y2 or y-1 == y2):
        kk -= 1
    if (x+1 == x3 or x-1 == x3) or (y+1 == y3 or y-1 == y3):
        kk -= 1
elif M == 4:
    x1, y1 = input().split()
    x1, y1 = int(x1), int(y1)
    x2, y2 = input().split()
    x2, y2 = int(x2), int(y2)
    x3, y3 = input().split()
    x3, y3 = int(x3), int(y3)
    x4, y4 = input().split()
    x4, y4 = int(x4), int(y4)
    if (x+1 == x1 or x-1 == x1) or (y+1 == y1 or y-1 == y1):
        kk -= 1
    if (x+1 == x2 or x-1 == x2) or (y+1 == y2 or y-1 == y2):
        kk -= 1
    if (x+1 == x3 or x-1 == x3) or (y+1 == y3 or y-1 == y3):
        kk -= 1
    if (x+1 == x4 or x-1 == x4) or (y+1 == y4 or y-1 == y4):
        kk -= 1
elif M == 5:
    x1, y1 = input().split()
    x1, y1 = int(x1), int(y1)
    x2, y2 = input().split()
    x2, y2 = int(x2), int(y2)
    x3, y3 = input().split()
    x3, y3 = int(x3), int(y3)
    x4, y4 = input().split()
    x4, y4 = int(x4), int(y4)
    x5, y5 = input().split()
    x5, y5 = int(x5), int(y5)
    if (x+1 == x1 or x-1 == x1) or (y+1 == y1 or y-1 == y1):
        kk -= 1
    if (x+1 == x2 or x-1 == x2) or (y+1 == y2 or y-1 == y2):
        kk -= 1
    if (x+1 == x3 or x-1 == x3) or (y+1 == y3 or y-1 == y3):
        kk -= 1
    if (x+1 == x4 or x-1 == x4) or (y+1 == y4 or y-1 == y4):
        kk -= 1
    if (x+1 == x5 or x-1 == x5) or (y+1 == y5 or y-1 == y5):
        kk -= 1
elif M == 6:
    x1, y1 = input().split()
    x1, y1 = int(x1), int(y1)
    x2, y2 = input().split()
    x2, y2 = int(x2), int(y2)
    x3, y3 = input().split()
    x3, y3 = int(x3), int(y3)
    x4, y4 = input().split()
    x4, y4 = int(x4), int(y4)
    x5, y5 = input().split()
    x5, y5 = int(x5), int(y5)
    x6, y6 = input().split()
    x6, y6 = int(x6), int(y6)
    if (x+1 == x1 or x-1 == x1) or (y+1 == y1 or y-1 == y1):
        kk -= 1
    if (x+1 == x2 or x-1 == x2) or (y+1 == y2 or y-1 == y2):
        kk -= 1
    if (x+1 == x3 or x-1 == x3) or (y+1 == y3 or y-1 == y3):
        kk -= 1
    if (x+1 == x4 or x-1 == x4) or (y+1 == y4 or y-1 == y4):
        kk -= 1
    if (x+1 == x5 or x-1 == x5) or (y+1 == y5 or y-1 == y5):
        kk -= 1
    if (x+1 == x6 or x-1 == x6) or (y+1 == y6 or y-1 == y6):
        kk -= 1
elif M == 7:
    x1, y1 = input().split()
    x1, y1 = int(x1), int(y1)
    x2, y2 = input().split()
    x2, y2 = int(x2), int(y2)
    x3, y3 = input().split()
    x3, y3 = int(x3), int(y3)
    x4, y4 = input().split()
    x4, y4 = int(x4), int(y4)
    x5, y5 = input().split()
    x5, y5 = int(x5), int(y5)
    x6, y6 = input().split()
    x6, y6 = int(x6), int(y6)
    x7, y7 = input().split()
    x7, y7 = int(x7), int(y7)
    if (x+1 == x1 or x-1 == x1)or (y+1 == y1 or y-1 == y1):
        kk -= 1
    if (x+1 == x2 or x-1 == x2)or (y+1 == y2 or y-1 == y2):
        kk -= 1
    if (x+1 == x3 or x-1 == x3)or (y+1 == y3 or y-1 == y3):
        kk -= 1
    if (x+1 == x4 or x-1 == x4)or (y+1 == y4 or y-1 == y4):
        kk -= 1
    if (x+1 == x5 or x-1 == x5)or (y+1 == y5 or y-1 == y5):
        kk -= 1
    if (x+1 == x6 or x-1 == x6)or (y+1 == y6 or y-1 == y6):
        kk -= 1
    if (x+1 == x7 or x-1 == x7)or (y+1 == y7 or y-1 == y7):
        kk -= 1
elif M == 8:
    x1, y1 = input().split()
    x1, y1 = int(x1), int(y1)
    x2, y2 = input().split()
    x2, y2 = int(x2), int(y2)
    x3, y3 = input().split()
    x3, y3 = int(x3), int(y3)
    x4, y4 = input().split()
    x4, y4 = int(x4), int(y4)
    x5, y5 = input().split()
    x5, y5 = int(x5), int(y5)
    x6, y6 = input().split()
    x6, y6 = int(x6), int(y6)
    x7, y7 = input().split()
    x7, y7 = int(x7), int(y7)
    x8, y8 = input().split()
    x8, y8 = int(x8), int(y8)
    if (x+1 == x1 or x-1 == x1) or (y+1 == y1 or y-1 == y1):
        kk -= 1
    if (x+1 == x2 or x-1 == x2) or (y+1 == y2 or y-1 == y2):
        kk -= 1
    if (x+1 == x3 or x-1 == x3) or (y+1 == y3 or y-1 == y3):
        kk -= 1
    if (x+1 == x4 or x-1 == x4) or (y+1 == y4 or y-1 == y4):
        kk -= 1
    if (x+1 == x5 or x-1 == x5) or (y+1 == y5 or y-1 == y5):
        kk -= 1
    if (x+1 == x6 or x-1 == x6) or (y+1 == y6 or y-1 == y6):
        kk -= 1
    if (x+1 == x7 or x-1 == x7) or (y+1 == y7 or y-1 == y7):
        kk -= 1
    if (x+1 == x8 or x-1 == x8) or (y+1 == y8 or y-1 == y8):
        kk -= 1
elif M == 0:
    kk = 0

#print(kk)

if kk > 0:
    print("Senshi makan hari ini!")
else:
    print("Senshi makannya besok aja deh.")