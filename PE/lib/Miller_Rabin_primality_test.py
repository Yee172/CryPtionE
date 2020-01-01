import random


def Miller_Rabin_primality_test(n, **kwargs):
    """Miller Rabin primality test
    
    Miller Rabin primality test implement based on
    1. n = d * 2^{p} + 1
    2. if p is prime, then a^{p - 1} \equiv 1 (mod p)
    3. if p is prime, then x \equiv 1 or x \equiv p - 1 are the only solutions to the equation x^{2} \equiv 1 (mod p)

    When n < 10^{16}, the test is absolutely accurate;
    otherwise, the accurate probability is about 1 - \frac{1}{4}^{iteration_time}
    
    Arguments:
        n {int} -- the test number
        **kwargs {[type]} -- [description]
            iteration_time {int} -- iteration time (default: {20})
            using_fixed_test {bool} -- whether using fixed tests (default: {False})
    
    Returns:
        bool -- whether the test number is prime
    """
    iteration_time = kwargs.get('iteration_time', 20)
    using_fixed_test = kwargs.get('using_fixed_test', False)
    assert(isinstance(iteration_time, int) and iteration_time > 0)

    if n in [2, 3]:
        return True
    if n < 2 or not n & 1 or not n % 3:
        return False
    d = n - 1
    p = 0
    while not d & 1:
        d >>= 1
        p += 1

    def test(a):
        t = pow(a, d, n)
        for i in range(p):
            flag = t != 1 and t != n - 1
            t = t ** 2 % n
            if t == 1 and flag:
                return False
        return t == 1

    if n < 10 ** 16 or using_fixed_test:
        test_list = [2, 3, 7, 61, 24251]
        if n in test_list[2:]:
            return True
        if n == 46856248255981:
            return False
        return all(test(a) for a in test_list)
    else:
        return all(test(random.randint(1, n - 1)) for i in range(iteration_time))
