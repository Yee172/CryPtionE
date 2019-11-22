def integer_sqrt(n):
    """Integer square root of n
    
    Get the integer square root of n
    
    Arguments:
        n {number} -- n
    
    Returns:
        int -- integer square root of n
    """
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
