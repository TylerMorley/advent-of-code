import unittest
from code import day22

class PartOne(unittest.TestCase):
    def test_getBricks(self):
        filename = 'inputs/testinput22.txt'
        bricks = day22.getBricks(filename)
        self.assertEqual(len(bricks), 7)
        self.assertTrue([1,0,1] in bricks[0])

    def test_dropBrick(self):
        brick = [[1, 0, 1], [1, 2, 1]]
        tower = dict()
        tower = day22.dropBrick(tower, brick)
        self.assertTrue(brick in tower)
