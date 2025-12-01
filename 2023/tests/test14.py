import unittest
from code import day14

class PartOne(unittest.TestCase):
    def test_getPlatform(self):
        filename = 'inputs/testinput14.txt'
        platform = day14.getPlatform(filename)
        self.assertEqual(len(platform), 10)
        self.assertEqual(platform[6], '..O..#O..O')

    def test_tiltNorth(self):
        platform = ['O....#....',
                    'O.OO#....#',
                    '.....##...',
                    'OO.#O....O',
                    '.O.....O#.',
                    'O.#..O.#.#',
                    '..O..#O..O',
                    '.......O..',
                    '#....###..',
                    '#OO..#....'
                    ]
        tilted = day14.tiltNorth(platform)
        self.assertEqual(platform[0][1], 'O')

