import unittest
import day08

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.antenna_map = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

    def test_getInput(self):
        filename = 'testinput08.txt'
        antenna_map = day08.getInput(filename)
        expected = self.antenna_map
        self.assertEqual(antenna_map, expected)

    def test_getLocations(self):
        antenna_map = self.antenna_map
        antennas = day08.getLocations(antenna_map)
        expected = {'0':[[8,1],[5,2],[7,3],[4,4]], 'A':[[6,5],[8,8],[9,9]]}
        self.assertEqual(len(antennas), len(expected))
        for zero in expected['0']:
            self.assertTrue(zero in antennas['0'])

    def test_makeAntinode(self):
        current = [8,1]
        other = [5,2]
        antinode = day08.makeAntinode(current, other)
        expected = {'x11y0', 'x2y3'}
        for exp in expected:
            self.assertTrue(exp in antinode)

    def test_makeAntinodes(self):
        antennas = {'a':[[4,3],[5,5]]}
        antinodes = day08.makeAntinodes(antennas)
        self.assertEqual(len(antinodes), 2)
        expected = {'x3y1', 'x6y7'}
        for exp in expected:
            self.assertTrue(exp in antinodes)

        antennas = {'0':[[8,1],[5,2],[7,3],[4,4]], 'A':[[6,5],[8,8],[9,9]]}
        antinodes = day08.makeAntinodes(antennas)
        self.assertEqual(len(antinodes), 17)

    def test_isInbounds(self):
        height, width = [12,12]

        antinode = 'x12y3'
        is_inbounds = day08.is_inbounds(height, width, antinode)
        self.assertFalse(is_inbounds)

    def test_uniqueLocs(self):
        antenna_map = self.antenna_map.copy()

        unique = day08.uniqueLocs(antenna_map)
        self.assertEqual(len(unique), 14)

class TestPartTwo(unittest.TestCase):
    def test_makeAntinodes_rh:
        antenna_map = [['T','.','.','.','.','#','.','.','.','.'],
                       ['.','.','.','T','.','.','.','.','.','.'],
                       ['.','T','.','.','.','.','#','.','.','.'],
                       ['.','.','.','.','.','.','.','.','.','#'],
                       ['.','.','#','.','.','.','.','.','.','.'],
                       ['.','.','.','.','.','.','.','.','.','.'],
                       ['.','.','.','#','.','.','.','.','.','.'],
                       ['.','.','.','.','.','.','.','.','.','.'],
                       ['.','.','.','.','#','.','.','.','.','.'],
                       ['.','.','.','.','.','.','.','.','.','.']]

        antennas = {'T':[[0,0],[1,2],[3,1]}
        antinodes = day08.makeAntinodes(antennas)
        self.assertEqual(len(antinodes), 17)

