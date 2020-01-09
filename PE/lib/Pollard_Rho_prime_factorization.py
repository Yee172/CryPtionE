from math import gcd
from Miller_Rabin_primality_test import random, Miller_Rabin_primality_test


def Pollard_Rho_prime_factorization(n):
    if n & 1 ^ 1:
        return 2
    if not n % 3:
        return 3
    M = (1 << 7) - 1
    x, y, t, q, c = 0, 0, 1, 1, random.randint(1, n - 1)
    k = 2
    while True:
        for i in range(1, k + 1):
            x = (x ** 2 + c) % n
            q = q * abs(x - y) % n
            if not i & M:
                t = gcd(q, n)
                if t > 1:
                    break
        if t > 1:
            break
        t = gcd(q, n)
        if t > 1:
            break
        k <<= 1
        y = x
        q = 1
    return t


def get_max_prime_factor(n):
    maximum_prime_factor = [0]

    def get_max_prime_factor_dfs(n):
        if n == 1 or n <= maximum_prime_factor[0]:
            return
        if Miller_Rabin_primality_test(n):
            if n > maximum_prime_factor[0]:
                maximum_prime_factor[0] = n
            return
        p = n
        while p == n:
            p = Pollard_Rho_prime_factorization(n)
        while not n % p:
            n //= p
        get_max_prime_factor_dfs(p)
        get_max_prime_factor_dfs(n)

    get_max_prime_factor_dfs(n)
    return maximum_prime_factor[0]
