def get_integer_power_summation_function(k, modulo=0):
    """Get the integer power summation function
    
    Get the integer power summation function of i^{k} from 1
    
    Arguments:
        k {int} -- the order of power

    Keyword Arguments:
        modulo {int} -- modulo (default: {0})
    
    Returns:
        function -- the integer power summation function of i^{k} from 1
    """
    if k == 0:
        return lambda n: n
    if k == 1:
        return lambda n: n * (n + 1) // 2
    if k == 2:
        return lambda n: n * (n + 1) * (2 * n + 1) // 6
    if k == 3:
        return lambda n: (n * (n + 1) // 2) ** 2

    first_n_integer_power_number = [i ** k for i in range(k + 1)]
    delta_table = [first_n_integer_power_number[0]]
    for i in range(k):
        first_n_integer_power_number = [first_n_integer_power_number[j + 1] - first_n_integer_power_number[j] for j in range(k - i)]
        delta_table.append(first_n_integer_power_number[0])

    if modulo:
        for i in range(k + 1):
            delta_table[i] %= modulo

    def binomial(n, k):
        result = 1
        for i in range(k):
            result *= n - i
            result //= i + 1
        return result

    def integer_power_summation(n):
        result = 0
        for i in range(k + 1):
            result += delta_table[i] * binomial(n + 1, i + 1)
        return result

    return (lambda n: integer_power_summation(n) % modulo) if modulo else integer_power_summation


def sigma_summation(k, n, **kwargs):
    """Return the summation of the sigma_{k} function
    
    \\sum_{i = 1}^{n} \\sigma_{k}(i)
    = \\sum_{d = 1}^{n} d^{k} \\sum_{j = 1}^{\\left \\lfloor \\frac{n}{d} \\right \\rfloor} f(d * j)
    , where f(x) = 1
    
    Arguments:
        k {int} -- the order of power
        n {int} -- summation upper bound (inclusive)
        **kwargs {[type]} -- [description]
            modulo {int} -- modulo (default: {0})
    
    Returns:
        int -- the summation of the sigma_{k} function up to n
    """
    modulo = kwargs.get('modulo', 0)
    integer_power_summation_0 = get_integer_power_summation_function(0)
    integer_power_summation_k = get_integer_power_summation_function(k, modulo)

    p = int(n ** .5)
    while p ** 2 <= n:
        p += 1

    result = 0
    for i in range(1, p):
        result += integer_power_summation_0(n // i) * i ** k
    for i in range(1, n // p + 1):
        result += (integer_power_summation_k(n // i) - integer_power_summation_k(n // (i + 1))) * i
    return result % modulo if modulo else result


def sigma_summation_summation(k, n, **kwargs):
    """Return the summation of the summation of the sigma_{k} function
    
      \\sum_{i = 1}^{n} \\sum_{j = 1}^{i} \\sigma_{k}(j)
    = \\sum_{d = 1}^{n} d^{k} \\sum_{j = 1}^{\\left \\lfloor \\frac{n}{d} \\right \\rfloor} f(d * j)
    , where f(x) = (n + 1 - x)
    
    Arguments:
        k {int} -- the order of power
        n {int} -- summation upper bound (inclusive)
        **kwargs {[type]} -- [description]
            modulo {int} -- modulo (default: {0})
    
    Returns:
        int -- the summation of the summation of the sigma_{k} function up to n
    """
    modulo = kwargs.get('modulo', 0)
    integer_power_summation_0 = get_integer_power_summation_function(0)
    integer_power_summation_1 = get_integer_power_summation_function(1)
    integer_power_summation_k = get_integer_power_summation_function(k, modulo)
    integer_power_summation_k_plus_1 = get_integer_power_summation_function(k + 1, modulo)

    p = int(n ** .5)
    while p ** 2 <= n:
        p += 1

    result_positive_part = 0
    result_negative_part = 0
    for i in range(1, p):
        result_positive_part += integer_power_summation_0(n // i) * i ** k
        result_negative_part += integer_power_summation_1(n // i) * i ** (k + 1)
    for i in range(1, n // p + 1):
        result_positive_part += (integer_power_summation_k(n // i) - integer_power_summation_k(n // (i + 1))) * integer_power_summation_0(i)
        result_negative_part += (integer_power_summation_k_plus_1(n // i) - integer_power_summation_k_plus_1(n // (i + 1))) * integer_power_summation_1(i)
    result_positive_part *= n + 1
    result = result_positive_part - result_negative_part
    return result % modulo if modulo else result


def sigma_summation_summation_summation(k, n, **kwargs):
    """Return the summation of the summation of the summation of the sigma_{k} function
    
      \\sum_{i = 1}^{n} \\sum_{j = 1}^{i} \\sum_{l = 1}^{j} \\sigma_{k}(l)
    = \\sum_{d = 1}^{n} d^{k} \\sum_{j = 1}^{\\left \\lfloor \\frac{n}{d} \\right \\rfloor} f(d * j)
    , where f(x) = \\frac{(n + 2 - x) * (n + 1 - x)}{2}
    
    Arguments:
        k {int} -- the order of power
        n {int} -- summation upper bound (inclusive)
        **kwargs {[type]} -- [description]
            modulo {int} -- modulo (default: {0})
    
    Returns:
        int -- the summation of the summation of the summation of the sigma_{k} function up to n
    """
    original_modulo = kwargs.get('modulo', 0)
    modulo = original_modulo * 2
    integer_power_summation_0 = get_integer_power_summation_function(0)
    integer_power_summation_1 = get_integer_power_summation_function(1)
    integer_power_summation_2 = get_integer_power_summation_function(2)
    integer_power_summation_k = get_integer_power_summation_function(k, modulo)
    integer_power_summation_k_plus_1 = get_integer_power_summation_function(k + 1, modulo)
    integer_power_summation_k_plus_2 = get_integer_power_summation_function(k + 2, modulo)

    p = int(n ** .5)
    while p ** 2 <= n:
        p += 1

    result_part_1 = 0
    result_part_2 = 0
    result_part_3 = 0
    for i in range(1, p):
        result_part_1 += integer_power_summation_0(n // i) * i ** k
        result_part_2 += integer_power_summation_1(n // i) * i ** (k + 1)
        result_part_3 += integer_power_summation_2(n // i) * i ** (k + 2)
    for i in range(1, n // p + 1):
        result_part_1 += (integer_power_summation_k(n // i) - integer_power_summation_k(n // (i + 1))) * integer_power_summation_0(i)
        result_part_2 += (integer_power_summation_k_plus_1(n // i) - integer_power_summation_k_plus_1(n // (i + 1))) * integer_power_summation_1(i)
        result_part_3 += (integer_power_summation_k_plus_2(n // i) - integer_power_summation_k_plus_2(n // (i + 1))) * integer_power_summation_2(i)
    result_part_1 *= (n + 1) * (n + 2) // 2
    result_part_3 -= result_part_2
    result_part_2 *= n + 1
    result_part_3 //= 2
    result = result_part_1 - result_part_2 + result_part_3
    return result % original_modulo if original_modulo else result


def sigma_summation_summation_summation_summation(k, n, **kwargs):
    """Return the summation of the summation of the summation of the summation of the sigma_{k} function
    
      \\sum_{i = 1}^{n} \\sum_{j = 1}^{i} \\sum_{l = 1}^{j} \\sum_{m = 1}^{l} \\sigma_{k}(m)
    = \\sum_{d = 1}^{n} d^{k} \\sum_{j = 1}^{\\left \\lfloor \\frac{n}{d} \\right \\rfloor} f(d * j)
    , where f(x) = \\frac{(n + 1 - x) * (n + 2 - x) * (2 * n + 3 - 2 * x)}{12} + \\frac{(n + 2 - x) * (n + 1 - x)}{4}
    
    Arguments:
        k {int} -- the order of power
        n {int} -- summation upper bound (inclusive)
        **kwargs {[type]} -- [description]
            modulo {int} -- modulo (default: {0})
    
    Returns:
        int -- the summation of the summation of the summation of the summation of the sigma_{k} function up to n
    """
    original_modulo = kwargs.get('modulo', 0)
    modulo = original_modulo * 6
    integer_power_summation_0 = get_integer_power_summation_function(0)
    integer_power_summation_1 = get_integer_power_summation_function(1)
    integer_power_summation_2 = get_integer_power_summation_function(2)
    integer_power_summation_3 = get_integer_power_summation_function(3)
    integer_power_summation_k = get_integer_power_summation_function(k, modulo)
    integer_power_summation_k_plus_1 = get_integer_power_summation_function(k + 1, modulo)
    integer_power_summation_k_plus_2 = get_integer_power_summation_function(k + 2, modulo)
    integer_power_summation_k_plus_3 = get_integer_power_summation_function(k + 3, modulo)

    p = int(n ** .5)
    while p ** 2 <= n:
        p += 1

    result_part_1 = 0
    result_part_2 = 0
    result_part_3 = 0
    result_part_4 = 0
    for i in range(1, p):
        result_part_1 += integer_power_summation_0(n // i) * i ** k
        result_part_2 += integer_power_summation_1(n // i) * i ** (k + 1)
        result_part_3 += integer_power_summation_2(n // i) * i ** (k + 2)
        result_part_4 += integer_power_summation_3(n // i) * i ** (k + 3)
    for i in range(1, n // p + 1):
        result_part_1 += (integer_power_summation_k(n // i) - integer_power_summation_k(n // (i + 1))) * integer_power_summation_0(i)
        result_part_2 += (integer_power_summation_k_plus_1(n // i) - integer_power_summation_k_plus_1(n // (i + 1))) * integer_power_summation_1(i)
        result_part_3 += (integer_power_summation_k_plus_2(n // i) - integer_power_summation_k_plus_2(n // (i + 1))) * integer_power_summation_2(i)
        result_part_4 += (integer_power_summation_k_plus_3(n // i) - integer_power_summation_k_plus_3(n // (i + 1))) * integer_power_summation_3(i)
    result_part_1 *= n ** 3 + 11 * n + 6 * n ** 2 + 6
    result_part_4 = 11 * result_part_2 + result_part_4
    result_part_2 *= (n ** 2 + 4 * n) * 3
    result_part_3 *= (n + 2) * 3
    result = result_part_1 - result_part_2 + result_part_3 - result_part_4
    result //= 6
    return result % original_modulo if original_modulo else result
