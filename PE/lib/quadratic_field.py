def generate_quadratic_field(d, modulo=0):
    """generate quadratic field number class
    
    generate quadratic field number class
    
    Arguments:
        d {int} -- nonzero square free integer for generating quadratic field
    
    Keyword Arguments:
        modulo {int} -- modulo (default: {0})
    
    Returns:
        class -- quadratic field number class
    """
    assert(isinstance(modulo, int) and modulo >= 0)
    
    class QuadraticFieldNumber:
        """quadratic field number class
        
        use to generate number in the corresponding quadratic field
        """
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __mul__(self, another):
            x = self.x * another.x + d * self.y * another.y
            y = self.x * another.y + self.y * another.x
            return self.__class__(x, y)

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
            return '({}, {} \\sqrt({}))'.format(self.x, self.y, d)

    class QuadraticFieldNumberModulo(QuadraticFieldNumber):
        """quadratic field number class with modulo
        
        use to generate number in the corresponding quadratic field with modulo
        """
        def __init__(self, x, y):
            self.x = x % modulo
            self.y = y % modulo

    return QuadraticFieldNumberModulo if modulo else QuadraticFieldNumber
