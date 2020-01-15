from random import random, randint, choice


class Grid:
    def __init__(self):
        self.base_grid = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            # ----------------------- #
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            # ----------------------- #
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]
        ]
        self.grid = self.base_grid

    def show(self, grid):
        for i in grid:
            print(i)

    def transpose(self):
        """Transposing the whole grid"""
        transposed = self.grid
        for i in range(0, len(self.base_grid)):
            for j in range(0, len(self.base_grid[i])):
                transposed[j][i] = self.grid[i][j]

    def swap_rows(self):
        """Swaps rows in one area"""
        n = choice([3, 6])
        ind_1 = randint(0, 2)
        ind_2 = randint(0, 2)
        if ind_2 == ind_1:
            ind_2 = randint(0, 2)
        ind_1 += n
        ind_2 += n
        print(ind_1, ind_2)
        self.grid[ind_1], self.grid[ind_2] = self.grid[ind_2], self.grid[ind_1]

    def swap_horizontal_areas(self):
        """Swaps horizontal areas"""
        ind_1 = choice([0, 3, 6])
        ind_2 = choice([0, 3, 6])
        while ind_2 == ind_1:
            ind_2 = choice([0, 3, 6])
        print(ind_1, ind_2)
        for i in range(0, 3):
            self.grid[i + ind_1], self.grid[i + ind_2] = self.grid[i + ind_2], self.grid[i + ind_1]


if __name__ == '__main__':
    grid = Grid()
    print('Grid before changes')
    grid.show(grid.base_grid)
    grid.swap_rows()
    print('Changed grid')
    grid.show(grid.grid)
