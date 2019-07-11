def extended_gcd(a, b, d, x, y):
    """Extended gcd
    
    a x + b y = d = gcd(x, y)
    
    Arguments:
        a {int} -- a
        b {int} -- b
        d {int *} -- gcd(x, y)
        x {int *} -- x
        y {int *} -- y
    """
    if not b:
        d[0] = a
        x[0] = 1
        y[0] = 0
    else:
        extended_gcd(b, a % b, d, y, x)
        y[0] -= x[0] * (a // b)

def inverse(n, modulo):
    """Inverse of n
    
    inverse(n, modulo) * n % modulo = 1
    
    Arguments:
        n {int} -- n
        modulo {int} -- modulo
    
    Returns:
        int -- inverse of n
    """
    d, x, y = [0], [0], [0]
    extended_gcd(n, modulo, d, x, y)
    return x[0] % modulo
