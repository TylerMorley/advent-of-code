import unittest
from code import day17

class PartOne(unittest.TestCase):
    def test_getHeatMap(self):
        filename = 'inputs/testinput17.txt'
        heat_map = day17.getHeatMap(filename)
        self.assertEqual(len(heat_map), 13)
        self.assertEqual(len(heat_map[0]), 13)
        self.assertEqual(heat_map[2][12], 4)

    def test_move(self):
        self.assertTrue(False)
