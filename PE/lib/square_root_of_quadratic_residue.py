from quadratic_field import generate_quadratic_field


def square_root_of_quadratic_residue(n, modulo):
    """Square root of quadratic residue
    
    Solve the square root of quadratic residue using Cipolla's algorithm with Legendre symbol
    
    Arguments:
        n {int} -- quadratic residue
        modulo {int} -- the corresponding modulo, which should be an odd prime number
    
    Returns:
        int -- if n is a quadratic residue,
                   return x, such that x^{2} = n (mod modulo)
               otherwise,
                   return -1
    """
    assert(isinstance(modulo, int) and modulo > 0)
    if modulo == 2:
        return 1
    if n % modulo == 0:
        return 0
    Legendre = lambda n: pow(n, modulo - 1 >> 1, modulo)
    if Legendre(n) == modulo - 1:
        return -1
    t = 0
    while Legendre(t ** 2 - n) != modulo - 1:
        t += 1
    w = (t ** 2 - n) % modulo
    return (generate_quadratic_field(w, modulo)(t, 1) ** (modulo + 1 >> 1)).x
