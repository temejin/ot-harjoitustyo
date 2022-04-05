import random
from tile import Tile

class Field:
    def __init__(self, height, width, mines):
        self.grid = [ [Tile() for j in range(width)] for i in range(height)]
        mines_set = 0
        while mines_set < mines:
            y = random.randint(0,height-1)
            x = random.randint(0,height-1)
            if not self.grid[y][x].mine:
                self.grid[y][x].mine = True
                mines_set += 1
        
        # update adjacent
        for y in range(height):
            for x in range(width):
                if not self.grid[y][x].mine:
                    self.grid[y][x].check_adjacent_mines(self.grid, width, height, y, x)

        for row in self.grid:
            for tile in row:
                a = -1 if tile.mine else tile.adjacent_mines
                print("%3d" % a, end="")
            print()

