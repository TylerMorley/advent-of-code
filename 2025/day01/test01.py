import unittest
import day01

class PartOne(unittest.TestCase):
    def test_getInputs(self):
        filename = 'testinput01.txt'
        rotations = day01.getInputs(filename)
        self.assertEqual(len(rotations), 10)

        expected = [['L',68], ['L',30], ['R',48], ['L',5], ['R',60], ['L',55], ['L',1], ['L',99], ['R',14], ['L',82]]
        self.assertEqual(rotations, expected)

    def test_turn(self):
        start = 50
        rotation = ['R',1]
        arrow, crossed = day01.turn(start, rotation)
        self.assertEqual(arrow, 51)
        self.assertIsNone(crossed)

        start = 50
        rotation = ['L', 1]
        arrow, crossed = day01.turn(start, rotation)
        self.assertEqual(arrow, 49)

        start = 99
        rotation = ['R', 1]
        arrow, crossed = day01.turn(start, rotation)
        self.assertEqual(arrow, 0)

        start = 0
        rotation = ['L', 1]
        arrow, crossed = day01.turn(start, rotation)
        self.assertEqual(arrow, 99)

    def test_getPassword(self):
        rotations = [['L',68], ['L',30], ['R',48], ['L',5], ['R',60], ['L',55], ['L',1], ['L',99], ['R',14], ['L',82]]
        start = 50
        password = day01.getPassword(start, rotations)

        self.assertEqual(password, 3)

class PartTwo(unittest.TestCase):
    def test_turn2(self):
        start = 50
        rotation = ['L',68]
        use_method = True
        arrow, crossed_zero = day01.turn(start, rotation, use_method)
        self.assertEqual(arrow, 82)
        self.assertEqual(crossed_zero, 1)

        start = 82
        rotation = ['L',30]
        arrow,crossed_zero = day01.turn(start, rotation, use_method)
        self.assertEqual(arrow, 52)
        self.assertEqual(crossed_zero, 0)
        
        start = 52
        rotation = ['R',48]
        arrow,crossed_zero = day01.turn(start, rotation, use_method)
        self.assertEqual(arrow, 0)
        self.assertEqual(crossed_zero, 1)

        start = 0
        rotation = ['L',5]
        arrow, crossed_zero = day01.turn(start, rotation, use_method)
        self.assertEqual(arrow, 95)
        self.assertEqual(crossed_zero, 0)

        start = 95
        rotation = ['R',60]
        arrow,crossed_zero = day01.turn(start, rotation, use_method)
        self.assertEqual(arrow, 55)
        self.assertEqual(crossed_zero, 1)

        start = 55
        rotation = ['L',55]
        arrow,crossed_zero = day01.turn(start, rotation, use_method)
        self.assertEqual(arrow, 0)
        self.assertEqual(crossed_zero, 1)

        start = 0
        rotation = ['L',1]
        arrow,crossed_zero = day01.turn(start, rotation, use_method)
        self.assertEqual(arrow, 99)
        self.assertEqual(crossed_zero, 0)

        rotations = [['L',68], ['L',30], ['R',48], ['L',5], ['R',60], ['L',55], ['L',1], ['L',99], ['R',14], ['L',82]]
        expected = [[82,1], [52,0], [0,1], [95,0], [55,1], [0,1], [99,0], [0,1], [14,0], [32,1]]
        arrow = 50
        for i in range(len(rotations)):
            arrow, crossed_zero = day01.turn(arrow, rotations[i], True)
            self.assertEqual(arrow, expected[i][0])
            self.assertEqual(crossed_zero, expected[i][1])

    def test_turn2_stop_at_zero(self):
        arrow = 99
        rotations = [['R',1], ['R',1]]
        expected = [[0,1], [1,0]]
        for i in range(len(rotations)):
            exp_arrow, exp_crossed_zero = expected[i]
            arrow, crossed_zero = day01.turn(arrow, rotations[i], True)
            self.assertEqual(arrow, exp_arrow)
            self.assertEqual(crossed_zero, exp_crossed_zero)

        arrow = 1
        rotations = [['L',1], ['L',1]]
        expected = [[0,1], [99,0]]
        for i in range(len(rotations)):
            exp_arrow, exp_crossed_zero = expected[i]
            arrow, crossed_zero = day01.turn(arrow, rotations[i], True)
            self.assertEqual(arrow, exp_arrow)
            self.assertEqual(crossed_zero, exp_crossed_zero)

        arrow = 1
        rotations = [['L',1], ['R',1]]
        expected = [[0,1], [1,0]]
        for i in range(len(rotations)):
            exp_arrow, exp_crossed_zero = expected[i]
            arrow, crossed_zero = day01.turn(arrow, rotations[i], True)
            self.assertEqual(arrow, exp_arrow)
            self.assertEqual(crossed_zero, exp_crossed_zero)
        
        arrow = 99
        rotations = [['R',1], ['L',1]]
        expected = [[0,1], [99,0]]
        for i in range(len(rotations)):
            exp_arrow, exp_crossed_zero = expected[i]
            arrow, crossed_zero = day01.turn(arrow, rotations[i], True)
            self.assertEqual(arrow, exp_arrow)
            self.assertEqual(crossed_zero, exp_crossed_zero)

    def test_getPassword2(self):
        rotations = [['L',68], ['L',30], ['R',48], ['L',5], ['R',60], ['L',55], ['L',1], ['L',99], ['R',14], ['L',82]]
        start = 50
        use_method = True
        password = day01.getPassword(start, rotations, use_method)

        self.assertEqual(password, 6)
        
