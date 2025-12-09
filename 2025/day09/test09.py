import unittest
import day09

class PartOne(unittest.TestCase):
    def test_getInputs(self):
        red_tiles = day09.getInputs('testinput09.txt')
        self.assertEqual(len(red_tiles), 8)
        self.assertTrue([7,1] in red_tiles)

    def test_calcArea(self):
        corners = [[7,1],[11,7]]
        area = day09.calcArea(corners)
        self.assertEqual(area, 35)

    def test_findBiggestRect(self):
        red_tiles = [[7, 1], [11, 1], [11, 7], [9, 7], [9, 5], [2, 5], [2, 3], [7, 3]]
        biggest_area = day09.findBiggestRect(red_tiles)
        self.assertEqual(biggest_area, 50)
