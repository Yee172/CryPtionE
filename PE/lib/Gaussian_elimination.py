from extended_gcd import inverse


class GaussianElimination:
    """Gaussian elimination
    
    Guassian elimination process
    """
    def __init__(self, matrix, **kwargs):
        modulo = kwargs.get('modulo', 0)
        EPS = kwargs.get('EPS', 1e-8)
        dimension = len(matrix)
        augment_dimension = len(matrix[0]) - dimension
        assert(augment_dimension > 0)
        if modulo:
            self.__class__ = GaussianEliminationModulo
            self.__init__(dimension, matrix, augment_dimension, modulo)
        else:
            self.__class__ = GaussianEliminationDecimal
            self.__init__(dimension, matrix, augment_dimension, EPS)


class GaussianEliminationPrototype:
    """Gaussian elimination prototype
    
    Guassian elimination process
    """
    def __init__(self, dimension, matrix, augment_dimension):
        self.dimension = dimension
        self.matrix = matrix
        self.augment_dimension = augment_dimension

    def solve(self):
        """Solve the system of linear equations given
        
        Using normal Guassian elimination to solve
        
        Returns:
            bool -- whether the system is solvable or not
        """
        raise NotImplementedError


class GaussianEliminationDecimal(GaussianEliminationPrototype):
    """General Gaussian elimination
    
    Guassian elimination process
    
    Extends:
        GaussianEliminationPrototype
    """
    def __init__(self, dimension, matrix, augment_dimension, EPS):
        super(GaussianEliminationNormal, self).__init__(dimension, matrix, augment_dimension)
        self.EPS = EPS

    def sign(self, x):
        return -1 if x < -self.EPS else x > self.EPS

    def solve(self):
        for i in range(self.dimension):
            r = i
            for j in range(i + 1, self.dimension):
                if self.sign(abs(self.matrix[j][i]) - abs(self.matrix[r][i])) == 1:
                    r = j
            if self.sign(abs(self.matrix[r][i])) == 0:
                return False
            if not r == i:
                for j in range(self.dimension + self.augment_dimension):
                    self.matrix[r][j], self.matrix[i][j] = self.matrix[i][j], self.matrix[r][j]
            for k in range(i + 1, self.dimension):
                f = self.matrix[k][i] / self.matrix[i][i]
                for j in range(i, self.dimension + self.augment_dimension):
                    self.matrix[k][j] -= f * self.matrix[i][j]
        for i in range(self.dimension - 1, -1, -1):
            for j in range(i + 1, self.dimension):
                for k in range(self.dimension, self.dimension + self.augment_dimension):
                    self.matrix[i][k] -= self.matrix[j][k] * self.matrix[i][j]
            for k in range(self.dimension, self.dimension + self.augment_dimension):
                self.matrix[i][k] /= self.matrix[i][i]
        return True


class GaussianEliminationModulo(GaussianEliminationPrototype):
    """Gaussian elimination with modulo
    
    Guassian elimination process
    
    Extends:
        GaussianEliminationPrototype
    """
    def __init__(self, dimension, matrix, augment_dimension, modulo):
        super(GaussianEliminationModulo, self).__init__(dimension, matrix, augment_dimension)
        self.modulo = modulo

    def solve(self):
        diagonal_inverse = [0] * self.dimension
        for i in range(self.dimension):
            r = i
            for j in range(i + 1, self.dimension):
                if self.matrix[j][i] > self.matrix[r][i]:
                    r = j
            if not self.matrix[r][i]:
                return False
            if not r == i:
                for j in range(self.dimension + self.augment_dimension):
                    self.matrix[r][j], self.matrix[i][j] = self.matrix[i][j], self.matrix[r][j]
            diagonal_inverse[i] = inverse(self.matrix[i][i], self.modulo)
            if diagonal_inverse[i] < 0:
                raise ArithmeticError
            for k in range(i + 1, self.dimension):
                f = self.matrix[k][i] * diagonal_inverse[i] % self.modulo
                for j in range(i, self.dimension + self.augment_dimension):
                    self.matrix[k][j] -= f * self.matrix[i][j]
                    self.matrix[k][j] %= self.modulo
        for i in range(self.dimension - 1, -1, -1):
            for j in range(i + 1, self.dimension):
                for k in range(self.dimension, self.dimension + self.augment_dimension):
                    self.matrix[i][k] -= self.matrix[j][k] * self.matrix[i][j]
                    self.matrix[i][k] %= self.modulo
            for k in range(self.dimension, self.dimension + self.augment_dimension):
                self.matrix[i][k] *= diagonal_inverse[i]
                self.matrix[i][k] %= self.modulo
        return True
