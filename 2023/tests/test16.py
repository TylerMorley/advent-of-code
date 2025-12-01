import unittest
from code import day16

class PartOne(unittest.TestCase):
    def test_getContraption(self):
        filename = 'inputs/testinput16.txt'
        contraption = day16.getContraption(filename)
        self.assertEqual(len(contraption), 10)

    def test_move(self):
        location = [0,1]
        direction = 'r'
        new_loc = day16.move(location, direction)
        self.assertEqual(new_loc, [0,2])

        location = [0,2]
        direction = 'l'
        new_loc = day16.move(location, direction)
        self.assertEqual(new_loc, [0,1])

        location = [1,2]
        direction = 'd'
        new_loc = day16.move(location, direction)
        self.assertEqual(new_loc, [2,2])

        location = [2,2]
        direction = 'u'
        new_loc = day16.move(location, direction)
        self.assertEqual(new_loc, [1,2])

    def test_takeStep(self):
        location, direction = [[0,1], 'r']
        contents = '.'
        next_step = day16.takeStep(location, direction, contents)
        self.assertEqual(next_step[0], [0,2])
        self.assertEqual(next_step[1], 'r')

        location, direction = [[0,2], 'r']
        contents = '\\'
        next_step = day16.takeStep(location, direction, contents)
        self.assertEqual(next_step[0], [1,1])
        self.assertEqual(next_step[1], 'd')
