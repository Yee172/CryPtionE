from prime_sieve import prime_sieve
from binary_indexed_tree import BinaryIndexedTree


def prime_counting(upper_bound=10 ** 10, **kwargs):
    """Prime counting function
    
    Count prime number below upper_bound with O(n^{3 / 4}) time complexity
    
    Arguments:
        **kwargs {[type]} -- [description]
            with_prime {bool} -- when with_prime is true, this function returns pi and prime

    Keyword Arguments:
        upper_bound {int} -- upper bound (default: {10 ** 10})
    
    Returns:
        function -- pi function, which can count the number of prime numbers in interval [0, n], where n is the input parameter
    """
    with_prime = kwargs.get('with_prime', False)

    tiny_upper_bound = int(upper_bound ** .5) + 2
    tiny_pi, prime = prime_sieve(tiny_upper_bound, only_prime=False, info=False, raw_is_prime=False)
    tiny_pi[0] = 0
    for i in range(1, len(tiny_pi)):
        tiny_pi[i] += tiny_pi[i - 1]

    C = [0] * tiny_upper_bound
    G = [0] * tiny_upper_bound

    def pi(n):
        assert(0 <= n <= upper_bound)
        if n < tiny_upper_bound:
            return tiny_pi[n]
        square_root_of_n = int(n ** .5) + 1
        fourth_root_of_n = int(n ** .25) + 1
        for i in range(1, square_root_of_n + 1):
            C[i] = i
            G[i] = n // i
        k = 0
        while prime[k] < fourth_root_of_n:
            for i in range(1, square_root_of_n):
                d = i * prime[k]
                u = n // d
                if u < square_root_of_n:
                    G[i] -= C[u]
                else:
                    G[i] -= G[d]
            for i in range(square_root_of_n, 0, -1):
                C[i] -= C[i // prime[k]]
            k += 1
        BIT = BinaryIndexedTree(square_root_of_n)
        while k < len(prime) and prime[k] < square_root_of_n:
            last_p = prime[k - 1] if k else 0
            p_square = prime[k] ** 2
            update_upper_bound = n // p_square + 1
            for i in range(1, update_upper_bound):
                d = i * prime[k]
                u = n // d
                if u < square_root_of_n:
                    if u <= last_p:
                        G[i] -= 1
                    else:
                        G[i] -= tiny_pi[u] - k + 1
                else:
                    G[i] -= G[d] - BIT.get_sum(d)
            BIT.add(update_upper_bound, 1)
            k += 1
        return k + G[1] - 1

    if with_prime:
        return pi, prime
    else:
        return pi
