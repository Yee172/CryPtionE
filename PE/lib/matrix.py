class Matrix:
    """Matrix
    
    Matrix implements
    
    Variables:
        MODULE {number} -- global module for matrix operations
        PURE_INTEGER {bool} -- indicator of whether the matrix only contains integers
        PRECISION {number} -- if the matrix contains decimals, then we need to set the precision
    """

    MODULE = 0
    PURE_INTEGER = True
    PRECISION = 1e-8

    @staticmethod
    def __sign(x):
        return -1 if x < -Matrix.PRECISION else x > Matrix.PRECISION

    @staticmethod
    def __copy(matrix_source, matrix_destination):
        assert((matrix_source.row_number, matrix_source.column_number) == (matrix_destination.row_number, matrix_destination.column_number))
        for i in range(matrix_source.row_number):
            for j in range(matrix_source.column_number):
                matrix_destination[i][j] = matrix_source[i][j]

    def __init__(self, row_number, column_number=0, initial_value=0):
        self.row_number = row_number
        self.column_number = column_number if column_number else self.row_number
        self.matrix = [[initial_value] * self.column_number for _ in range(self.row_number)]
    
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

    def __copy__(self):
        copy = Matrix(self.row_number, self.column_number)
        Matrix.__copy(self, copy)
        return copy

    def __imod__(self, module):
        for i in range(self.row_number):
            for j in range(self.column_number):
                self[i][j] %= module
        return self

    def __mod__(self, module):
        result = self.__copy__()
        result %= module
        return result

    def __iadd__(self, another):
        assert((self.row_number, self.column_number) == (another.row_number, another.column_number))
        for i in range(self.row_number):
            for j in range(self.column_number):
                self[i][j] += another[i][j]
        if Matrix.MODULE:
            self %= Matrix.MODULE
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
        if Matrix.MODULE:
            self %= Matrix.MODULE
        return self

    def __sub__(self, another):
        result = self.__copy__()
        result -= another
        return result

    def __mul__(self, another):
        assert(self.column_number == another.row_number)
        result = Matrix(self.row_number, another.column_number)
        if Matrix.PURE_INTEGER:
            for i in range(self.row_number):
                for k in range(self.column_number):
                    if self[i][k]:
                        for j in range(another.column_number):
                            result[i][j] += self[i][k] * another[k][j]
        else:
            for i in range(self.row_number):
                for k in range(self.column_number):
                    if Matrix.__sign(self[i][k]):
                        for j in range(another.column_number):
                            result[i][j] += self[i][k] * another[k][j]
        if Matrix.MODULE:
            result %= Matrix.MODULE
        return result

    def __imul__(self, another):
        Matrix.__copy(self * another, self)
        return self

    def __pow__(self, exponent):
        assert(isinstance(exponent, int) and exponent >= 0)
        assert(self.row_number == self.column_number)
        result = Matrix(self.row_number)
        for i in range(self.row_number):
            result[i][i] = 1
        if exponent:
            temporary = result * self
            while exponent:
                if exponent & 1:
                    result *= temporary
                temporary *= temporary
                exponent >>= 1
        return result

    def __ipow__(self, exponent):
        Matrix.__copy(self ** exponent, self)
        return self

    def trace(self):
        assert(self.row_number == self.column_number)
        result = sum(self[i][i] for i in range(self.row_number))
        if Matrix.MODULE:
            result %= Matrix.MODULE
        return result
