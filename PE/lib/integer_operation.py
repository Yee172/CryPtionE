def integer_sqrt(n):
    """Integer square root of n
    
    Get the integer square root of n, i.e.
    1. square_root(n) ** 2 \\leq n
    2. (square_root(n) + 1) ** 2 > n
    
    Arguments:
        n {int} -- n
    
    Returns:
        int -- integer square root of n
    """
    assert(n >= 0)
    if n < 100000000000000:
        result = int(n ** .5)
    elif n < 100000000000000000000000000000000:
        result = int(n ** .5)
        while result ** 2 > n:
            result -= 1
    elif n < 100000000000000000000000000000000000000000000:
        result = int(n ** .5)
        while (result + 1) ** 2 <= n:
            result += 1
        while result ** 2 > n:
            result -= 1
    else:
        result = n
        while result ** 2 > n:
            result = result + n // result >> 1
    return result


def integer_kth_root(n, k):
    """Integer kth root of n
    
    Get the integer kth root of n, i.e.
    1. square_root(n) ** k \\leq n
    2. (square_root(n) + 1) ** k > n
    
    Arguments:
        n {int} -- n
        k {int} -- k
    """
    assert(k > 0 and n >= 0)
    result = n
    k_minus_1 = k - 1
    k_minus_1_power_of_result = result ** k_minus_1
    while k_minus_1_power_of_result * result > n:
        result = (k_minus_1 * result + n // k_minus_1_power_of_result) // k
        k_minus_1_power_of_result = result ** k_minus_1
    return result
