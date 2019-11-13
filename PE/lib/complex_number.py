from math import acos


__all__ = ['ComplexNumber']


class ComplexNumber(complex):
    """complex number
    
    common complex number implement
    """
    @staticmethod
    def _get_real_part(complex_number):
        return complex_number.real

    @staticmethod
    def _get_imaginary_part(complex_number):
        return complex_number.imag

    @staticmethod
    def _get_norm_square(complex_number):
        return complex_number.__get_real_part() ** 2 + complex_number.__get_imaginary_part() ** 2

    @staticmethod
    def _get_norm(complex_number):
        return ComplexNumber.__abs__(complex_number)

    def __get_real_part(self):
        return self.real

    def __get_imaginary_part(self):
        return self.imag

    def __add__(self, another):
        return self.__class__(super(ComplexNumber, self).__add__(another))

    def __radd__(self, another):
        return self.__class__(super(ComplexNumber, self).__radd__(another))

    def __sub__(self, another):
        return self.__class__(super(ComplexNumber, self).__sub__(another))

    def __rsub__(self, another):
        return self.__class__(super(ComplexNumber, self).__rsub__(another))

    def __mul__(self, another):
        return self.__class__(super(ComplexNumber, self).__mul__(another))

    def __rmul__(self, another):
        return self.__class__(super(ComplexNumber, self).__rmul__(another))

    def __truediv__(self, another):
        return self.__class__(super(ComplexNumber, self).__truediv__(another))

    def __rtruediv__(self, another):
        return self.__class__(super(ComplexNumber, self).__rtruediv__(another))

    def __pow__(self, exponent, modulo=None):
        return self.__class__(super(ComplexNumber, self).__pow__(exponent, modulo))

    def __rpow__(self, base, modulo=None):
        return self.__class__(super(ComplexNumber, self).__rpow__(base, modulo))

    def __neg__(self):
        return self.__class__(super(ComplexNumber, self).__neg__())

    def __pos__(self):
        return self.__class__(super(ComplexNumber, self).__pos__())

    def __getattr__(self, attribute):
        if attribute in ['x', 're']:
            return self.__class__._get_real_part(self)
        if attribute in ['y', 'im', 'image']:
            return self.__class__._get_imaginary_part(self)
        if attribute in ['r', 'modulus']:
            return self.norm()
        if attribute == 'theta':
            norm = self.norm()
            return -acos(self.__get_real_part() / norm) if self.y < 0 else acos(self.__get_real_part() / norm)

    def norm_square(self):
        return self.__class__._get_norm_square(self)

    def norm(self):
        return self.__class__._get_norm(self)
