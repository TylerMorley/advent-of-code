import unittest
from code import day24

class PartOne(unittest.TestCase):
    def test_getTrajectories(self):
        filename = 'inputs/testinput24.txt'
        trajectories = day24.getTrajectories(filename)
        self.assertEqual(len(trajectories), 5)
        self.assertEqual(len(trajectories[3]), 2)
        self.assertEqual(trajectories[3][0], [12, 31, 28])
