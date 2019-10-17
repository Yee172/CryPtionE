def Cipolla(n, modulo):
    assert(isinstance(modulo, int) and modulo > 0)
    if modulo == 2:
        return 1
    if n % modulo == 0:
        return 0
    Legendre = lambda n: pow(n, modulo - 1 >> 1, modulo)
    if Legendre(n) == modulo - 1:
        return -1
    t = 0
    while Legendre(t ** 2 - n) != modulo - 1:
        t += 1
    w = (t ** 2 - n) % modulo

    class QuadraticFieldNumber:
        def __init__(self, x, y):
            self.x = x % modulo
            self.y = y % modulo

        def __mul__(self, another):
            x = self.x * another.x + w * self.y * another.y
            y = self.x * another.y + self.y * another.x
            return QuadraticFieldNumber(x, y)

        def __pow__(self, exponent):
            result = QuadraticFieldNumber(1, 0)
            if exponent:
                temporary = QuadraticFieldNumber(self.x, self.y)
                while exponent:
                    if exponent & 1:
                        result *= temporary
                    temporary *= temporary
                    exponent >>= 1
            return result
    
    result = QuadraticFieldNumber(t, 1) ** (modulo + 1 >> 1)
    return result.x
