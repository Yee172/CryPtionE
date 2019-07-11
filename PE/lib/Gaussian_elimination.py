class Gaussian_elimination:
    """Gaussian elimination
    
    Normal Guassian elimination process
    """
    @staticmethod
    def sign(x):
        eps = 1e-8
        return -1 if x < -eps else x > eps

    def __init__(self, dimension, matrix, augment_dimension=1):
        self.dimension = dimension
        self.matrix = matrix
        self.augment_dimension = augment_dimension

    def solve(self, **kwargs):
        """Solve the system of linear equations given
        
        Using normal Guassian elimination to solve
        
        Arguments:
            **kwargs {[type]} -- [description]
                modulo {int} -- modulo number (default: {0})
        
        Returns:
            bool -- whether the system is solvable or not
        """
        module = kwargs.get('module', 0)

        if module:
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
                diagonal_inverse[i] = pow(self.matrix[i][i], module - 2, module)
                for k in range(i + 1, self.dimension):
                    f = self.matrix[k][i] * diagonal_inverse[i] % module
                    for j in range(i, self.dimension + self.augment_dimension):
                        self.matrix[k][j] -= f * self.matrix[i][j]
                        self.matrix[k][j] %= module
            for i in range(self.dimension - 1, -1, -1):
                for j in range(i + 1, self.dimension):
                    for k in range(self.dimension, self.dimension + self.augment_dimension):
                        self.matrix[i][k] -= self.matrix[j][k] * self.matrix[i][j]
                        self.matrix[i][k] %= module
                for k in range(self.dimension, self.dimension + self.augment_dimension):
                    self.matrix[i][k] *= diagonal_inverse[i]
                    self.matrix[i][k] %= module
            return True

        for i in range(self.dimension):
            r = i
            for j in range(i + 1, self.dimension):
                if Gaussian_elimination.sign(abs(self.matrix[j][i]) - abs(self.matrix[r][i])) == 1:
                    r = j
            if Gaussian_elimination.sign(abs(self.matrix[r][i])) == 0:
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
