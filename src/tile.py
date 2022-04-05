class Tile:
    def __init__(self):
        self.adjacent_mines = 0
        self.mine = False
        self.revealed = False

    def check_adjacent_mines(self, grid, width, height, y, x):
        for j in range(-1, 2):
            if (y == 0 and j == -1) or y+j == height:
                continue
            for i in range(-1, 2):
                if (x == 0 and i == -1) or x+i == width:
                    continue
                if grid[y+j][x+i].mine:
                    self.adjacent_mines += 1
        return self.adjacent_mines
