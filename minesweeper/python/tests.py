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


if __name__ == "__main__":
    unittest.main()
