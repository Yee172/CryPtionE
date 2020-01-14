def prime_sieve(upper_bound=10 ** 7, only_prime=True, info=True, **kwargs):
    """Return a list of prime with index up to upper_bound

    if bitarray is installed:
        Sieve of Eratosthenes (Learnt from code of epiclolz) for both sieve
        PS: faster because of the operation of bitarray
    else:
        Sieve of Euler in normal way for prime sieve
        Sieve of Eratosthenes for segment prime sieve

    Arguments:
        **kwargs {[type]} -- [description]
            raw_is_prime {bool} -- when only_prime is False, this argument determines whether
                                   return the raw is_prime list of the faster way (default: {False})
            function_is_prime {bool} -- when only_prime is False, this argument determines whether
                                        return the prime test function that can test up to
                                        upper_bound ** 2 (default: {False})
            with_minimum_factor {bool} -- when only_prime is False, this argument determines whether
                                          return the minimum factor of each number under
                                          upper_bound (default: {False})
            with_minimum_factor_time {bool} -- when only_prime is False, this argument determines whether
                                               return the time of minimum factor of each number under
                                               upper_bound (default: {False})
            with_divisor_number {bool} -- when only_prime is False, this argument determines whether
                                          return the divisor number of each number under
                                          upper_bound (default: {False})
            segment_prime_sieve {bool} -- this argument determines whether use segment prime sieve,
                                          when this argument is True, raw_is_prime and function_is_prime
                                          and with_minimum_factor would be ignored (default: {False})
            lower_bound {int} -- when segment_prime_sieve is True, this argument is used to set the
                                 lower bound of segment prime sieve (default: {1})
            without_prime {bool} -- when only_prime is False, this argument determines whether
                                    not return the sieved prime under upper_bound (default: {False})
    
    Keyword Arguments:
        upper_bound {int} -- upper bound (default: {10 ** 7})
        only_prime {bool} -- whether only return prime or
                             with [is_prime or check_is_prime or minimum_factor or minimum_factor_time or divisor_number] ahead (default: {True})
                             default False situation:
                                 return is_prime and prime
        info {bool} -- need info or not (default: {True})
    
    Returns:
        if only_prime:
            list -- a list of prime with index up to upper_bound
        else:
            tuple -- a subset of [check_is_prime, minimum_factor, minimum_factor_time, divisor_number, is_prime, a list of prime with index up to upper_bound] with order kept
    """
    raw_is_prime = kwargs.get('raw_is_prime', False)
    function_is_prime = kwargs.get('function_is_prime', False)
    with_minimum_factor = kwargs.get('with_minimum_factor', False)
    with_minimum_factor_time = kwargs.get('with_minimum_factor_time', False)
    with_divisor_number = kwargs.get('with_divisor_number', False)
    segment_prime_sieve = kwargs.get('segment_prime_sieve', False)
    without_prime = kwargs.get('without_prime', False)

    if only_prime and without_prime:
        if info:
            print('Nothing to do!')

        return ()

    if segment_prime_sieve:
        if raw_is_prime:
            print('Warning: raw_is_prime would be ignored when using segment prime sieve')
        if function_is_prime:
            print('Warning: function_is_prime would be ignored when using segment prime sieve')
        if with_minimum_factor:
            print('Warning: with_minimum_factor would be ignored when using segment prime sieve')
        if with_minimum_factor_time:
            print('Warning: with_minimum_factor_time would be ignored when using segment prime sieve')
        if with_divisor_number:
            print('Warning: with_divisor_number would be ignored when using segment prime sieve')

        lower_bound = kwargs.get('lower_bound', 1)
        if not isinstance(lower_bound, int) or lower_bound < 1:
            raise Exception('Invalid lower bound for segment prime sieve')

        if info:
            print('Sieving prime numbers at range [{}, {})'.format(lower_bound, upper_bound))

        _prime = prime_sieve(int(upper_bound ** .5), only_prime=True, info=info)

        forced_odd = lambda x: x | 1
        _lower_bound = forced_odd(lower_bound)
        length = upper_bound - _lower_bound >> 1

        try:
            if info:
                print('Trying using bitarray to accelerate the speed')

            from bitarray import bitarray
            is_prime = bitarray(length)
            is_prime.setall(1)
            for p in _prime[1:]:
                is_prime[forced_odd((_lower_bound + p - 1) // p) * p - _lower_bound >> 1::p] = 0
            prime = [i * 2 + _lower_bound for i in is_prime.search(bitarray([1]))]
            
        except:
            if info:
                print('Something was wrong with bitarray, using the segment prime sieve in normal way')

            is_prime = [True] * length
            for p in _prime[1:]:
                for k in range(forced_odd((_lower_bound + p - 1) // p) * p - _lower_bound >> 1, length, p):
                    is_prime[k] = False
            prime = [i * 2 + _lower_bound for i in range(length) if is_prime[i]]

        if _lower_bound < 3:
            prime = [2] + prime

        if info:
            print('Prime number at range [{}, {}) generated successfully'.format(lower_bound, upper_bound))

        return prime

    else:
        FLAG_BITARRAY = False

        if info:
            print('Sieving prime numbers below {}'.format(upper_bound))

        if with_minimum_factor or with_minimum_factor_time or with_divisor_number:
            if info:
                print('Using the sieve of Euler in normal way')

            prime = []
            is_prime = [True] * upper_bound
            is_prime[0] = False
            is_prime[1] = False
            if with_minimum_factor:
                minimum_factor = [1] * upper_bound
                minimum_factor[0] = 0

                def minimum_factor_part_0(i):
                    minimum_factor[i] = i

                def minimum_factor_part_1(y, x):
                    minimum_factor[y] = x

            else:

                def minimum_factor_part_0(*args, **kwargs):
                    pass

                def minimum_factor_part_1(*args, **kwargs):
                    pass

            if with_minimum_factor_time or with_divisor_number:
                minimum_factor_time = [1] * upper_bound
                minimum_factor_time[0] = 0
                minimum_factor_time[1] = 0

                def minimum_factor_time_part_0(y, i):
                    minimum_factor_time[y] += minimum_factor_time[i]

            else:

                def minimum_factor_time_part_0(*args, **kwargs):
                    pass

            if with_divisor_number:
                divisor_number = [2] * upper_bound
                divisor_number[0] = 0

                def divisor_number_part_0(y, i):
                    divisor_number[y] = divisor_number[i] * 2

                def divisor_number_part_1(y, i):
                    divisor_number[y] = divisor_number[i] // (minimum_factor_time[i] + 1) * (minimum_factor_time[i] + 2)

            else:

                def divisor_number_part_0(*args, **kwargs):
                    pass

                def divisor_number_part_1(*args, **kwargs):
                    pass

            for i in range(2, upper_bound):
                if is_prime[i]:
                    prime.append(i)
                    minimum_factor_part_0(i)
                for x in prime:
                    y = i * x
                    if y >= upper_bound:
                        break
                    is_prime[y] = False
                    minimum_factor_part_1(y, x)
                    divisor_number_part_0(y, i)
                    if not i % x:
                        minimum_factor_time_part_0(y, i)
                        divisor_number_part_1(y, i)
                        break

        else:
            try:
                if info:
                    print('Trying using bitarray to accelerate the speed')

                from bitarray import bitarray
                is_prime = bitarray(upper_bound >> 1)
                is_prime.setall(1)
                is_prime[0] = 0
                for i in range(1, int(upper_bound ** .5)):
                    if is_prime[i]:
                        is_prime[2 * i ** 2 + 2 * i::2 * i + 1] = 0
                prime = [2] + [i * 2 + 1 for i in is_prime.search(bitarray([1]))]

                if not only_prime:
                    if function_is_prime:
                        def naive_is_prime(n):
                            return bool(n & 1 and is_prime[n >> 1]) or n == 2

                    elif not raw_is_prime:
                        is_prime = [bool(i & 1 and is_prime[i >> 1]) for i in range(upper_bound)]
                        is_prime[2] = True

                FLAG_BITARRAY = True

            except:
                if info:
                    print('Something was wrong with bitarray, using the sieve of Euler in normal way')

                prime = []
                is_prime = [True] * upper_bound
                is_prime[0] = False
                is_prime[1] = False
                for i in range(2, upper_bound):
                    if is_prime[i]:
                        prime.append(i)
                    for x in prime:
                        if i * x >= upper_bound:
                            break
                        is_prime[i * x] = False
                        if not i % x:
                            break

        if not FLAG_BITARRAY:
            if not only_prime and function_is_prime:
                def naive_is_prime(n):
                    return is_prime[n]
        
        if info:
            print('Prime number below {} generated successfully'.format(upper_bound))

        if only_prime:
            return prime

        return_list = []
        if function_is_prime:
            def check_is_prime(n):
                if n < upper_bound:
                    return naive_is_prime(n)
                for p in prime:
                    if p * p > n:
                        break
                    if not n % p:
                        return False
                return True
            return_list.append(check_is_prime)
        if with_minimum_factor:
            return_list.append(minimum_factor)
        if with_minimum_factor_time:
            return_list.append(minimum_factor_time)
        if with_divisor_number:
            return_list.append(divisor_number)
        if not (function_is_prime or with_minimum_factor or with_minimum_factor_time or with_divisor_number):
            return_list.append(is_prime)
        if not without_prime:
            return_list.append(prime)
        return tuple(return_list) if len(return_list) > 1 else return_list[0]
