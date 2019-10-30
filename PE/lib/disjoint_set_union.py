class DisjointSetUnionPrototype:
    """Disjoint set union (AKA dsu)

    Basis usages and functions
    """
    def __init__(self, length):
        self.father = [i for i in range(length)]

    def get_father(self, x):
        """Get the father of index x
        
        Get the father of index x and compress the route
        
        Arguments:
            x {int} -- index
        
        Returns:
            int -- father of this index
        """
        self.father[x] = x if self.father[x] == x else self.get_father(self.father[x])
        return self.father[x]

    def union_father(self, x, y):
        """Union the set contains x and the set contains y
        
        Union the most father of index x and index y
        
        Arguments:
            x {int} -- index
            y {int} -- index
        """
        self.father[self.get_father(y)] = self.get_father(x)


class DisjointSetUnion(DisjointSetUnionPrototype):
    """Disjoint set union

    Same as DisjointSetUnionPrototype
    """
    pass


class DisjointSetUnionCounting(DisjointSetUnionPrototype):
    """Disjoint set union with counting

    Basis usages and functions
    """
    def __init__(self, length):
        super(DisjointSetUnionCounting, self).__init__(length)
        self.quantity = [1] * length

    def union_father(self, x, y):
        """Union the set contains x and the set contains y with counting
        
        Union the most father of index x and index y with counting
        
        Arguments:
            x {int} -- index
            y {int} -- index
        """
        x = self.get_father(x)
        y = self.get_father(y)
        if x != y:
            self.quantity[x] += self.quantity[y]
            self.father[y] = x

    def get_quantity(self, x):
        """Get the quantity of one set
        
        Get the quantity of the father of index x
        
        Arguments:
            x {int} -- index
        
        Returns:
            int -- quantity of the set contains index x
        """
        return self.quantity[self.get_father(x)]
