from extended_gcd import extended_gcd

def Chinese_remainder_theorem(M, R):
    """Chinese remainder theorem
    
    extended Chinese remainder theorem, can deal with the situation of not relatively prime
    
    Arguments:
        M {list/tuple} -- a list of divisors
        R {list/tuple} -- a list of remainders
    
    Returns:
        tuple -- if has solution: minimum non-negative result and the corresponding divisor
                 if has no solution: -1, 0
    
    Raises:
        ArithmeticError -- the length of M be equal to the length of R
        TypeError -- M and R must be a sequence of number
    """
    try:
        if not len(M) == len(R):
            raise ArithmeticError('the length of M be equal to the length of R')
    except:
        raise TypeError('M and R must be a sequence of number')
    m1 = M[0]
    r1 = R[0]
    for m2, r2 in zip(M, R):
        d, x, y = [0], [0], [0]
        extended_gcd(m1, m2, d, x, y)
        c = r2 - r1
        if c % d[0]:
            # no solution
            break
        d = d[0]
        x = x[0]
        t = m2 // d
        x = c // d * x % t
        r1 += m1 * x;
        m1 = m1 // d * m2
    else:
        return r1, m1
        # r1 could be 0
        # result = r1 + k * m1, where k is non-negative integer
    return -1, 0
