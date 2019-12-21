"""A library of sequences

This library is set for various of sequences
"""

from linear_recursion import LinearRecursion


def Horadam(p, q, r, s, **kwargs):
    """Fibonacci sequence
    
    Horadam[0] = p, Horadam[1] = q,
    Horadam[n] = r * Horadam[n - 1] + s * Horadam[n - 2]
    
    Arguments:
        p {int} -- p
        q {int} -- q
        r {int} -- r
        s {int} -- s
        **kwargs {[type]} -- [description]
            modulo[int] -- modulo (default: {0})
    
    Returns:
        LinearRecursion -- Horadam sequence
    """
    return LinearRecursion([p, q], [r, s], modulo=kwargs.get('modulo', 0))

def Fibonacci(**kwargs):
    """Fibonacci sequence
    
    Fibonacci[0] = 0, Fibonacci[1] = 1,
    Fibonacci[n] = Fibonacci[n - 1] + Fibonacci[n - 2]
    
    Arguments:
        **kwargs {[type]} -- [description]
            modulo[int] -- modulo (default: {0})
    
    Returns:
        LinearRecursion -- Fibonacci sequence
    """
    return Horadam(0, 1, 1, 1, **kwargs)

def Lucas(**kwargs):
    """Lucas sequence
    
    Lucas[0] = 2, Lucas[1] = 1,
    Lucas[n] = Lucas[n - 1] + Lucas[n - 2]
    
    Arguments:
        **kwargs {[type]} -- [description]
            modulo[int] -- modulo (default: {0})
    
    Returns:
        LinearRecursion -- Lucas sequence
    """
    return Horadam(2, 1, 1, 1, **kwargs)

def Pell(**kwargs):
    """Pell sequence
    
    Pell[0] = 0, Pell[1] = 1,
    Pell[n] = 2 Pell[n - 1] + Pell[n - 2]
    
    Arguments:
        **kwargs {[type]} -- [description]
            modulo[int] -- modulo (default: {0})
    
    Returns:
        LinearRecursion -- Pell sequence
    """
    return Horadam(0, 1, 2, 1, **kwargs)

def Pell_Lucas(**kwargs):
    """Pell_Lucas sequence
    
    Pell_Lucas[0] = 2, Pell_Lucas[1] = 2,
    Pell_Lucas[n] = 2 Pell_Lucas[n - 1] + Pell_Lucas[n - 2]
    
    Arguments:
        **kwargs {[type]} -- [description]
            modulo[int] -- modulo (default: {0})
    
    Returns:
        LinearRecursion -- Pell_Lucas sequence
    """
    return Horadam(2, 2, 2, 1, **kwargs)

def Tribonacci(**kwargs):
    """Tribonacci sequence
    
    Tribonacci[0] = 0, Tribonacci[1] = 0, Tribonacci[2] = 1,
    Tribonacci[n] = Tribonacci[n - 1] + Tribonacci[n - 2] + Tribonacci[n - 3]
    
    Arguments:
        **kwargs {[type]} -- [description]
            modulo[int] -- modulo (default: {0})

    Returns:
        LinearRecursion -- Tribonacci sequence
    """
    return LinearRecursion([0, 0, 1], [1, 1, 1], modulo=kwargs.get('modulo', 0))

def Padovan(**kwargs):
    """Padovan sequence
    
    Padovan[0] = 1, Padovan[1] = 0, Padovan[2] = 0,
    Padovan[n] = Padovan[n - 2] + Padovan[n - 3]
    
    Arguments:
        **kwargs {[type]} -- [description]
            modulo[int] -- modulo (default: {0})

    Returns:
        LinearRecursion -- Padovan sequence
    """
    return LinearRecursion([1, 0, 0], [0, 1, 1], modulo=kwargs.get('modulo', 0))
