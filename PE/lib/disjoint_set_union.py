class disjoint_set_union:
    """Disjoint set union (AKA dsu)

    Basis usages and functions
    """
    def __init__(self, length):
        self.father = [i for i in range(length)]

    def get_father(self, x):
        """Get the father of index x
        
        get the father of index x and compress the route
        
        Arguments:
            x {int} -- index
        
        Returns:
            int -- father of this index
        """
        self.father[x] = x if self.father[x] == x else self.get_father(self.father[x])
        return self.father[x]

    def union_father(self, x, y):
        """Union the set contains x and the set contains y
        
        union the most father of index x and index y
        
        Arguments:
            x {int} -- index
            y {int} -- index
        """
        self.father[self.get_father(y)] = self.get_father(x)
