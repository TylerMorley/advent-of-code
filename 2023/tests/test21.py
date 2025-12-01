import unittest
from code import day21

class PartOne(unittest.TestCase):
    def test_getGardenMap(self):
        filename = 'inputs/testinput21.txt'
        garden_map = day21.getGardenMap(filename)
        self.assertEqual(len(garden_map), 11)
        self.assertEqual(len(garden_map[0]), 11)

    def test_getNextSteps(self):
        garden_map = ['...........',
                      '.....###.#.',
                      '.###.##..#.',
                      '..#.#...#..',
                      '....#.#....',
                      '.##..S####.',
                      '.##..#...#.',
                      '.......##..',
                      '.##.#.####.',
                      '.##..##.##.',
                      '...........'
                      ]
        position = [5,5]
        paths = day21.getNextSteps(garden_map, position)
        self.assertEqual(len(paths), 2)
