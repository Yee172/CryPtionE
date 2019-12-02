from math import gcd
from extended_gcd import inverse
from integer_operation import integer_sqrt


def baby_step_giant_step(A, B, C, **kwargs):
    """Baby step giant step
    
    Using baby step giant step method to solve the equation of A^{x} \equiv B (mod C) with given A, B and C
    
    Arguments:
        A {int} -- A
        B {int} -- B
        C {int} -- C
        **kwargs {[type]} -- [description]
            guess_limit {int} -- the maximum guess attempt times from x equals 0 (default: {100})
                                 [0, guess_limit)
    
    Returns:
        int -- the smallest positive solution of the equation or -1
    """
    guess_attempt = 1
    guess_limit = kwargs.get('guess_limit', 100)
    baby_step_mapping = dict()
    for guess in range(guess_limit):
        if guess_attempt == B:
            return guess
        if guess_attempt not in baby_step_mapping:
            baby_step_mapping[guess_attempt] = guess
        guess_attempt = guess_attempt * A % C

    D = 1
    d = 0
    tmp = gcd(A, C)
    while tmp ^ 1:
        if B % tmp:
            return -1
        d += 1
        C //= tmp
        B //= tmp
        D = D * A // tmp % C
        tmp = gcd(A, C)

    M = integer_sqrt(C)
    for i in range(guess_limit, M + 1):
        if guess_attempt not in baby_step_mapping:
            baby_step_mapping[guess_attempt] = i
        guess_attempt = guess_attempt * A % C

    K = pow(A, M, C)
    for i in range(M + 1):
        tmp = inverse(D, C) * B % C
        if tmp in baby_step_mapping:
            return i * M + baby_step_mapping[tmp] + d
        D = D * K % C
    return -1
