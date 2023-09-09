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


def find_maximum_prime_factor(n):
    maximum_prime_factor = [0]

    def find_maximum_prime_factor_dfs(n):
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
        find_maximum_prime_factor_dfs(p)
        find_maximum_prime_factor_dfs(n)

    find_maximum_prime_factor_dfs(n)
    return maximum_prime_factor[0]


def find_minimum_prime_factor(n):
    minimum_prime_factor = [n]

    def find_minimum_prime_factor_dfs(n):
        if n == 1:
            return
        if Miller_Rabin_primality_test(n):
            if n < minimum_prime_factor[0]:
                minimum_prime_factor[0] = n
            return
        p = n
        while p == n:
            p = Pollard_Rho_prime_factorization(n)
        while not n % p:
            n //= p
        find_minimum_prime_factor_dfs(p)
        find_minimum_prime_factor_dfs(n)

    find_minimum_prime_factor_dfs(n)
    return minimum_prime_factor[0]


def prime_factorization(n):
    prime_factors = []

    def prime_factorization_dfs(n):
        if n == 1:
            return
        if Miller_Rabin_primality_test(n):
            prime_factors.append(n)
            return
        p = n
        while p == n:
            p = Pollard_Rho_prime_factorization(n)
        prime_factorization_dfs(p)
        prime_factorization_dfs(n // p)

    prime_factorization_dfs(n)
    if not prime_factors:
        return []
    prime_factors.sort()
    p = prime_factors[0]
    p_counter = 0
    result = []
    for q in prime_factors:
        if q == p:
            p_counter += 1
        else:
            result.append((p, p_counter))
            p = q
            p_counter = 1
    result.append((p, p_counter))
    return result


def get_all_divisors(n):
    all_divisors = [1]

    for p, e in prime_factorization(n):
        p_power = [1]
        while e:
            p_power.append(p_power[- 1] * p)
            e -= 1
        next_all_divisors = []
        for a in all_divisors:
            for b in p_power:
                next_all_divisors.append(a * b)
        all_divisors = next_all_divisors

    all_divisors.sort()
    return all_divisors


def get_phi(n):
    assert(n > 0)
    result = 1
    for p, c in prime_factorization(n):
        result *= (p - 1) * p ** (c - 1)
    return result


def get_mu(n):
    assert(n > 0)
    result = 1
    for p, c in prime_factorization(n):
        if c > 1:
            result = 0
            break
        result *= -1
    return result
