import unittest
import day20

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.racetrack = ['###############',
                          '#...#...#.....#',
                          '#.#.#.#.#.###.#',
                          '#S#...#.#.#...#',
                          '#######.#.#.###',
                          '#######.#.#...#',
                          '#######.#.###.#',
                          '###..E#...#...#',
                          '###.#######.###',
                          '#...###...#...#',
                          '#.#####.#.###.#',
                          '#.#...#.#.#...#',
                          '#.#.#.#.#.#.###',
                          '#...#...#...###',
                          '###############']
    def test_getInput(self):
        filename = 'testinput20.txt'
        racetrack = day20.getInput(filename)
        expected = self.racetrack
        self.assertEqual(racetrack, expected)

    def test_getStart(self):
        racetrack = self.racetrack.copy()
        start = day20.getStart(racetrack)
        expected = [1,3]
        self.assertEqual(start, expected)

    def test_getNeighbors(self):
        location = [1,3]
        size = [15,15]
        neighbors = day20.getNeighbors(location, size)
        expected = [[1,2],[1,4],[0,3],[2,3]]
        for exp in expected:
            self.assertTrue(exp in neighbors)

    def test_runRace(self):
        racetrack = self.racetrack.copy()
        picoseconds = day20.runRace(racetrack)
        expected = 84
        self.assertEqual(picoseconds, expected)

    def test_cheat(self):
        racetrack = self.racetrack.copy()
        self.assertTrue(False)

