import unittest
from code import day10

class PartOne(unittest.TestCase):
    def test_getPipes(self):
        filename = 'inputs/testinput10-1.txt'
        pipes = day10.getPipes(filename)
        self.assertEqual(len(pipes), 25)
        self.assertEqual(pipes['x1y1'], 'S')
        self.assertEqual(pipes['x1y3'], 'L')

    def test_getXAndY(self):
        key = 'x0y3'
        x,y = day10.getXAndY(key)
        self.assertEqual(x, 0)
        self.assertEqual(y, 3)
        key = 'x108y25'
        x,y = day10.getXAndY(key)
        self.assertEqual(x, 108)
        self.assertEqual(y, 25)
        

    def test_getConnections(self):
        pipes = {'x0y0': '-', 'x1y0': 'L', 'x2y0': '|', 'x3y0': 'F', 'x4y0': '7',
                 'x0y1': '7', 'x1y1': 'S', 'x2y1': '-', 'x3y1': '7', 'x4y1': '|',
                 'x0y2': 'L', 'x1y2': '|', 'x2y2': '7', 'x3y2': '|', 'x4y2': '|',
                 'x0y3': '-', 'x1y3': 'L', 'x2y3': '-', 'x3y3': 'J', 'x4y3': '|',
                 'x0y4': 'L', 'x1y4': '|', 'x2y4': '-', 'x3y4': 'J', 'x4y4': 'F'}
        tile = 'x3y1'
        connections = day10.getConnections(pipes, tile)
        self.assertEqual(len(connections), 2)
        self.assertTrue('x3y2' in connections)
        self.assertTrue('x2y1' in connections)

    def test_getStartingPoint(self):
        pipes = {'x0y0': '-', 'x1y0': 'L', 'x2y0': '|', 'x3y0': 'F', 'x4y0': '7',
                 'x0y1': '7', 'x1y1': 'S', 'x2y1': '-', 'x3y1': '7', 'x4y1': '|',
                 'x0y2': 'L', 'x1y2': '|', 'x2y2': '7', 'x3y2': '|', 'x4y2': '|',
                 'x0y3': '-', 'x1y3': 'L', 'x2y3': '-', 'x3y3': 'J', 'x4y3': '|',
                 'x0y4': 'L', 'x1y4': '|', 'x2y4': '-', 'x3y4': 'J', 'x4y4': 'F'}
        location, shape = day10.getStartingPoint(pipes)
        self.assertEqual(location, 'x1y1')
        self.assertEqual(shape, 'F')
        pipes = {'x0y0': '7', 'x1y0': '-', 'x2y0': 'F', 'x3y0': '7', 'x4y0': '-',
                 'x0y1': '.', 'x1y1': 'F', 'x2y1': 'J', 'x3y1': '|', 'x4y1': '7',
                 'x0y2': 'S', 'x1y2': 'J', 'x2y2': 'L', 'x3y2': 'L', 'x4y2': '7',
                 'x0y3': '|', 'x1y3': 'F', 'x2y3': '-', 'x3y3': '-', 'x4y3': 'J',
                 'x0y4': 'L', 'x1y4': 'J', 'x2y4': '.', 'x3y4': 'L', 'x4y4': 'J',}
        location, shape = day10.getStartingPoint(pipes)
        self.assertEqual(location, 'x0y2')
        self.assertEqual(shape, 'F')
        pipes = {'x0y0': '7', 'x1y0': '-', 'x2y0': 'F', 'x3y0': '7', 'x4y0': '-',
                 'x0y1': '.', 'x1y1': 'F', 'x2y1': 'J', 'x3y1': '|', 'x4y1': '7',
                 'x0y2': 'F', 'x1y2': 'J', 'x2y2': 'L', 'x3y2': 'L', 'x4y2': '7',
                 'x0y3': 'S', 'x1y3': 'F', 'x2y3': '-', 'x3y3': '-', 'x4y3': 'J',
                 'x0y4': 'L', 'x1y4': 'J', 'x2y4': '.', 'x3y4': 'L', 'x4y4': 'J',}
        location, shape = day10.getStartingPoint(pipes)
        self.assertEqual(location, 'x0y3')
        self.assertEqual(shape, '|')
        

    def test_getMainLoop(self):
        pipes = {'x0y0': '-', 'x1y0': 'L', 'x2y0': '|', 'x3y0': 'F', 'x4y0': '7',
                 'x0y1': '7', 'x1y1': 'S', 'x2y1': '-', 'x3y1': '7', 'x4y1': '|',
                 'x0y2': 'L', 'x1y2': '|', 'x2y2': '7', 'x3y2': '|', 'x4y2': '|',
                 'x0y3': '-', 'x1y3': 'L', 'x2y3': '-', 'x3y3': 'J', 'x4y3': '|',
                 'x0y4': 'L', 'x1y4': '|', 'x2y4': '-', 'x3y4': 'J', 'x4y4': 'F'}

        loop = day10.getMainLoop(pipes)
        self.assertEqual(len(loop), 8)

class PartTwo(unittest.TestCase):
    def test_hasOddCrosses(self):
        pipes = {'x0y0': '.', 'x1y0': '.', 'x2y0': '.', 'x3y0': '.', 'x4y0': '.', 'x5y0': '.', 'x6y0': '.', 'x7y0': '.', 'x8y0': '.', 'x9y0': '.', 'x10y0': '.',
                'x0y1': '.', 'x1y1': 'S', 'x2y1': '-', 'x3y1': '-', 'x4y1': '-', 'x5y1': '-', 'x6y1': '-', 'x7y1': '-', 'x8y1': '-', 'x9y1': '7', 'x10y1': '.',
                'x0y2': '.', 'x1y2': '|', 'x2y2': 'F', 'x3y2': '-', 'x4y2': '-', 'x5y2': '-', 'x6y2': '-', 'x7y2': '-', 'x8y2': '7', 'x9y2': '|', 'x10y2': '.',
                'x0y3': '.', 'x1y3': '|', 'x2y3': '|', 'x3y3': '.', 'x4y3': '.', 'x5y3': '.', 'x6y3': '.', 'x7y3': '.', 'x8y3': '|', 'x9y3': '|', 'x10y3': '.',
                'x0y4': '.', 'x1y4': '|', 'x2y4': '|', 'x3y4': '.', 'x4y4': '.', 'x5y4': '.', 'x6y4': '.', 'x7y4': '.', 'x8y4': '|', 'x9y4': '|', 'x10y4': '.',
                'x0y5': '.', 'x1y5': '|', 'x2y5': 'L', 'x3y5': '-', 'x4y5': '7', 'x5y5': '.', 'x6y5': 'F', 'x7y5': '-', 'x8y5': 'J', 'x9y5': '|', 'x10y5': '.',
                 'x0y6': '.', 'x1y6': '|', 'x2y6': '.', 'x3y6': '.', 'x4y6': '|', 'x5y6': '.', 'x6y6': '|', 'x7y6': '.', 'x8y6': '.', 'x9y6': '|', 'x10y6': '.',
                 'x0y7': '.', 'x1y7': 'L', 'x2y7': '-', 'x3y7': '-', 'x4y7': 'J', 'x5y7': '.', 'x6y7': 'L', 'x7y7': '-', 'x8y7': '-', 'x9y7': 'J', 'x10y7': '.',
                 'x0y8': '.', 'x1y8': '.', 'x2y8': '.', 'x3y8': '.', 'x4y8': '.', 'x5y8': '.', 'x6y8': '.', 'x7y8': '.', 'x8y8': '.', 'x9y8': '.', 'x10y8': '.'}
        tile = 'x0y0'
        is_internal = day10.hasOddCrosses(pipes, tile)
        self.assertFalse(is_internal)
        tile = 'x3y6'
        is_internal = day10.hasOddCrosses(pipes, tile)
        self.assertTrue(is_internal)

        pipes = {'x0y0': '.', 'x1y0': 'F', 'x2y0': '-', 'x3y0': '-', 'x4y0': '-', 'x5y0': '-', 'x6y0': '7', 'x7y0': 'F', 'x8y0': '7', 'x9y0': 'F', 'x10y0': '7', 
                 'x0y1': '.', 'x1y1': '|', 'x2y1': 'F', 'x3y1': '-', 'x4y1': '-', 'x5y1': '7', 'x6y1': '|', 'x7y1': '|', 'x8y1': '|', 'x9y1': '|', 'x10y1': '|',
                 'x0y2': '.', 'x1y2': '|', 'x2y2': '|', 'x3y2': '.', 'x4y2': 'F', 'x5y2': 'J', 'x6y2': '|', 'x7y2': '|', 'x8y2': '|', 'x9y2': '|', 'x10y2': '|',
                 'x0y3': 'F', 'x1y3': 'J', 'x2y3': 'L', 'x3y3': '7', 'x4y3': 'L', 'x5y3': '7', 'x6y3': 'L', 'x7y3': 'J', 'x8y3': 'L', 'x9y3': 'J', 'x10y3': '|',
                 'x0y4': 'L', 'x1y4': '-', 'x2y4': '-', 'x3y4': 'J', 'x4y4': '.', 'x5y4': 'L', 'x6y4': '7', 'x7y4': '.', 'x8y4': '.', 'x9y4': '.', 'x10y4': 'L',
                 'x0y5': '.', 'x1y5': '.', 'x2y5': '.', 'x3y5': '.', 'x4y5': 'F', 'x5y5': '-', 'x6y5': 'J', 'x7y5': '.', 'x8y5': '.', 'x9y5': 'F', 'x10y5': '7',
                 'x0y6': '.', 'x1y6': '.', 'x2y6': '.', 'x3y6': '.', 'x4y6': 'L', 'x5y6': '7', 'x6y6': '.', 'x7y6': 'F', 'x8y6': '7', 'x9y6': '|', 'x10y6': '|',
                 'x0y7': '.', 'x1y7': '.', 'x2y7': '.', 'x3y7': '.', 'x4y7': '.', 'x5y7': '|', 'x6y7': 'F', 'x7y7': 'J', 'x8y7': 'L', 'x9y7': 'J', 'x10y7': '|',
                 'x0y8': '.', 'x1y8': '.', 'x2y8': '.', 'x3y8': '.', 'x4y8': 'F', 'x5y8': 'J', 'x6y8': 'L', 'x7y8': '-', 'x8y8': '7', 'x9y8': '.', 'x10y8': '|'}
        tile = 'x7y4'
        is_internal = day10.hasOddCrosses(pipes, tile)
        self.assertTrue(is_internal)

    def test_countInternals(self):
        pipes = {'x0y0': '.', 'x1y0': '.', 'x2y0': '.', 'x3y0': '.', 'x4y0': '.', 'x5y0': '.', 'x6y0': '.', 'x7y0': '.', 'x8y0': '.', 'x9y0': '.', 'x10y0': '.',
                'x0y1': '.', 'x1y1': 'S', 'x2y1': '-', 'x3y1': '-', 'x4y1': '-', 'x5y1': '-', 'x6y1': '-', 'x7y1': '-', 'x8y1': '-', 'x9y1': '7', 'x10y1': '.',
                'x0y2': '.', 'x1y2': '|', 'x2y2': 'F', 'x3y2': '-', 'x4y2': '-', 'x5y2': '-', 'x6y2': '-', 'x7y2': '-', 'x8y2': '7', 'x9y2': '|', 'x10y2': '.',
                'x0y3': '.', 'x1y3': '|', 'x2y3': '|', 'x3y3': '.', 'x4y3': '.', 'x5y3': '.', 'x6y3': '.', 'x7y3': '.', 'x8y3': '|', 'x9y3': '|', 'x10y3': '.',
                'x0y4': '.', 'x1y4': '|', 'x2y4': '|', 'x3y4': '.', 'x4y4': '.', 'x5y4': '.', 'x6y4': '.', 'x7y4': '.', 'x8y4': '|', 'x9y4': '|', 'x10y4': '.',
                'x0y5': '.', 'x1y5': '|', 'x2y5': 'L', 'x3y5': '-', 'x4y5': '7', 'x5y5': '.', 'x6y5': 'F', 'x7y5': '-', 'x8y5': 'J', 'x9y5': '|', 'x10y5': '.',
                 'x0y6': '.', 'x1y6': '|', 'x2y6': '.', 'x3y6': '.', 'x4y6': '|', 'x5y6': '.', 'x6y6': '|', 'x7y6': '.', 'x8y6': '.', 'x9y6': '|', 'x10y6': '.',
                 'x0y7': '.', 'x1y7': 'L', 'x2y7': '-', 'x3y7': '-', 'x4y7': 'J', 'x5y7': '.', 'x6y7': 'L', 'x7y7': '-', 'x8y7': '-', 'x9y7': 'J', 'x10y7': '.',
                 'x0y8': '.', 'x1y8': '.', 'x2y8': '.', 'x3y8': '.', 'x4y8': '.', 'x5y8': '.', 'x6y8': '.', 'x7y8': '.', 'x8y8': '.', 'x9y8': '.', 'x10y8': '.'}
        internals = day10.countInternals(pipes)
        self.assertEqual(internals, 4)
