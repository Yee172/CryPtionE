from extended_gcd import inverse
from slice_lib import rearrange_slice_for_infinite_sequence


__all__ = ['LinearRecursion']


class LinearRecursion:
    """Linear recursion
    
    Berlekamp Massey Algorithm implement
    """
    def __init__(self, initial_values, recursion=[], **kwargs):
        modulo = kwargs.get('modulo', 0)
        EPS = kwargs.get('EPS', 1e-8)
        if modulo:
            self.__class__ = LinearRecursionModulo
            self.__init__(initial_values, recursion, modulo)
        else:
            self.__class__ = LinearRecursionDecimal
            self.__init__(initial_values, recursion, EPS)

class LinearRecursionPrototype:
    """Linear recursion prototype
    
    Berlekamp Massey Algorithm implement
    """
    def __init__(self, initial_values, recursion):
        self.initial_values = initial_values
        self.recursion = recursion

    def get_recursion(self):
        raise NotImplementedError

    def prefix_summation(self):
        raise NotImplementedError

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__get_value_by_index(item)
        elif isinstance(item, slice):
            return self.__get_value_by_range(item)
        else:
            raise TypeError('list indices must be integers or slices, not {}'.format(item.__class__.__name__))

    def _polymul(self, poly1, poly2):
        raise NotImplementedError

    def _polypow(self, poly, exponent):
        assert(isinstance(exponent, int) and exponent >= 0)
        result = [0] * len(poly)
        result[0] = 1
        while exponent:
            if exponent & 1:
                result = self._polymul(result, poly)
            poly = self._polymul(poly, poly)
            exponent >>= 1
        return result

    def _get_poly_by_index(self, index):
        if not self.recursion:
            self.get_recursion()
        length = len(self.recursion)
        t = [0] * length
        if length == 1:
            t[0] = self.recursion[0]
        else:
            t[1] = 1
        return self._polypow(t, index)

    def _get_value_by_poly(self, poly):
        return sum(map(lambda i: poly[i] * self.initial_values[i], range(len(poly))))

    def __get_value_by_index(self, index):
        return self._get_value_by_poly(self._get_poly_by_index(index))

    def __get_value_by_range(self, slice_item):
        reverse_flag, minimum, maximum, step = rearrange_slice_for_infinite_sequence(slice_item)
        if minimum >= maximum:
            return []
        result = [0] * ((maximum - minimum - 1) // step + 1)
        s = self._get_poly_by_index(step)
        r = self._get_poly_by_index(minimum)
        if reverse_flag:
            result[-1] = self._get_value_by_poly(r)
            for j in range(len(result) - 2, -1, -1):
                r = self._polymul(r, s)
                result[j] = self._get_value_by_poly(r)
        else:
            result[0] = self._get_value_by_poly(r)
            for j in range(1, len(result)):
                r = self._polymul(r, s)
                result[j] = self._get_value_by_poly(r)
        return result

class LinearRecursionDecimal(LinearRecursionPrototype):
    """General linear recursion
    
    Berlekamp Massey Algorithm implement
    
    Extends:
        LinearRecursionPrototype
    """
    def __init__(self, initial_values, recursion, EPS):
        self.initial_values = initial_values
        self.recursion = recursion
        self.EPS = EPS

    def get_recursion(self):
        last_fail_state = []
        for i in range(len(self.initial_values)):
            expectation_delta = -self.initial_values[i]
            for j, r in enumerate(self.recursion):
                expectation_delta += self.initial_values[i - j - 1] * r
            if -self.EPS < expectation_delta < self.EPS:
                continue
            if not self.recursion:
                self.recursion = [0] * (i + 1)
                fail = i
                delta = expectation_delta
                continue
            multiple = -expectation_delta / delta
            change = [0] * (i - fail - 1) + [-multiple]
            for r in last_fail_state:
                addition = r * multiple
                change.append(addition)
            if len(change) < len(self.recursion):
                change += [0] * (len(self.recursion) - len(change))
            for j, r in enumerate(self.recursion):
                change[j] += r
            if i - fail + len(last_fail_state) >= len(self.recursion):
                last_fail_state = self.recursion
                fail = i
                delta = expectation_delta
            self.recursion = change
        return self.recursion

    def prefix_summation(self):
        if not self.recursion:
            self.get_recursion()
        initial_values = self.initial_values[:len(self.recursion)] + [self[len(self.recursion)]]
        recursion = [0] * (len(self.recursion) + 1)
        recursion[0] = 1
        for i in range(len(self.recursion)):
            initial_values[i + 1] += initial_values[i]
            recursion[i] += self.recursion[i]
            recursion[i + 1] -= self.recursion[i]
        return self.__class__(initial_values, recursion)

    def round_recursion(self, round_to_digit=0):
        if round_to_digit:
            self.recursion = list(map(lambda x: round(x, round_to_digit), self.recursion))
        else:
            self.recursion = list(map(round, self.recursion))

    def _polymul(self, poly1, poly2):
        r = [0] * (len(poly1) + len(poly2) - 1)
        for i, x in enumerate(poly1):
            if x > self.EPS or x < -self.EPS:
                for j, y in enumerate(poly2):
                    r[i + j] += x * y
        for i in range(len(poly1) + len(poly2) - 2, len(poly1) - 1, -1):
            if r[i] > self.EPS or r[i] < -self.EPS:
                for j in range(len(poly1) - 1, -1, -1):
                    r[i - j - 1] += r[i] * self.recursion[j]
        return r[:len(poly1)]


class LinearRecursionModulo(LinearRecursionPrototype):
    """Linear recursion with modulo
    
    Berlekamp Massey Algorithm implement
    
    Extends:
        LinearRecursionPrototype
    """
    def __init__(self, initial_values, recursion, modulo):
        super(LinearRecursionModulo, self).__init__(initial_values, recursion)
        self.modulo = modulo

    def get_recursion(self):
        last_fail_state = []
        for i in range(len(self.initial_values)):
            expectation_delta = -self.initial_values[i] % self.modulo
            for j, r in enumerate(self.recursion):
                expectation_delta = (expectation_delta + self.initial_values[i - j - 1] * r) % self.modulo
            if not expectation_delta:
                continue
            if not self.recursion:
                self.recursion = [0] * (i + 1)
                fail = i
                delta = expectation_delta
                continue
            multiple = -expectation_delta * inverse(delta, self.modulo) % self.modulo
            change = [0] * (i - fail - 1) + [-multiple]
            for r in last_fail_state:
                addition = r * multiple % self.modulo
                change.append(addition)
            if len(change) < len(self.recursion):
                change += [0] * (len(self.recursion) - len(change))
            for j, r in enumerate(self.recursion):
                change[j] = (change[j] + r) % self.modulo
            if i - fail + len(last_fail_state) >= len(self.recursion):
                last_fail_state = self.recursion
                fail = i
                delta = expectation_delta
            self.recursion = change
        return self.recursion

    def prefix_summation(self):
        if not self.recursion:
            self.get_recursion()
        initial_values = self.initial_values[:len(self.recursion)] + [self[len(self.recursion)]]
        recursion = [0] * (len(self.recursion) + 1)
        recursion[0] = 1
        for i in range(len(self.recursion)):
            initial_values[i + 1] = (initial_values[i + 1] + initial_values[i]) % self.modulo
            recursion[i] = (recursion[i] + self.recursion[i]) % self.modulo
            recursion[i + 1] = self.modulo - self.recursion[i]
        return self.__class__(initial_values, recursion, self.modulo)

    def _polymul(self, poly1, poly2):
        r = [0] * (len(poly1) + len(poly2) - 1)
        for i, x in enumerate(poly1):
            if x:
                for j, y in enumerate(poly2):
                    r[i + j] = (r[i + j] + x * y) % self.modulo
        for i in range(len(poly1) + len(poly2) - 2, len(poly1) - 1, -1):
            if r[i]:
                for j in range(len(poly1) - 1, -1, -1):
                    r[i - j - 1] = (r[i - j - 1] + r[i] * self.recursion[j]) % self.modulo
        return r[:len(poly1)]

    def _get_value_by_poly(self, poly):
        return super(LinearRecursionModulo, self)._get_value_by_poly(poly) % self.modulo
