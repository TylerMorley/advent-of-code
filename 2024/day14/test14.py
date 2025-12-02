import unittest
import day14

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput14.txt'
        robots = day14.getInput(filename)
        self.assertEqual(len(robots), 12)
        self.assertEqual(robots[0][0], [0,4])

    def test_moveRobot(self):
        robot = [[2, 4], [2, -3]]
        room = [11,7]
        seconds = 5
        position = day14.moveRobot(robot, room, seconds)
        expected_loc = [1,3]
        self.assertEqual(position, expected_loc)

        robot = [[0, 4], [3, -3]]
        room = [11,7]
        seconds = 100
        position = day14.moveRobot(robot, room, seconds)
        expected_loc = [3,5]
        self.assertEqual(position, expected_loc)

    def test_moveRobots(self):
        robots = [[[0, 4], [3, -3]],
                    [[6, 3], [-1, -3]],
                    [[10, 3], [-1, 2]],
                    [[2, 0], [2, -1]],
                    [[0, 0], [1, 3]],
                    [[3, 0], [-2, -2]],
                    [[7, 6], [-1, -3]],
                    [[3, 0], [-1, -2]],
                    [[9, 3], [2, 3]],
                    [[7, 3], [-1, 2]],
                    [[2, 4], [2, -3]],
                    [[9, 5], [-3, -3]]]
        room = [11,7]
        seconds = 100
        positions = day14.moveRobots(robots, room, seconds)
        self.assertTrue([3,5] in positions)

    def test_getSafetyFactor(self):
        positions = [[3, 5], [5, 4], [9, 0], [4, 5], [1, 6], [1, 3], [6, 0], [2, 3], [0, 2], [6, 0], [4, 5], [6, 6]]
        room = [11,7]
        safety_factor = day14.getSafetyFactor(positions, room)
        expected = 12
        self.assertEqual(safety_factor, expected)

class TestPartTwo(unittest.TestCase):
    def test_checkForImage(self):
        positions = [[3, 5], [5, 4], [9, 0], [4, 5], [1, 6], [1, 3], [6, 0], [2, 3], [0, 2], [6, 0], [4, 5], [6, 6]]
        is_candidate = day14.checkForImage(20, 20, positions)
        self.assertFalse(is_candidate)

        positions = [[3,5], [4,4],[4,5],[4,6],[5,5]]
        is_candidate = day14.checkForImage(20, 20, positions)
        self.assertTrue(is_candidate)


