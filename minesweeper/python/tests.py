import unittest

from minesweeper import Field

class MinesweeperTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_field_size(self):
        field = Field([])
        self.assertEquals(field.width, 0)
        self.assertEquals(field.height, 0)

        field = Field([[]])
        self.assertEquals(field.width, 0)
        self.assertEquals(field.height, 1)

        field = Field([['.']])
        self.assertEquals(field.width, 1)
        self.assertEquals(field.height, 1)

        field = Field([['.', '.']])
        self.assertEquals(field.width, 2)
        self.assertEquals(field.height, 1)

        field = Field([['.', '.'], ['.', '.']])
        self.assertEquals(field.width, 2)
        self.assertEquals(field.height, 2)

    def test_invalid_field(self):
        # validate non-equal length rows
        self.assertRaises(ValueError, Field, [['.'], ['.', '.']])
        self.assertRaises(ValueError, Field, [['.', '.', '.'], ['.', '.']])

    def test_input_only_dot_and_star(self):
        # valid input only dot and start
        self.assert_(Field([['.', '*']]))
        self.assertRaises(ValueError, Field, [['.', 'a'], ['.', '*']])
        self.assertRaises(ValueError, Field, [['.', '.'], ['.', 1]])

    def test_find_bombs(self):
        # find_bombs shuold returns bomb indexes
        # find_bombs returns generator
        field = Field([])
        indexes = list(field.find_bombs())
        self.assertEquals(indexes, [])

        field = Field([[]])
        indexes = list(field.find_bombs())
        self.assertEquals(indexes, [])

        field = Field([['.']])
        indexes = list(field.find_bombs())
        self.assertEquals(indexes, [])

        field = Field([['*']])
        indexes = list(field.find_bombs())
        self.assertEquals(indexes, [(0, 0)])

        field = Field([['.', '*']])
        indexes = list(field.find_bombs())
        self.assertEquals(indexes, [(0, 1)])

        field = Field([['*', '*']])
        indexes = list(field.find_bombs())
        self.assertEquals(indexes, [(0, 0), (0, 1)])

        field = Field([['.', '.', '*'],
                       ['*', '.', '.'],
                       ['.', '*', '.']])
        indexes = list(field.find_bombs())
        self.assertEquals(indexes, [(0, 2), (1, 0), (2, 1)])




if __name__ == "__main__":
    unittest.main()
