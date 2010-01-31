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

    def test_is_bomb(self):
        # is_bomb returns bool
        #         raises IndexError
        field = Field([['.', '.', '*'],
                       ['*', '.', '.'],
                       ['.', '*', '.']])

        self.assertRaises(IndexError, field.is_bomb, 0, -1)
        self.assertRaises(IndexError, field.is_bomb, -1, 0)
        self.assertRaises(IndexError, field.is_bomb, 3, 3)

        self.assertTrue(field.is_bomb(2, 1))
        self.assertFalse(field.is_bomb(1, 1))

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

    def test_find_adjacents(self):
        # find_adjacents returns adjacents' indexes
        # find_adjacents returns generator
        # find_adjacents returns empty on non-existent index
        field = Field([['.', '.', '*'],
                       ['*', '.', '.'],
                       ['.', '*', '.']])

        # test invalid indexes
        adjacents = list(field.find_adjacents(0, -1))
        self.assertEquals(adjacents, [])
        adjacents = list(field.find_adjacents(-1, 0))
        self.assertEquals(adjacents, [])
        adjacents = list(field.find_adjacents(3, 3))
        self.assertEquals(adjacents, [])

        adjacents = list(field.find_adjacents(0, 0))
        self.assertEquals(adjacents, [(0, 1), (1, 0), (1, 1)])

        adjacents = list(field.find_adjacents(0, 2))
        self.assertEquals(adjacents, [(0, 1), (1, 1), (1, 2)])

        adjacents = list(field.find_adjacents(2, 0))
        self.assertEquals(adjacents, [(1, 0), (1, 1), (2, 1)])

        adjacents = list(field.find_adjacents(2, 2))
        self.assertEquals(adjacents, [(1, 1), (1, 2), (2, 1)])

        adjacents = list(field.find_adjacents(1, 1))
        self.assertEquals(adjacents, [(0, 0), (0, 1), (0, 2),
                                      (1, 0),         (1, 2),
                                      (2, 0), (2, 1), (2, 2)])

    def test_count_adjacents_bombs(self):
        # count_adjacents_bombs returns integer
        # count_adjacents_bombs raises IndexError on invalid index
        field = Field([['.', '.', '*'],
                       ['*', '.', '.'],
                       ['.', '*', '.']])

        self.assertRaises(IndexError, field.count_adjacents_bombs, -1, 0)
        self.assertRaises(IndexError, field.count_adjacents_bombs, 0, -1)
        self.assertRaises(IndexError, field.count_adjacents_bombs, 3, 3)

        self.assertEquals(field.count_adjacents_bombs(0, 0), 1)
        self.assertEquals(field.count_adjacents_bombs(0, 2), 0)
        self.assertEquals(field.count_adjacents_bombs(1, 1), 3)
        self.assertEquals(field.count_adjacents_bombs(1, 2), 2)
        self.assertEquals(field.count_adjacents_bombs(2, 0), 2)
        self.assertEquals(field.count_adjacents_bombs(2, 2), 1)




if __name__ == "__main__":
    unittest.main()
