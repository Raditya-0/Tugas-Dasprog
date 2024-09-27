
def hitung_fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def hitung_kpk(a, b, fpb):
    return (a * b) // fpb

a, b = map(int, input().split())

fpb = hitung_fpb(a, b)
kpk = hitung_kpk(a, b, fpb)

print((fpb*kpk)//a + (fpb*kpk)//b)
