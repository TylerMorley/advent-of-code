import unittest
import day04

class PartOne(unittest.TestCase):
    def setUp(self):
        self.grid = ['..@@.@@@@.', 
             '@@@.@.@.@@', 
             '@@@@@.@.@@', 
             '@.@@@@..@.', 
             '@@.@@@@.@@', 
             '.@@@@@@@.@', 
             '.@.@.@.@@@', 
             '@.@@@.@@@@', 
             '.@@@@@@@@.', 
             '@.@.@@@.@.']
    def test_getInputs(self):
        filename = 'testinput04.txt'
        grid = day04.getInputs(filename)
        
        self.assertEqual(len(grid), 10)
        self.assertEqual(len(grid[0]), 10)

    def test_getAdjacent(self):
        grid = self.grid.copy()
        location = [0,0]
        adjacents = day04.getAdjacent(location, grid)
        
        self.assertTrue([0,1] in adjacents)
        self.assertTrue([1,0] in adjacents)
        self.assertTrue([1,1] in adjacents)
        self.assertFalse([-1,-1] in adjacents)

        location = [1,1]
        adjacents = day04.getAdjacent(location, grid)
        self.assertEqual(len(adjacents), 8)

    def test_countPaperRolls(self):
        grid = self.grid.copy()
        adjacents = [[3, 0], [3, 1], [2, 1], [1, 0], [1, 1]]
        num_rolls = day04.countPaperRolls(adjacents, grid)
        expected = 3
        self.assertEqual(num_rolls, expected)

        adjacents = [[8, 0], [8, 1], [7, 1], [6, 0], [6, 1]]
        num_rolls = day04.countPaperRolls(adjacents, grid)
        expected = 4
        self.assertEqual(num_rolls, expected)

    def test_getForkliftAccessibility(self):
        grid = self.grid.copy()
        num_accessible = day04.getForkliftAccessibility(grid)
        expected = 13
        self.assertEqual(num_accessible, expected)

class PartTwo(unittest.TestCase):
    def setUp(self):
        self.grid = ['..@@.@@@@.', 
             '@@@.@.@.@@', 
             '@@@@@.@.@@', 
             '@.@@@@..@.', 
             '@@.@@@@.@@', 
             '.@@@@@@@.@', 
             '.@.@.@.@@@', 
             '@.@@@.@@@@', 
             '.@@@@@@@@.', 
             '@.@.@@@.@.']

    def test_getForkliftAccessibility2(self):
        grid = self.grid.copy()
        remove_rolls = True
        locs_accessible = day04.getForkliftAccessibility(grid, remove_rolls)
        self.assertEqual(len(locs_accessible), 13)
        self.assertTrue([2,0] in locs_accessible)

    def test_removeRolls(self):
        grid = self.grid.copy()
        to_remove = [[2,0],[3,0],[5,0],[6,0],[8,0],[0,1],[2,6],[4,0],[4,9],[7,0],[9,0],[9,2],[9,8]]
        new_grid = day04.removeRolls(to_remove, grid)
        self.assertEqual(new_grid[0][2], 'X')
        for location in to_remove:
            x,y = location
            self.assertEqual(new_grid[y][x], 'X')

    def test_getMaxAccessibility(self):
        grid = self.grid.copy()
        num_accessible = day04.getMaxAccessibility(grid)
        expected = 43
        self.assertEqual(num_accessible, expected)
