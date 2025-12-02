import unittest
import day12

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput12-1.txt'
        garden = day12.getInput(filename)
        expected = [['A','A','A','A'],
                    ['B','B','C','D'],
                    ['B','B','C','C'],
                    ['E','E','E','C']]
        self.assertEqual(garden, expected)

    def test_getNeighbors(self):
        location = [0,0]
        height = width = 5
        neighbors = day12.getNeighbors(location, height, width)
        expected = [[0,1],[1,0]]
        for e in expected:
            self.assertTrue(e in neighbors)

    def test_addPlot(self):
        record = dict()
        plot = ['A', [0,0]]
        record = day12.addPlot(record, plot)
        self.assertTrue(len(record), 1)
        self.assertEqual(record['A'], [[0,0]])

        record = {'A':[[0,0]]}
        plot = ['A', [0,1]]
        record = day12.addPlot(record, plot)
        self.assertEqual(len(record['A']), 2)
        self.assertTrue([0,1] in record['A'])

    def test_updatePerimeter(self):
        neighbors = [[0,0],[0,2],[1,1]]
        plots = [[0,0]]
        perimeter_change = day12.updatePerimeter(neighbors, plots)
        self.assertEqual(perimeter_change, 2)

        neighbors = [[0,1]]
        plots = []
        perimeter_change = day12.updatePerimeter(neighbors, plots)
        self.assertEqual(perimeter_change, 4)

    def test_updateRegion(self):
        garden = [['A','A','A','A'],
                    ['B','B','C','D'],
                    ['B','B','C','C'],
                    ['E','E','E','C']]
        location = [0,0]
        record = {'type':'A','plots':[], 'perimeter':0}
        garden, record, new_locations = day12.updateRegion(garden, record, location)
        self.assertTrue([0,0] in record['plots'])
        self.assertTrue([0,1] in new_locations)
        self.assertEqual(garden[0][0], '.')
        self.assertEqual(record['perimeter'], 4)

        location = [0,1]
        record = {'type':'A','plots':[[0,0]], 'perimeter':4}
        garden, record, new_locations = day12.updateRegion(garden, record, location)
        self.assertTrue([0,1] in record['plots'])
        self.assertTrue([0,2] in new_locations)
        self.assertEqual(garden[0][1], '.')
        self.assertEqual(record['perimeter'], 6)

    def test_findNewRegion(self):
        garden = [['A','A','A','A'],
                    ['B','B','C','D'],
                    ['B','B','C','C'],
                    ['E','E','E','C']]
        new_region = day12.findNewRegion(garden)
        expected = [0,0]
        self.assertEqual(new_region, expected)

        garden = [['.','.','.','.'],
                    ['.','.','.','.'],
                    ['.','.','.','.'],
                    ['.','.','.','.']]
        new_region = day12.findNewRegion(garden)
        expected = None
        self.assertEqual(new_region, expected)

    def test_mapRegion(self):
        garden = [['A','A','A','A'],
                    ['B','B','C','D'],
                    ['B','B','C','C'],
                    ['E','E','E','C']]
        start = [0,0]
        region = day12.mapRegion(garden, start)
        expected = {'type':'A','perimeter':10,'plots':[[0,0],[0,1],[0,2],[0,3]]}
        self.assertEqual(region['type'], expected['type'])
        self.assertEqual(region['perimeter'], expected['perimeter'])
        for plot in region['plots']:
            self.assertTrue(plot in expected['plots'])

        garden = [['.','.','.','.'],
                    ['B','B','C','D'],
                    ['B','B','C','C'],
                    ['E','E','E','C']]
        start = [1,0]
        region = day12.mapRegion(garden, start)
        expected = {'type':'B','perimeter':8,'plots':[[1,0],[1,1],[2,0],[2,1]]}
        self.assertEqual(region['type'], expected['type'])
        self.assertEqual(region['perimeter'], expected['perimeter'])
        for plot in region['plots']:
            self.assertTrue(plot in expected['plots'])

        garden = [['.','.','.','.'],
                    ['.','.','C','D'],
                    ['.','.','C','C'],
                    ['E','E','E','C']]
        start = [1,2]
        region = day12.mapRegion(garden, start)
        expected = {'type':'C','perimeter':10,'plots':[[1,2],[2,2],[2,3],[3,3]]}
        self.assertEqual(region['type'], expected['type'])
        self.assertEqual(region['perimeter'], expected['perimeter'])
        for plot in region['plots']:
            self.assertTrue(plot in expected['plots'])
        
        garden = [['A','A','A','A'],
                    ['A','B','C','D'],
                    ['B','B','C','C'],
                    ['E','E','E','C']]
        start = [0,0]
        region = day12.mapRegion(garden, start)
        expected = {'type':'A','perimeter':12,'plots':[[0,0],[0,1],[0,2],[0,3],[1,0]]}
        self.assertEqual(region['type'], expected['type'])
        self.assertEqual(region['perimeter'], expected['perimeter'])
        for plot in region['plots']:
            self.assertTrue(plot in expected['plots'])

    def test_calculateFencing(self):
        garden = [['A','A','A','A'],
                    ['B','B','C','D'],
                    ['B','B','C','C'],
                    ['E','E','E','C']]
        price = day12.calculateFencing(garden)
        expected = 140
        self.assertEqual(price, expected)

        garden = [['O','O','O','O','O'],
                    ['O','X','O','X','O'],
                    ['O','O','O','O','O'],
                    ['O','X','O','X','O'],
                    ['O','O','O','O','O']]
        price = day12.calculateFencing(garden)
        expected = 772
        self.assertEqual(price, expected)

        filename = 'testinput12-2.txt'
        garden = day12.getInput(filename)
        price = day12.calculateFencing(garden)
        expected = 1930
        self.assertEqual(price, expected)

class TestPartTwo(unittest.TestCase):
    def test_updatePerimeterBulk(self):
        self.assertTrue(False)
