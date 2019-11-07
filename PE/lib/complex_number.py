class ComplexNumber:
    """complex number
    
    common complex number implement
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, another):
        return self.__class__(self.x + another.x, self.y + another.y)

    def __sub__(self, another):
        return self.__class__(self.x - another.x, self.y - another.y)

    def __mul__(self, another):
        return self.__class__(self.x * another.x - self.y * another.y, self.x * another.y + self.y * another.x)

    def __mod__(self, modulo):
        return self.__class__(x % modulo, y % modulo)

    def __pow__(self, exponent):
        result = self.__class__(1, 0)
        if exponent:
            temporary = self.__class__(self.x, self.y)
            while exponent:
                if exponent & 1:
                    result *= temporary
                temporary *= temporary
                exponent >>= 1
        return result

    def __str__(self):
        return '({}, {} i)'.format(self.x, self.y)
