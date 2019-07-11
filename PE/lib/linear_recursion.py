from extended_gcd import inverse

class LinearRecursion:
    '''linear recursion
    
    Berlekamp Massey Algorithm implement
    
    Variables:
        EPS {number} -- epsilon
    '''
    EPS = 1e-8

    def __init__(self, initial_values, **kwargs):
        self.initial_values = initial_values
        self.recursion = []
        self.modulo = kwargs.get('modulo', 0)

    def __getitem__(self, item):
        return self.__get_value_by_index(item)

    def get_recursion(self):
        if self.modulo:
            return self.__get_recursion_modulo()
        else:
            return self.__get_recursion_normal()

    def __get_recursion_normal(self):
        last_fail_state = []
        for i in range(len(self.initial_values)):
            expectation_delta = -self.initial_values[i]
            for j, r in enumerate(self.recursion):
                expectation_delta += self.initial_values[i - j - 1] * r
            if -LinearRecursion.EPS < expectation_delta < LinearRecursion.EPS:
                continue
            if not len(self.recursion):
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

    def __get_recursion_modulo(self):
        last_fail_state = []
        for i in range(len(self.initial_values)):
            expectation_delta = -self.initial_values[i] % self.modulo
            for j, r in enumerate(self.recursion):
                expectation_delta += self.initial_values[i - j - 1] * r
                expectation_delta %= self.modulo
            if not expectation_delta:
                continue
            if not len(self.recursion):
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
                change[j] += r
                change[j] %= self.modulo
            if i - fail + len(last_fail_state) >= len(self.recursion):
                last_fail_state = self.recursion
                fail = i
                delta = expectation_delta
            self.recursion = change
        return self.recursion

    def __polymul(self, poly1, poly2):
        if self.modulo:
            return self.__polymul_modulo(poly1, poly2)
        else:
            return self.__polymul_normal(poly1, poly2)

    def __polymul_normal(self, poly1, poly2):
        r = [0] * (len(poly1) + len(poly2) - 1)
        for i, x in enumerate(poly1):
            if x > LinearRecursion.EPS or x < -LinearRecursion.EPS:
                for j, y in enumerate(poly2):
                    r[i + j] += x * y
        for i in range(len(poly1) + len(poly2) - 2, len(poly1) - 1, -1):
            if r[i] > LinearRecursion.EPS or r[i] < -LinearRecursion.EPS:
                for j in range(len(poly1) - 1, -1, -1):
                    r[i - j - 1] += r[i] * self.recursion[j]
        return r[:len(poly1)]

    def __polymul_modulo(self, poly1, poly2):
        r = [0] * (len(poly1) + len(poly2) - 1)
        for i, x in enumerate(poly1):
            if x:
                for j, y in enumerate(poly2):
                    r[i + j] += x * y
                    r[i + j] %= self.modulo
        for i in range(len(poly1) + len(poly2) - 2, len(poly1) - 1, -1):
            if r[i]:
                for j in range(len(poly1) - 1, -1, -1):
                    r[i - j - 1] += r[i] * self.recursion[j]
                    r[i - j - 1] %= self.modulo
        return r[:len(poly1)]

    def __get_value_by_index(self, index):
        if not len(self.recursion):
            self.get_recursion()
        length = len(self.recursion)
        r, t = [0] * length, [0] * length
        r[0] = 1
        if length == 1:
            t[0] = self.recursion[0]
        else:
            t[1] = 1
        while index:
            if index & 1:
                r = self.__polymul(r, t)
            t = self.__polymul(t, t)
            index >>= 1
        result = sum(map(lambda i: r[i] * self.initial_values[i], range(len(self.recursion))))
        if self.modulo:
            result %= self.modulo
        return result
