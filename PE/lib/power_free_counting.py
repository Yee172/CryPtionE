from prime_sieve import prime_sieve
from integer_operation import integer_kth_root


__all__ = ['SquareFreeCounting', 'CubeFreeCounting', 'PowerFreeCounting']


class PowerFreeCounting:
    """Power Free Counting Prototype
    
    Let S(n) denote the number of power-free positive integers less than or equal to n
    According to the inclusion-exclusion principle, we have
    S(n) = \\sum_{d = 1}^{n^{1 / p}} \\mu(d) n // d ** p,
    where \\mu is the Mobius function
    """
    def __init__(self, p, N, prime=None):
        self.p = p # power
        self.N = N # counting upper bound
        self.prime = prime_sieve(integer_kth_root(self.N, self.p) + 1, info=False) if prime is None else prime
        self.prime_length = len(self.prime)

    def _count(self, prime_index, n):
        result = n
        for i in range(prime_index, self.prime_length):
            prime_power = self.prime[i] ** self.p
            if prime_power > n:
                break
            result -= self._count(i + 1, n // prime_power)
        return result

    def count(self, n):
        return self._count(0, n)


class SquareFreeCounting(PowerFreeCounting):
    """Sqaure Free Counting
    
    count square-free numbers
    
    Extends:
        PowerFreeCounting
    """
    def __init__(self, N, prime=None):
        super().__init__(2, N, prime)


class CubeFreeCounting(PowerFreeCounting):
    """Cube Free Counting
    
    count cube-free numbers
    
    Extends:
        PowerFreeCounting
    """
    def __init__(self, N, prime=None):
        super().__init__(3, N, prime)
