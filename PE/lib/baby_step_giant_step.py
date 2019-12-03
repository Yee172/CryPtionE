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
            guess_limit {int} -- the maximum guess attempt times from x equals 0, the guessing range is
                                 [0, guess_limit), and guess_limit must be at least 1 (default: {100})
    
    Returns:
        int -- the smallest non-negative solution of the equation or -1
    """
    guess_attempt = 1
    guess_limit = max(1, kwargs.get('guess_limit', 100))
    for guess in range(guess_limit):
        if guess_attempt == B:
            return guess
        guess_attempt = guess_attempt * A % C

    splitted_A = 1
    baby_step_shift = 0
    G = gcd(A, C)
    while G ^ 1:
        if B % G:
            return -1
        baby_step_shift += 1
        C //= G
        B //= G
        splitted_A = A // G * splitted_A % C
        G = gcd(C, G)

    baby_step_mapping = dict()
    M = integer_sqrt(C)
    baby_step_value = 1
    for baby_step in range(M + 1):
        if baby_step_value not in baby_step_mapping:
            baby_step_mapping[baby_step_value] = baby_step
        baby_step_value = baby_step_value * A % C

    giant_step_length = pow(inverse(A, C), M, C)
    giant_step_value = inverse(splitted_A, C) * B % C
    for giant_step in range(M + 1):
        if giant_step_value in baby_step_mapping:
            return giant_step * M + baby_step_mapping[giant_step_value] + baby_step_shift
        giant_step_value = giant_step_value * giant_step_length % C
    return -1
