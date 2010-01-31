
class Field(object):
    """
    This class represents Minesweeper's Field
    """

    def __init__(self, field):
        """
        Constructor.
        
        field -- embedded list
        """
        assert isinstance(field, list)
        self._field = field

        # initialize size
        self.height = len(field)
        self.width = len(field[0]) if self.height > 0 else 0

        # validate if all rows have same length
        for row in self._field:
            if len(row) != self.width:
                raise ValueError('Invalid row length %d != %d: %r' \
                            % (self.width, len(row), row))

        # validate characters
        for row in self._field:
            for cell in row:
                if cell not in ('.', '*'):
                    raise ValueError('Only dot (.) and start (*)'
                                     'expected. Found %r ' % cell)

    def is_bomb(self, i, j):
        """
        Checks if given index is bomb
        """
        if 0 <= i < self.height and 0 <= j < self.width:
            return self._field[i][j] == '*'
        else:
            raise IndexError('Invalid index (%d, %d)' % (i, j))

    def find_bombs(self):
        """
        Yields bomb indexes (tuple)
        """
        for i,row in enumerate(self._field):
            for j,cell in enumerate(row):
                if cell == '*':
                    yield (i,j)

        # no index found
        raise StopIteration

    def find_adjacents(self, i, j):
        """
        Yields adjacent indexes
        """
        # check if cell index exists
        # - negative index
        # - out of bound
        if 0 <= i < self.height and 0 <= j < self.width:
            # walk over all sourranding index
            # Note: xrange generates i-1 <= m < i+2
            for m in xrange(i-1, i+2):
                for n in xrange(j-1, j+2):
                    if (m, n) != (i, j) and 0 <= m < self.height and 0 <= n < self.width:
                        yield (m, n)

        raise StopIteration
        
        
    def count_adjacents_bombs(self, i, j):
        if 0 <= i < self.height and 0 <= j < self.width:
            return sum(1 for (m,n) in self.find_adjacents(i,j) if self.is_bomb(m,n))
        else:
            raise IndexError('Invalid index (%d, %d)' % (i, j))

