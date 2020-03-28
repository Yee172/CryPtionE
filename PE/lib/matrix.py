__all__ = ['Matrix', 'generate_fixed_matrix_class']


class Matrix:
    """Matrix
    
    Matrix implements
    """
    def __init__(self, row_number, column_number=0, initial_value=0, **kwargs):
        modulo = kwargs.get('modulo', 0)
        precision = kwargs.get('precision', 1e-8)
        if modulo:
            self.__class__ = MatrixModulo
            self.__init__(row_number, column_number, initial_value, modulo)
        else:
            self.__class__ = MatrixDecimal
            self.__init__(row_number, column_number, initial_value, precision)


def generate_fixed_matrix_class(**kwargs):
    modulo = kwargs.get('modulo', 0)
    precision = kwargs.get('precision', 1e-8)
    assert(isinstance(modulo, int) and modulo >= 0)
    if modulo:
        class MatrixFixedModulo(MatrixPrototype):
            """Matrix with fixed modulo
            
            Matrix implements with fixed modulo

            Extends:
                MatrixPrototype
            """
            def __init__(self, row_number, column_number=0, initial_value=0):
                if isinstance(row_number, int):
                    self.row_number = row_number
                    self.column_number = column_number if column_number else self.row_number
                    self.matrix = [[initial_value] * self.column_number for _ in range(self.row_number)]
                else:
                    vector = row_number
                    self.row_number = len(vector)
                    self.column_number = 1
                    self.matrix = list(map(lambda x: [x], vector))
            
            def __iadd__(self, another):
                assert((self.row_number, self.column_number) == (another.row_number, another.column_number))
                for i in range(self.row_number):
                    for j in range(self.column_number):
                        self[i][j] = (self[i][j] + another[i][j]) % modulo
                return self

            def __isub__(self, another):
                assert((self.row_number, self.column_number) == (another.row_number, another.column_number))
                for i in range(self.row_number):
                    for j in range(self.column_number):
                        self[i][j] = (self[i][j] - another[i][j]) % modulo
                return self

            def __mul__(self, another):
                if isinstance(another, int) or isinstance(another, float):
                    result = self.__copy_without_content__()
                    if another:
                        for i in range(self.row_number):
                            for j in range(self.column_number):
                                result[i][j] = self[i][j] * another
                else:
                    assert(self.column_number == another.row_number)
                    result = self.__class__(self.row_number, another.column_number)
                    for i in range(self.row_number):
                        for k in range(self.column_number):
                            if self[i][k]:
                                for j in range(another.column_number):
                                    result[i][j] += self[i][k] * another[k][j]
                result %= modulo
                return result

            def trace(self):
                return super(self.__class__, self).trace() % modulo

        return MatrixFixedModulo
    else:
        class MatrixFixedDecimal(MatrixPrototype):
            """General matrix with fixed precision
            
            General matrix implements with fixed precision

            Extends:
                MatrixPrototype
            """
            def __init__(self, row_number, column_number=0, initial_value=0):
                if isinstance(row_number, int):
                    self.row_number = row_number
                    self.column_number = column_number if column_number else self.row_number
                    self.matrix = [[initial_value] * self.column_number for _ in range(self.row_number)]
                else:
                    vector = row_number
                    self.row_number = len(vector)
                    self.column_number = 1
                    self.matrix = list(map(lambda x: [x], vector))

            def __sign__(self, x):
                return -1 if x < precision else x > precision
            
            def __contains__(self, item):
                for i in range(self.row_number):
                    for each_element in self[i]:
                        if not self.__sign__(each_element - item):
                            return True
                return False

            def __mul__(self, another):
                if isinstance(another, int) or isinstance(another, float):
                    result = self.__copy_without_content__()
                    if self.__sign__(another):
                        for i in range(self.row_number):
                            for j in range(self.column_number):
                                result[i][j] = self[i][j] * another
                else:
                    assert(self.column_number == another.row_number)
                    result = self.__class__(self.row_number, another.column_number)
                    for i in range(self.row_number):
                        for k in range(self.column_number):
                            if self.__sign__(self[i][k]):
                                for j in range(another.column_number):
                                    result[i][j] += self[i][k] * another[k][j]
                return result

        return MatrixFixedDecimal


class MatrixPrototype:
    """Matrix prototype
    
    Matrix implements
    """
    @staticmethod
    def __copy(matrix_source, matrix_destination):
        assert((matrix_source.row_number, matrix_source.column_number) == (matrix_destination.row_number, matrix_destination.column_number))
        for i in range(matrix_source.row_number):
            for j in range(matrix_source.column_number):
                matrix_destination[i][j] = matrix_source[i][j]

    def __init__(self, row_number, column_number=0, initial_value=0):
        if isinstance(row_number, int):
            self.row_number = row_number
            self.column_number = column_number if column_number else self.row_number
            self.matrix = [[initial_value] * self.column_number for _ in range(self.row_number)]
        else:
            vector = row_number
            self.row_number = len(vector)
            self.column_number = 1
            self.matrix = list(map(lambda x: [x], vector))
    
    def __getitem__(self, item):
        return self.matrix[item]

    def __setitem__(self, item, value):
        assert(isinstance(value, list) and len(value) == self.column_number)
        self.matrix[item] = value

    def __str__(self):
        return '\n'.join(map(lambda each_row: ' '.join(map(str, each_row)), self.matrix))

    def __contains__(self, item):
        for i in range(self.row_number):
            if item in self[i]:
                return True
        return False

    def __copy_without_content__(self):
        return self.__class__(self.row_number, self.column_number)

    def __copy__(self):
        copy = self.__copy_without_content__()
        self.__class__.__copy(self, copy)
        return copy

    def __imod__(self, modulo):
        for i in range(self.row_number):
            for j in range(self.column_number):
                self[i][j] %= modulo
        return self

    def __mod__(self, modulo):
        result = self.__copy__()
        result %= modulo
        return result

    def __iadd__(self, another):
        assert((self.row_number, self.column_number) == (another.row_number, another.column_number))
        for i in range(self.row_number):
            for j in range(self.column_number):
                self[i][j] += another[i][j]
        return self

    def __add__(self, another):
        result = self.__copy__()
        result += another
        return result

    def __isub__(self, another):
        assert((self.row_number, self.column_number) == (another.row_number, another.column_number))
        for i in range(self.row_number):
            for j in range(self.column_number):
                self[i][j] -= another[i][j]
        return self

    def __sub__(self, another):
        result = self.__copy__()
        result -= another
        return result

    def __mul__(self, another):
        if isinstance(another, int) or isinstance(another, float):
            result = self.__copy_without_content__()
            for i in range(self.row_number):
                for j in range(self.column_number):
                    result[i][j] = self[i][j] * another
        else:
            assert(self.column_number == another.row_number)
            result = self.__class__(self.row_number, another.column_number)
            for i in range(self.row_number):
                for k in range(self.column_number):
                    for j in range(another.column_number):
                        result[i][j] += self[i][k] * another[k][j]
        return result

    def __imul__(self, another):
        self.__class__.__copy(self * another, self)
        return self

    def __pow__(self, exponent):
        assert(isinstance(exponent, int) and exponent >= 0)
        assert(self.row_number == self.column_number)
        result = self.__copy_without_content__()
        for i in range(self.row_number):
            result[i][i] = 1
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

    def trace(self):
        assert(self.row_number == self.column_number)
        result = sum(self[i][i] for i in range(self.row_number))
        return result


class MatrixDecimal(MatrixPrototype):
    """General matrix
    
    General matrix implements

    Extends:
        MatrixPrototype
    """
    def __init__(self, row_number, column_number=0, initial_value=0, precision=1e-8):
        if isinstance(row_number, int):
            self.row_number = row_number
            self.column_number = column_number if column_number else self.row_number
            self.matrix = [[initial_value] * self.column_number for _ in range(self.row_number)]
        else:
            vector = row_number
            self.row_number = len(vector)
            self.column_number = 1
            self.matrix = list(map(lambda x: [x], vector))
        self.precision = precision

    def __sign__(self, x):
        return -1 if x < -self.precision else x > self.precision
    
    def __contains__(self, item):
        for i in range(self.row_number):
            for each_element in self[i]:
                if not self.__sign__(each_element - item):
                    return True
        return False

    def __copy_without_content__(self):
        return self.__class__(self.row_number, self.column_number, precision=self.precision)

    def __mul__(self, another):
        if isinstance(another, int) or isinstance(another, float):
            result = self.__copy_without_content__()
            if self.__sign__(another):
                for i in range(self.row_number):
                    for j in range(self.column_number):
                        result[i][j] = self[i][j] * another
        else:
            assert(self.column_number == another.row_number)
            result = self.__class__(self.row_number, another.column_number, precision=self.precision)
            for i in range(self.row_number):
                for k in range(self.column_number):
                    if self.__sign__(self[i][k]):
                        for j in range(another.column_number):
                            result[i][j] += self[i][k] * another[k][j]
        return result


class MatrixModulo(MatrixPrototype):
    """Matrix with modulo
    
    Matrix implements with modulo

    Extends:
        MatrixPrototype
    """
    def __init__(self, row_number, column_number=0, initial_value=0, modulo=0):
        if isinstance(row_number, int):
            self.row_number = row_number
            self.column_number = column_number if column_number else self.row_number
            self.matrix = [[initial_value] * self.column_number for _ in range(self.row_number)]
        else:
            vector = row_number
            self.row_number = len(vector)
            self.column_number = 1
            self.matrix = list(map(lambda x: [x], vector))
        self.modulo = modulo
    
    def __copy_without_content__(self):
        return self.__class__(self.row_number, self.column_number, modulo=self.modulo)

    def __iadd__(self, another):
        assert((self.row_number, self.column_number, self.modulo) == (another.row_number, another.column_number, another.modulo))
        for i in range(self.row_number):
            for j in range(self.column_number):
                self[i][j] = (self[i][j] + another[i][j]) % self.modulo
        return self

    def __isub__(self, another):
        assert((self.row_number, self.column_number, self.modulo) == (another.row_number, another.column_number, another.modulo))
        for i in range(self.row_number):
            for j in range(self.column_number):
                self[i][j] = (self[i][j] - another[i][j]) % self.modulo
        return self

    def __mul__(self, another):
        if isinstance(another, int) or isinstance(another, float):
            result = self.__copy_without_content__()
            if another:
                for i in range(self.row_number):
                    for j in range(self.column_number):
                        result[i][j] = self[i][j] * another
        else:
            assert(self.column_number == another.row_number and self.modulo == another.modulo)
            result = self.__class__(self.row_number, another.column_number, modulo=self.modulo)
            for i in range(self.row_number):
                for k in range(self.column_number):
                    if self[i][k]:
                        for j in range(another.column_number):
                            result[i][j] += self[i][k] * another[k][j]
        result %= self.modulo
        return result

    def trace(self):
        return super(self.__class__, self).trace() % self.modulo
