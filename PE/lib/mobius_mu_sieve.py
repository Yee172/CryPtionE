def mobius_mu_sieve(MAXN=10 ** 7, only_mu=False, info=True):
    """Return a list of prime and mu with index up to MAXN
    
    Sieve of Euler in normal way
    
    Keyword Arguments:
        MAXN {int} -- upper bound (default: {10 ** 7})
        only_mu {bool} -- only return the list of mu or plus the list of prime (default: {False})
        info {bool} -- need info or not (default: {True})
    
    Returns:
        list -- a list of prime and mu with index up to MAXN
             or a list of mu with index up to MAXN
    """
    if info:
        print('Sieving prime numbers and their mu...')

    prime = []
    is_prime = [True] * MAXN
    mu = [0] * MAXN
    mu[1] = 1
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, MAXN):
        if is_prime[i]:
            prime.append(i)
            mu[i] = -1
        for x in prime:
            if i * x >= MAXN:
                break
            is_prime[i * x] = False
            if i % x:
                mu[i * x] = -mu[i]
            else:
                mu[i * x] = 0
                break

    if info:
        print('Prime number and mu generated successfully.')

    if only_mu:
        return mu
    else:
        return prime, mu
