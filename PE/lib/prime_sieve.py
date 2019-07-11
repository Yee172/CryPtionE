def prime_sieve(MAXN=10 ** 7, only_prime=True, info=True, **kwargs):
    """Return a list of prime with index up to MAXN
    
    if bitarray is installed:
        Sieve of Eratosthenes (Learnt from code of epiclolz)
        PS: faster because of the operation of bitarray
    else:
        Sieve of Euler in normal way

    Arguments:
        **kwargs {[type]} -- [description]
            raw_is_prime {bool} -- when only_prime is False, this argument determines whether
                                   return the raw is_prime list of the faster way (default: {False})
            function_is_prime {bool} -- when only_prime is False, this argument determines whether
                                        return the prime test function that can test up to MAXN ** 2
    
    Keyword Arguments:
        MAXN {int} -- upper bound (default: {10 ** 7})
        only_prime {bool} -- whether only return prime or with the list of is_prime
        info {bool} -- need info or not (default: {True})
    
    Returns:
        list -- a list of prime with index up to MAXN
    """
    function_is_prime = kwargs.get('function_is_prime', False)

    if info:
        print('Sieving prime numbers...')

    try:
        if info:
            print('Trying using bitarray to accelerate the speed...')

        from bitarray import bitarray
        is_prime = bitarray(MAXN >> 1)
        is_prime.setall(1)
        is_prime[0] = 0
        for i in range(1, int(MAXN ** .5)):
            if is_prime[i]:
                is_prime[2 * i ** 2 + 2 * i::2 * i + 1] = 0
        prime = [2] + [i * 2 + 1 for i in is_prime.search(bitarray([1]))]

        if not only_prime:
            if function_is_prime:
                def naive_is_prime(n):
                    return bool(n & 1 and is_prime[n >> 1]) or n == 2

            elif not kwargs.get('raw_is_prime', False):
                is_prime = [bool(i & 1 and is_prime[i >> 1]) for i in range(MAXN)]
                is_prime[2] = True
    except:
        if info:
            print('Something was wrong with bitarray, using the sieve of Euler in normal way...')

        prime = []
        is_prime = [True] * MAXN
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, MAXN):
            if is_prime[i]:
                prime.append(i)
            for x in prime:
                if i * x >= MAXN:
                    break
                is_prime[i * x] = False
                if not i % x:
                    break

        if not only_prime and function_is_prime:
            def naive_is_prime(n):
                return is_prime[n]
    
    if info:
        print('Prime number generated successfully.')

    if only_prime:
        return prime
    else:
        if function_is_prime:
            def check_is_prime(n):
                if n < MAXN:
                    return naive_is_prime(n)
                for p in prime:
                    if p * p > n:
                        break
                    if not n % p:
                        return False
                return True

            return check_is_prime, prime
        else:
            return is_prime, prime
