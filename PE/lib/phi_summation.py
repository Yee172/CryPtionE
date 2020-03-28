from collections import defaultdict
from phi_sieve import phi_sieve


def phi_summation(n=10 ** 11, return_single_value=True, info=True, **kwargs):
    """Return the summation of phi up to n or the function to get the summation of phi
    
    Sieve of Dujiao without the memory trick in order to be more general
    
    f(n) = \\phi(n), g(n) = 1, h(n) = \\sum_{d | n} f(d) g(n / d) = n
    S(n) = \\sum_{i = 1}^{n} f(i)

       \\sum_{i = 1}^{n} h(i) = \\sum_{i = 1}^{n} \\sum_{d | n} f(d) g(n / d)
                              = \\sum_{i = 1}^{n} \\sum_{d | n} g(d) f(n / d)
                              = \\sum_{d = 1}^{n} g(d) \\sum_{i = 1}^{\\left \\lfloor n / d \\right \\rfloor} f(i)
                              = \\sum_{d = 1}^{n} S(\\left \\lfloor n / d \\right \\rfloor)
                              = S(n) + \\sum_{d = 2}^{n} S(\\left \\lfloor n / d \\right \\rfloor)
    => S(n) = \\sum_{i = 1}^{n} h(i) - \\sum_{d = 2}^{n} S(\\left \\lfloor n / d \\right \\rfloor)
            = n (n + 1) / 2 - \\sum_{d = 2}^{n} S(\\left \\lfloor n / d \\right \\rfloor)

    Arguments:
        **kwargs {[type]} -- [description]
            modulo {int} -- modulo number (default: {0})
    
    Keyword Arguments:
        n {int} -- upper bound (default: {10 ** 11})
        return_single_value {bool} -- only need the corresponding value or the DFS works for input less than or equal to n (default: {True})
        info {bool} -- need info or not (default: {True})
    
    Returns:
        int -- the corresponding value
            or the corresponding DFS 
    """
    modulo = kwargs.get('modulo', 0)

    brute_force_upperbound = int(n ** (2 / 3)) + 1

    if info:
        print('Getting the first two-thirds power of the upper bound phi by sieve of Euler...')

    phi = phi_sieve(brute_force_upperbound, True, False)

    if info:
        print('Phi generated successfully.')

    if info:
        print('Getting the naive prefix summation of phi...')

    pre_sum_phi_1 = [0] * brute_force_upperbound
    if modulo:
        for i in range(1, brute_force_upperbound):
            pre_sum_phi_1[i] = (pre_sum_phi_1[i - 1] + phi[i]) % modulo
    else:
        for i in range(1, brute_force_upperbound):
            pre_sum_phi_1[i] = pre_sum_phi_1[i - 1] + phi[i]

    if info:
        print('Naive prefix summation of phi generated successfully.')

    if info:
        print('Constructing the corresponding DFS...')

    pre_sum_phi_2 = defaultdict(int)

    def dfs(n):
        if n < brute_force_upperbound:
            return pre_sum_phi_1[n]
        else:
            if pre_sum_phi_2[n]:
                return pre_sum_phi_2[n]
        res = 0
        p = 2
        while p <= n:
            q = n // (n // p)
            res += (q - p + 1) * dfs(n // p)
            p = q + 1
        res = n * (n + 1) // 2 - res
        if modulo:
            res %= modulo
        if n >= brute_force_upperbound:
            pre_sum_phi_2[n] = res
        return res

    if info:
        print('The corresponding DFS generated successfully.')

    if return_single_value:
        if info:
            print('The value returned.')
        return dfs(n)
    if info:
        print('The DFS returned.')
        return dfs


def i_phi_summation(n=10 ** 11, return_single_value=True, info=True, **kwargs):
    """Return the summation of i * phi up to n or the function to get the summation of i * phi
    
    Sieve of Dujiao without the memory trick in order to be more general

    f(n) = n \\phi(n), g(n) = n, h(n) = \\sum_{d | n} f(d) g(n / d) = n \\sum_{d | n} \\phi(d) = n^{2}
    S(n) = \\sum_{i = 1}^{n} f(i)

       \\sum_{i = 1}^{n} h(i) = \\sum_{i = 1}^{n} \\sum_{d | n} f(d) g(n / d)
                              = \\sum_{i = 1}^{n} \\sum_{d | n} g(d) f(n / d)
                              = \\sum_{d = 1}^{n} g(d) \\sum_{i = 1}^{\\left \\lfloor n / d \\right \\rfloor} f(i)
                              = \\sum_{d = 1}^{n} d S(\\left \\lfloor n / d \\right \\rfloor)
                              = S(n) + \\sum_{d = 2}^{n} d S(\\left \\lfloor n / d \\right \\rfloor)
    => S(n) = \\sum_{i = 1}^{n} h(i) - \\sum_{d = 2}^{n} d S(\\left \\lfloor n / d \\right \\rfloor)
            = n (n + 1) (2 n + 1) / 6 - \\sum_{d = 2}^{n} d S(\\left \\lfloor n / d \\right \\rfloor)

    Arguments:
        **kwargs {[type]} -- [description]
            modulo {int} -- modulo number (default: {0})
    
    Keyword Arguments:
        n {int} -- upper bound (default: {10 ** 11})
        return_single_value {bool} -- only need the corresponding value or the DFS works for input less than or equal to n (default: {True})
        info {bool} -- need info or not (default: {True})
    
    Returns:
        int -- the corresponding value
            or the corresponding DFS 
    """
    modulo = kwargs.get('modulo', 0)

    brute_force_upperbound = int(n ** (2 / 3)) + 1

    if info:
        print('Getting the first two-thirds power of the upper bound phi by sieve of Euler...')

    phi = phi_sieve(brute_force_upperbound, True, False)

    if info:
        print('Phi generated successfully.')

    if info:
        print('Getting the naive prefix summation of i * phi...')

    pre_sum_i_phi_1 = [0] * brute_force_upperbound
    if modulo:
        for i in range(1, brute_force_upperbound):
            pre_sum_i_phi_1[i] = (pre_sum_i_phi_1[i - 1] + i * phi[i]) % modulo
    else:
        for i in range(1, brute_force_upperbound):
            pre_sum_i_phi_1[i] = pre_sum_i_phi_1[i - 1] + i * phi[i]

    if info:
        print('Naive prefix summation of i * phi generated successfully.')

    if info:
        print('Constructing the corresponding DFS...')

    pre_sum_i_phi_2 = defaultdict(int)

    def g_summation(n):
        return n * (n + 1) // 2

    def dfs(n):
        if n < brute_force_upperbound:
            return pre_sum_i_phi_1[n]
        else:
            if pre_sum_i_phi_2[n]:
                return pre_sum_i_phi_2[n]
        res = 0
        p = 2
        while p <= n:
            q = n // (n // p)
            res += (g_summation(q) - g_summation(p - 1)) * dfs(n // p)
            p = q + 1
        res = n * (n + 1) * (2 * n + 1) // 6 - res
        if modulo:
            res %= modulo
        if n >= brute_force_upperbound:
            pre_sum_i_phi_2[n] = res
        return res

    if info:
        print('The corresponding DFS generated successfully.')

    if return_single_value:
        if info:
            print('The value returned.')
        return dfs(n)
    if info:
        print('The DFS returned.')
        return dfs
