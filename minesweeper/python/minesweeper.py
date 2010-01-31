
class Field(object):
    """
    This class represents Minesweeper's Field
    """

    def __init__(self, field):
        """
        Constructor.
        
        field -- matrix, embedded list
        """
        assert isinstance(field, list)
        self._field = field
        self.height = len(field)
        self.width = len(field[0]) if self.height > 0 else 0
        

