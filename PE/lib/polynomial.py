class PolynomialPrototype:
    """Polynomial Prototype
    
    Polynomial Prototype
    """
    @staticmethod
    def __copy(polynomial_source, polynomial_destination):
        polynomial_destination.coefficient = polynomial_source.coefficient.copy()

    @classmethod
    def identity(cls):
        return cls([1])

    def __init__(self, coefficient):
        self.coefficient = coefficient

    def __getitem__(self, item):
        return self.coefficient[item]

    def __setitem__(self, item, value):
        self.coefficient[item] = value

    def __copy__(self):
        return self.__class__(self.coefficient.copy())

    def __imod__(self, modulo):
        raise NotImplementedError

    def __mod__(self, modulo):
        result = self.__copy__()
        result %= modulo
        return result

    def __iadd__(self, another):
        raise NotImplementedError

    def __add__(self, another):
        result = self.__copy__()
        result += another
        return result

    def __isub__(self, another):
        raise NotImplementedError

    def __sub__(self, another):
        result = self.__copy__()
        result -= another
        return result

    def __mul__(self, another):
        raise NotImplementedError

    def __imul__(self, another):
        raise NotImplementedError

    def __pow__(self, exponent):
        assert(isinstance(exponent, int) and exponent >= 0)
        result = self.__class__.identity()
        if exponent:
            temporary = self
            while exponent:
                if exponent & 1:
                    result = result * temporary
                temporary = temporary * temporary
                exponent >>= 1
        return result

    def __ipow__(self, exponent):
        self.__class__.__copy(self ** exponent, self)
        return self

    def __bool__(self):
        return bool(self.coefficient)

    def __str__(self):
        return self.__class__.__name__ + '(' + str(self.coefficient) + ')'

    def degree(self):
        raise NotImplementedError


class GF2Polynomial(PolynomialPrototype):
    """Polynomial under GF_{2}
    
    Polynomial under GF_{2}, which means each coefficient could only be 0 or 1
    
    Extends:
        PolynomialPrototype
    """
    @staticmethod
    def __copy(polynomial_source, polynomial_destination):
        polynomial_destination.coefficient = polynomial_source.coefficient

    @classmethod
    def identity(cls):
        return cls(1)

    @classmethod
    def gcd(cls, polynomial_0, polynomial_1):
        return cls.gcd(polynomial_1, polynomial_0 % polynomial_1) if polynomial_1 else polynomial_0

    def __init__(self, coefficient):
        assert(isinstance(coefficient, int))
        self.coefficient = coefficient

    def __getitem__(self, item):
        s = bin(self.coefficient)[-1:1:-1]
        return s[item] if item < len(s) else 0

    def __setitem__(self, item, value):
        assert(isinstance(value, int) and value in [0, 1])
        if value:
            self.coefficient |= 1 << item
        else:
            x = 1 << item
            if self.coefficient & x:
                self.coefficient ^= x

    def __copy__(self):
        return self.__class__(self.coefficient)

    def __iadd__(self, another):
        self.coefficient ^= another.coefficient
        return self

    def __imod__(self, another):
        a = self.coefficient
        b = another.coefficient
        self_length = a.bit_length()
        another_length = b.bit_length()
        if self_length < another_length:
            return self
        significant_bit = 1 << self_length - 1
        b <<= self_length - another_length
        for i in range(self_length - another_length + 1):
            if a & significant_bit:
                a ^= b
            significant_bit >>= 1
            b >>= 1
        self.coefficient = a
        return self

    def __mul__(self, another):
        result = GF2Polynomial(0)
        base = self.coefficient
        e = another.coefficient
        while e:
            if e & 1:
                result.coefficient ^= base
            base <<= 1
            e >>= 1
        return result

    def __imul__(self, another):
        self.__class__.__copy(self * another, self)
        return self

    def __ixor__(self, another):
        self.coefficient ^= another.coefficient
        return self

    def __xor__(self, another):
        result = self.__copy__()
        result ^= another
        return result

    def __ilshift__(self, shift):
        self.coefficient <<= shift
        return self

    def __lshift__(self, shift):
        result = self.__copy__()
        result <<= shift
        return result

    def __irshift__(self, shift):
        self.coefficient >>= shift
        return self

    def __rshift__(self, shift):
        result = self.__copy__()
        result >>= shift
        return result

    def __str__(self):
        return self.__class__.__name__ + '(' + bin(self.coefficient)[2:] + ')'

    def degree(self):
        return self.coefficient.bit_length() - 1
