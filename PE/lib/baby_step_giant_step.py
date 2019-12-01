from math import gcd
from extended_gcd import inverse

def baby_step_giant_step(A, B, C):
    # A^x = B (mod C)
    buf = 1
    D = buf
    d = 0
    tmp = gcd(A, C)
    for i in range(100):
        if buf == B:
            return i
        buf = buf * A % C
    while tmp ^ 1:
        if B % tmp:
            return -1
        d += 1
        C //= tmp
        B //= tmp
        D = D * A // tmp % C
        tmp = gcd(A, C)
    H = dict()
    M = int(C ** .5)
    while M ** 2 < C:
        M += 1
    buf = 1
    for i in range(M + 1):
        if buf not in H:
            H[buf] = i
        buf = buf * A % C
    K = pow(A, M, C)
    for i in range(M + 1):
        tmp = inverse(D, C) * B % C
        if tmp in H:
            return i * M + H[tmp] + d
        D = D * K % C
    return -1
