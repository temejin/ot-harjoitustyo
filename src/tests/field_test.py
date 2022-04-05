import unittest
from field import Field

class TestField(unittest.TestCase):
    def setUp(self):
        self.field = Field(10, 10, 20)

    def test_correct_amount_of_mines_set(self):
        mines = 0
        for y in range(10):
            for x in range(10):
                if self.field.grid[y][x].mine:
                    mines += 1
        self.assertEqual(mines, 20)
