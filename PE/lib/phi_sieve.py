def phi_sieve(MAXN=10 ** 7, only_phi=False, info=True):
    """Return a list of prime and phi with index up to MAXN
    
    Sieve of Euler in normal way
    
    Keyword Arguments:
        MAXN {int} -- upper bound (default: {10 ** 7})
        only_phi {bool} -- only return the list of phi or plus the list of prime (default: {False})
        info {bool} -- need info or not (default: {True})
    
    Returns:
        list -- a list of prime and phi with index up to MAXN
             or a list of phi with index up to MAXN
    """
    if info:
        print('Sieving prime numbers and their phi...')

    prime = []
    is_prime = [True] * MAXN
    phi = [0] * MAXN
    is_prime[0] = False
    is_prime[1] = False
    phi[1] = 1
    for i in range(2, MAXN):
        if is_prime[i]:
            prime.append(i)
            phi[i] = i - 1
        for x in prime:
            if i * x >= MAXN:
                break
            is_prime[i * x] = False
            if i % x:
                phi[i * x] = phi[i] * (x - 1)
            else:
                phi[i * x] = phi[i] * x
                break

    if info:
        print('Prime number and phi generated successfully.')

    if only_phi:
        return phi
    else:
        return prime, phi
