from matrix import Matrix
from slice_lib import rearrange_slice_for_infinite_sequence


class PellEquation:
    """Pell Equation
    
    x^{2} - D y^{2} = 1, where D is a postive integer
    solving for positive integer pair (x, y) satisfying the equation with the minimum solution of x below the upper bound
    """
    def __init__(self, D, x_upper_bound=0, modulo=0):
        if not isinstance(D, int) or D < 1:
            raise TypeError('D should be a positive integer')
        self.D = D
        self.x_upper_bound = x_upper_bound
        self.modulo = modulo
        self.solution_out_of_upper_bound = False
        self.minimum_x, self.minimum_y = self.__get_minimum_positive_solution()
        self.no_solution = self.minimum_x == 1
        self.transfer_matrix = self.__get_transfer_matrix()

    def __get_minimum_positive_solution(self):
        if self.x_upper_bound > 0:
            return self.__get_minimum_positive_solution_within_upper_bound()
        else:
            return self.__get_minimum_positive_solution_without_upper_bound()

    def __get_minimum_positive_solution_without_upper_bound(self):
        s = self.D ** .5
        p = 1
        q = int(s)
        if q ** 2 == self.D:
            return 1, 0
        x, y, last_x, last_y = q, 1, 1, 0
        while True:
            t = int(p / (s - q))
            p, q = q, (self.D - q ** 2) // p
            p, q = q, q * t - p
            x, y, last_x, last_y = t * x + last_x, t * y + last_y, x, y
            if x ** 2 - self.D * y ** 2 == 1:
                break
        return x, y

    def __get_minimum_positive_solution_within_upper_bound(self):
        s = self.D ** .5
        p = 1
        q = int(s)
        if q ** 2 == self.D:
            return 1, 0
        x, y, last_x, last_y = q, 1, 1, 0
        while x < self.x_upper_bound:
            t = int(p / (s - q))
            p, q = q, (self.D - q ** 2) // p
            p, q = q, q * t - p
            x, y, last_x, last_y = t * x + last_x, t * y + last_y, x, y
            if x ** 2 - self.D * y ** 2 == 1:
                break
        if x < self.x_upper_bound:
            return x, y
        else:
            self.solution_out_of_upper_bound = True
            return 1, 0

    def __get_transfer_matrix(self):
        if self.no_solution:
            return None
        transfer_matrix = Matrix(2, modulo=self.modulo)
        transfer_matrix[0] = [self.minimum_x, self.D * self.minimum_y]
        transfer_matrix[1] = [self.minimum_y, self.minimum_x]
        return transfer_matrix

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__get_solution_by_index(item)
        elif isinstance(item, slice):
            return self.__get_solution_by_range(item)
        else:
            raise TypeError('list indices must be integers or slices, not {}'.format(item.__class__.__name__))

    def __get_solution_by_index(self, index):
        result = self.transfer_matrix ** (index + 1)
        return result[0][0], result[1][0]

    def __get_solution_by_range(self, slice_item):
        reverse_flag, minimum, maximum, step = rearrange_slice_for_infinite_sequence(slice_item)
        if minimum >= maximum:
            return []
        result = [(0, 0)] * ((maximum - minimum - 1) // step + 1)
        s = self.transfer_matrix ** step
        r = self.transfer_matrix ** (minimum + 1)
        if reverse_flag:
            result[-1] = r[0][0], r[1][0]
            for j in range(len(result) - 2, -1, -1):
                r *= s
                result[j] = r[0][0], r[1][0]
        else:
            result[0] = r[0][0], r[1][0]
            for j in range(1, len(result)):
                r *= s
                result[j] = r[0][0], r[1][0]
        return result
