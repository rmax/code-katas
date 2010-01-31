
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
        

