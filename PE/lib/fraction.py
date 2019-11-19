from math import gcd

class Fraction:
    """Fraction
    
    Simple fraction implement for \frac{x}{y}
    """
    @staticmethod
    def __get_simplest_fraction(x, y):
        g = gcd(x, y)
        if g > 1:
            x //= g
            y //= g
        return Fraction(x, y)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, another):
        if isinstance(another, int):
            another = self.__class__(another, 1)
        return self.__class__.__get_simplest_fraction(self.x * another.y + self.y * another.x, self.y * another.y)

    def __sub__(self, another):
        if isinstance(another, int):
            another = self.__class__(another, 1)
        return self.__class__.__get_simplest_fraction(self.x * another.y - self.y * another.x, self.y * another.y)

    def __mul__(self, another):
        if isinstance(another, int):
            another = self.__class__(another, 1)
        return self.__class__.__get_simplest_fraction(self.x * another.x, self.y * another.y)

    def __truediv__(self, another):
        if isinstance(another, int):
            another = self.__class__(another, 1)
        return self.__class__.__get_simplest_fraction(self.x * another.y, self.y * another.x)

    def __floordiv__(self, another):
        if isinstance(another, int):
            another = self.__class__(another, 1)
        x = self.x * another.y
        y = self.y * another.x
        return x // y

    def __eq__(self, another):
        if isinstance(another, int):
            another = self.__class__(another, 1)
        a = self.__class__.__get_simplest_fraction(self.x, self.y)
        b = another.__class__.__get_simplest_fraction(another.x, another.y)
        return a.x == b.x and a.y == b.y

    def __lt__(self, another):
        if isinstance(another, int):
            another = self.__class__(another, 1)
        return self.x * another.y < self.y * another.x

    def __le__(self, another):
        if isinstance(another, int):
            another = self.__class__(another, 1)
        return self.x * another.y <= self.y * another.x

    def __gt__(self, another):
        if isinstance(another, int):
            another = self.__class__(another, 1)
        return self.x * another.y > self.y * another.x

    def __gt__(self, another):
        if isinstance(another, int):
            another = self.__class__(another, 1)
        return self.x * another.y >= self.y * another.x

    def simplify(self):
        g = gcd(self.x, self.y)
        if g > 1:
            self.x //= g
            self.y //= g

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
