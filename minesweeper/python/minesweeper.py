"""
Minesweeper Kata

Problem: http://acm.uva.es/p/v101/10189.html
"""

import copy

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

    def is_empty(self):
        """
        Returns True if field has no rows or columns
        """
        return self.height == 0 or self.width == 0

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
        for (i, row) in enumerate(self._field):
            for (j, cell) in enumerate(row):
                if cell == '*':
                    yield (i, j)

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
                    if 0 <= m < self.height and 0 <= n < self.width \
                        and (m, n) != (i, j): 
                        yield (m, n)

        raise StopIteration
        
        
    def count_adjacents_bombs(self, i, j):
        """
        Returns the total count of sourranding bombs
        """
        if 0 <= i < self.height and 0 <= j < self.width:
            return sum(1 for (m, n) in self.find_adjacents(i, j)
                        if self.is_bomb(m,n))
        else:
            raise IndexError('Invalid index (%d, %d)' % (i, j))

    def resolve(self):
        """
        Returns resolved field
        """
        result = copy.copy(self._field)
        for i in xrange(self.height):
            for j in xrange(self.width):
                if not self.is_bomb(i, j):
                    result[i][j] = str(self.count_adjacents_bombs(i, j))

        return result

