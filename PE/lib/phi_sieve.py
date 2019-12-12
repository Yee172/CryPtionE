def phi_sieve(upper_bound=10 ** 7, only_phi=False, info=True, **kwargs):
    """Return a list of prime and phi with index up to upper_bound
    
    Sieve of Euler in normal way
    
    Arguments:
        **kwargs {[type]} -- [description]
            function_phi {bool} -- this argument determines whether return the
                                   phi function that can calculate up to upper_bound ** 2

    Keyword Arguments:
        upper_bound {int} -- upper bound (default: {10 ** 7})
        only_phi {bool} -- only return the list of phi or plus the list of prime (default: {False})
        info {bool} -- need info or not (default: {True})
    
    Returns:
        list -- a list of prime and phi with index up to upper_bound
             or a list of phi with index up to upper_bound
    """
    if info:
        print('Sieving prime numbers and their phi...')

    prime = []
    is_prime = [True] * upper_bound
    phi = [0] * upper_bound
    is_prime[0] = False
    if upper_bound > 1:
        is_prime[1] = False
        phi[1] = 1
    for i in range(2, upper_bound):
        if is_prime[i]:
            prime.append(i)
            phi[i] = i - 1
        for x in prime:
            if i * x >= upper_bound:
                break
            is_prime[i * x] = False
            if i % x:
                phi[i * x] = phi[i] * (x - 1)
            else:
                phi[i * x] = phi[i] * x
                break

    def function_phi(n):
        if n < upper_bound:
            return phi[n]
        result = n
        for p in prime:
            if p * p > n:
                break
            if not n % p:
                result = result // p * (p - 1)
                while not n % p:
                    n //= p
        if n > 1:
            result = result // n * (n - 1)
        return result

    phi_return = phi
    if kwargs.get('function_phi', False):
        phi_return = function_phi

    if info:
        print('Prime number and phi generated successfully.')

    if only_phi:
        return phi_return
    else:
        return prime, phi_return
