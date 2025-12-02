import unittest
import day10

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput10-1.txt'
        top_map = day10.getInput(filename)
        expected = ['0123', '1234', '8765', '9876']
        self.assertEqual(top_map, expected)

    def test_findTrailheads(self):
        top_map = ['0123', '1234', '8765', '9876']
        trailheads = day10.findTrailheads(top_map)
        expected = [[0,0]]
        self.assertEqual(trailheads, expected)

        top_map = ['...0...', '...1...', '...2...', '6543456', '7.....7', '8.....8', '9.....9']
        trailheads = day10.findTrailheads(top_map)
        expected = [[0,3]]
        self.assertEqual(trailheads, expected)

    def test_getAdjacent(self):
        height, width = [4,4]
        location = [1,1]
        neighbors = day10.getAdjacent(height, width, location)
        expected = [[0,1],[1,0],[1,2],[2,1]]
        for loc in expected:
            self.assertTrue(loc in neighbors)

    def test_countCompleteTrails(self):
        top_map = ['...0...',
                   '...1...',
                   '...2...',
                   '6543456',
                   '7.....7',
                   '8.....8',
                   '9.....9']
        trailhead = [0,3]
        complete_trails = day10.countCompleteTrails(top_map, trailhead)
        expected = 2
        self.assertEqual(len(complete_trails), expected)

        top_map = ['0123', '1234', '8765', '9876']
        trailhead = [0,0]
        complete_trails2 = day10.countCompleteTrails(top_map, trailhead)
        expected = 1
        self.assertEqual(len(complete_trails2), expected)

    def test_getMapScore(self):
        top_map = ['89010123',
                   '78121874',
                   '87430965',
                   '96549874',
                   '45678903',
                   '32019012',
                   '01329801',
                   '10456732']
        map_score = day10.getMapScore(top_map)
        expected = 36
        self.assertEqual(map_score, expected)

class TestPartTwo(unittest.TestCase):
    def test_getMapScore_distinct(self):
        top_map = ['89010123',
                   '78121874',
                   '87430965',
                   '96549874',
                   '45678903',
                   '32019012',
                   '01329801',
                   '10456732']
        count_distinct = True
        map_score = day10.getMapScore(top_map, count_distinct)
        expected = 81
        self.assertEqual(map_score, expected)
        
    def test_countCompleteTrails_distinct(self):
        top_map = ['.....0.',
                   '..4321.',
                   '..5..2.',
                   '..6543.',
                   '..7..4.',
                   '..8765.',
                   '..9....']
        trailhead = [0,5]
        count_distinct = True
        complete_trails = day10.countCompleteTrails(top_map, trailhead, count_distinct)
        expected = 3
        self.assertEqual(len(complete_trails), expected)

