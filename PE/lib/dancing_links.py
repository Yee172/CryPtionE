# modified from https://philoscience.iteye.com/blog/1537004


class DancingNode:
    def __init__(self, left=None, right=None, up=None, down=None, column_header=None, row_header=None):
        self.left = left or self
        self.right = right or self
        self.up = up or self
        self.down = down or self
        self.column_header = column_header
        self.row_header = row_header

    def get_nodes_in_direction(self, direction):
        dancing_node = getattr(self, direction)
        while dancing_node != self:
            yield dancing_node
            dancing_node = getattr(dancing_node, direction)


class ColumnHeader(DancingNode):
    def __init__(self, *args, **kargs):
        DancingNode.__init__(self, *args, **kargs)
        self.size = 0


class RowHeader(DancingNode):
    def __init__(self, row_number, *args, **kargs):
        DancingNode.__init__(self, *args, **kargs)
        self.row_number = row_number
        self.row_header = self


class DancingLinks:
    DIRECTION = ['left', 'right', 'up', 'down']
    DIRECTION_INVERSE = {'left': 0, 'right': 1, 'up': 2, 'down': 3}

    @staticmethod
    def _inverse_direction(direction):
        return DancingLinks.DIRECTION[DancingLinks.DIRECTION_INVERSE[direction] ^ 1]

    @staticmethod
    def _insert(origin, addition, direction):
        """Insert a dancing node in direction
        From:
           ----------             ----------
           | origin | <---------> |   to   |
           ----------             ----------
        To:
           ----------             ----------             ----------
           | origin | <---------> |addition| <---------> |   to   |
           ----------             ----------             ----------
        where, direction is ---------->
        """
        inverse_direction = DancingLinks._inverse_direction(direction)
        setattr(addition, direction, getattr(origin, direction))
        setattr(addition, inverse_direction, origin)
        setattr(getattr(origin, direction), inverse_direction, addition)
        setattr(origin, direction, addition)

    @staticmethod
    def _delete(origin, direction):
        """Delete a dancing node in direction
        From:
           ----------             ----------             ----------
           | node A | <---------> | origin | <---------> | node B |
           ----------             ----------             ----------
        To:
           ----------             ----------
           | node A | <---------> | node B |
           ----------             ----------
        where, direction is ---------->
        """
        inverse_direction = DancingLinks._inverse_direction(direction)
        setattr(getattr(origin, inverse_direction), direction, getattr(origin, direction))
        setattr(getattr(origin, direction), inverse_direction, getattr(origin, inverse_direction))

    @staticmethod
    def _restore(origin, direction):
        """Inverse operation of _delete
        """
        inverse_direction = DancingLinks._inverse_direction(direction)
        setattr(getattr(origin, inverse_direction), direction, origin)
        setattr(getattr(origin, direction), inverse_direction, origin)

    @staticmethod
    def _cover(column_header):
        DancingLinks._delete(column_header, 'left')
        for each_dancing_node_down in column_header.get_nodes_in_direction('down'):
            for each_dancing_node_right in each_dancing_node_down.get_nodes_in_direction('right'):
                each_dancing_node_right.column_header.size -= 1
                DancingLinks._delete(each_dancing_node_right, 'up')

    @staticmethod
    def _recover(column_header):
        for each_dancing_node_up in column_header.get_nodes_in_direction('up'):
            for each_dancing_node_left in each_dancing_node_up.get_nodes_in_direction('left'):
                each_dancing_node_left.column_header.size += 1
                DancingLinks._restore(each_dancing_node_left, 'down')
        DancingLinks._restore(column_header, 'right')

    def __init__(self):
        self.root = None
        self.column_headers = None
        self._result = None
        self._n = None

    def _construct(self, sparse_matrix, column_number):
        """
        Sparse matrix should be a list or set of increasing indexes of each row
           Example: [[0, 2, 4], [3, 5], [1, 6]]
        """
        self.root = DancingNode()
        self.column_headers = []

        for i in range(column_number):
            column_header = ColumnHeader()
            DancingLinks._insert(self.root, column_header, 'left')
            self.column_headers.append(column_header)

        for i, column_id_of_each_row in enumerate(sparse_matrix):
            if not column_id_of_each_row:
                continue
            column_header = self.column_headers[column_id_of_each_row[0]]
            column_header.size += 1

            row_header = RowHeader(i, column_header=column_header)
            DancingLinks._insert(column_header, row_header, 'up')

            for k in column_id_of_each_row[1:]:
                column_header = self.column_headers[k]
                column_header.size += 1

                dancing_node = DancingNode(column_header=column_header, row_header=row_header)
                DancingLinks._insert(column_header, dancing_node, 'up')
                DancingLinks._insert(row_header, dancing_node, 'left')

    def _search(self, n):
        if self.root.right == self.root:
            self._n = n
            return True

        column_header = min(list(self.root.get_nodes_in_direction('right')), key=lambda header: header.size)
        self._cover(column_header)
        for each_dancing_node_down in column_header.get_nodes_in_direction('down'):
            self._result[n] = each_dancing_node_down.row_header.row_number

            for each_dancing_node_right in each_dancing_node_down.get_nodes_in_direction('right'):
                self._cover(each_dancing_node_right.column_header)

            if self._search(n + 1):
                return True

            for each_dancing_node_left in each_dancing_node_down.get_nodes_in_direction('left'):
                self._recover(each_dancing_node_left.column_header)

        self._recover(column_header)
        return False

    def solve(self, sparse_matrix, column_number):
        """
        Sparse matrix should be a list or set of increasing indexes of each row
           Example: [[0, 2, 4], [3, 5], [1, 6]]
        """
        self._result = {}
        self._n = 0
        self._construct(sparse_matrix, column_number)
        self._search(0)

        return [self._result[n] for n in range(self._n)]
