import unittest
import day16

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.maze1 = ['###############',
                        '#.......#....E#',
                        '#.#.###.#.###.#',
                        '#.....#.#...#.#',
                        '#.###.#####.#.#',
                        '#.#.#.......#.#',
                        '#.#.#####.###.#',
                        '#...........#.#',
                        '###.#.#####.#.#',
                        '#...#.....#.#.#',    
                        '#.#.#.###.#.#.#',
                        '#.....#...#.#.#',
                        '#.###.#.#.#.#.#',
                        '#S..#.....#...#',
                        '###############']

    def test_getInput(self):
        filename = 'testinput16.txt'
        maze = day16.getInput(filename)
        self.assertEqual(len(maze), 15)
        self.assertEqual(len(maze[0]), 15)
        self.assertEqual(maze[1][13], 'E')
        self.assertEqual(maze[13][1], 'S')

    def test_checkNeighbors(self):
        maze = self.maze1.copy()
        location = [1,13]
        options = day16.checkNeighbors(maze, location)
        expected = ['up', 'right']
        for exp in expected:
            self.assertTrue(exp in options)

    def test_move(self):
        location = [1,13]
        direction = 'right'
        new_loc = day16.move(location, direction)
        expected = [2,13]
        self.assertEqual(new_loc, expected)

        location = [1,13]
        direction = 'up'
        new_loc = day16.move(location, direction)
        expected = [1,12]
        self.assertEqual(new_loc, expected)

        location = [7,3]
        direction = 'left'
        new_loc = day16.move(location, direction)
        expected = [6,3]
        self.assertEqual(new_loc, expected)

        location = [11,5]
        direction = 'down'
        new_loc = day16.move(location, direction)
        expected = [11,6]
        self.assertEqual(new_loc, expected)

    def test_mapSection(self):
        maze = self.maze1.copy()
        location = [1,13]
        direction = 'right'
        section = day16.mapSection(maze, location, direction)
        exp_end = 'x3y13'
        exp_length = 2
        exp_options = 0
        self.assertTrue(exp_end in section)
        self.assertTrue(exp_length in section)
        self.assertTrue(exp_options in section)

        maze = self.maze1.copy()
        location = [1,13]
        direction = 'up'
        section = day16.mapSection(maze, location, direction)
        exp_end = 'x1y11'
        exp_length = 2
        exp_options = 2
        self.assertTrue(exp_end in section)
        self.assertTrue(exp_length in section)
        self.assertTrue(exp_options in section)

    def test_mapSections(self):
        maze = self.maze1.copy()
        start = [1,13]
        
        sections = day16.mapSections(maze, start)
        self.assertEqual(len(sections['start']), 2)
        self.assertTrue('x3y13' in sections['start'])
        self.assertTrue('x1y11' in sections['start'])
        self.assertEqual(len(sections['x1y11']), 2)
