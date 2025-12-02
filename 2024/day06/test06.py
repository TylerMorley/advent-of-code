import unittest
import day06

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.the_map = [['.','.','.','.','#','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.','.','#'],
                        ['.','.','.','.','.','.','.','.','.','.'],
                        ['.','.','#','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','#','.','.'],
                        ['.','.','.','.','.','.','.','.','.','.'],
                        ['.','#','.','.','^','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.','#','.'],
                        ['#','.','.','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','#','.','.','.']]
        self.start_loc = [6,4]
        
    def test_getInput(self):
        filename = 'testinput06.txt'
        lab_map = day06.getInput(filename)
        self.assertEqual(len(lab_map), 10)
        self.assertEqual(len(lab_map[0]), 10)
        self.assertEqual(lab_map, self.the_map)

    def test_rotate(self):
        unrotated  = self.the_map.copy()
        cur_loc = [6,4]
        rotated, new_loc = day06.rotate(unrotated, cur_loc)
        self.assertEqual(new_loc, [5,6])
        new_chevron = rotated[5][6]
        self.assertEqual(new_chevron, '^')
        self.assertEqual(type(rotated[0]), list)

        big = day06.getInput('input06.txt')
        rotated = big.copy()
        for i in range(4):
            rotated, loc = day06.rotate(rotated, [0,0])
        self.assertEqual(rotated, big)

    def test_moveToObstacle(self):
        cur_map, cur_location = day06.rotate(self.the_map.copy(), self.start_loc)
        new_map, new_location = day06.moveToObstacle(cur_map, cur_location)
        self.assertEqual(new_location, [5,1])
        path = new_map[5][1:7]
        for loc in path:
            self.assertEqual(loc, 'X')

        cur_map, cur_location = day06.rotate(new_map, new_location)
        new_map, new_location = day06.moveToObstacle(cur_map, cur_location)
        self.assertEqual(new_location, [8,1])
        path = new_map[8][1:5]
        for loc in path:
            self.assertEqual(loc, 'X')

        end_map = [['.','.','#','#'],
                   ['.','.','.','.'],
                   ['.','.','^','.'],
                   ['.','#','.','.']]
        end_loc = [2,2]
        end_map, end_loc = day06.moveToObstacle(end_map, end_loc)
        self.assertEqual(end_loc, [2,0])
        path = end_map[2][:3]
        for loc in path:
            self.assertEqual(loc, 'X')

        double_map = [['.','.','#','#'],
                      ['.','.','.','.'],
                      ['.','.','.','.'],
                      ['#','#','.','^']]
        location = [3,3]
        double_map, location = day06.moveToObstacle(double_map, location)
        self.assertEqual(location, [3,2])

        double_map = [['.','.','#','#','.'],
                      ['.','.','.','.','.'],
                      ['.','.','.','.','.'],
                      ['#','#','.','^','#']]
        location = [3,3]
        double_map, location = day06.moveToObstacle(double_map, location)
        self.assertEqual(location, [3,2])

    def test_getStartLocation(self):
        floormap = self.the_map.copy()
        start_location = day06.getStartLocation(floormap)
        expected = [6,4]
        self.assertEqual(start_location, expected)

    def test_countVisited(self):
        floormap = [['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '#'],
                    ['.', '.', '.', '.', 'X', '.', '.', '.', 'X', '.'],
                    ['.', '.', '#', '.', 'X', '.', '.', '.', 'X', '.'],
                    ['.', '.', 'X', 'X', 'X', 'X', 'X', '#', 'X', '.'],
                    ['.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'],
                    ['.', '#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '#', '.'],
                    ['#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', 'X', '.', '.']]
        visited = day06.countVisited(floormap)
        expected = 41
        self.assertEqual(visited, expected)

    def test_predictGuard(self):
        floormap = self.the_map.copy()
        pos_visited = day06.predictGuard(floormap)
        expected = 41
        self.assertEqual(pos_visited, expected)

        corner_map = [['.','#','.'],
                      ['.','.','#'],
                      ['.','^','.']]
        pos_visited = day06.predictGuard(corner_map)
        expected = 2
        self.assertEqual(pos_visited, expected)

class TestPartTwo(unittest.TestCase):
    def setUp(self):
        self.the_map = [['.','.','.','.','#','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.','.','#'],
                        ['.','.','.','.','.','.','.','.','.','.'],
                        ['.','.','#','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','#','.','.'],
                        ['.','.','.','.','.','.','.','.','.','.'],
                        ['.','#','.','.','^','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.','#','.'],
                        ['#','.','.','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','#','.','.','.']]
        self.start_loc = [6,4]
        
    def test_predictGuard_infinite(self):
        infinite_map = self.the_map.copy()
        infinite_map[6][3] = '#'
        result = day06.predictGuard(infinite_map)
        self.assertEqual(result, None)

    def test_predictGuard_locs(self):
        loc_map = self.the_map.copy()
        get_locs = True
        locs = day06.predictGuard(loc_map, get_locs)
        self.assertEqual(len(locs), 41)
        expected = [[1,4],[1,8],[2,4],[3,8],[4,2]]
        for exp in expected:
            self.assertTrue(exp in locs)

    def test_getVisited(self):
        floormap = [['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '#'],
                    ['.', '.', '.', '.', 'X', '.', '.', '.', 'X', '.'],
                    ['.', '.', '#', '.', 'X', '.', '.', '.', 'X', '.'],
                    ['.', '.', 'X', 'X', 'X', 'X', 'X', '#', 'X', '.'],
                    ['.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'],
                    ['.', '#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
                    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '#', '.'],
                    ['#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', 'X', '.', '.']]
        visited = day06.getVisited(floormap)
        expected = 41
        self.assertEqual(len(visited), expected)

    def test_tryObstacles(self):
        obstacle_map = self.the_map.copy()
        possible_obstacles = day06.tryObstacles(obstacle_map)
        expected = [[6,3],[7,6],[7,7],[8,1],[8,3],[9,7]]
        for ob in expected:
            self.assertTrue(ob in possible_obstacles)
        self.assertEqual(len(possible_obstacles), 6)
