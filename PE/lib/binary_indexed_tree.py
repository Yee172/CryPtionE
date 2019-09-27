class BinaryIndexedTree:
    """binary indexed tree
    
    simple binary indexed tree 1D
    """
    def __init__(self, size):
        self.size = size
        self.clear()

    def clear(self):
        self.tree = [0] * (self.size + 1)

    def add(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def get_sum(self, index):
        result = 0
        while index:
            result += self.tree[index]
            index -= index & -index
        return result
