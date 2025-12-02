import unittest
import day13

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput13.txt'
        machines = day13.getInput(filename)
        self.assertEqual(len(machines), 4)
        self.assertEqual(machines[0]['Button A'], [94, 34])
        self.assertEqual(machines[1]['Button B'], [67, 21])
        self.assertEqual(machines[2]['Prize'], [7870, 6450])

    def test_calcTokens(self):
        machine = {'Button A': [94,34],
                   'Button B': [22,67],
                   'Prize': [8400,5400]}
        tokens = day13.calcTokens(machine)
        expected = [80,40]
        self.assertEqual(tokens, expected)

        machine = {'Button A': [26, 66],
                   'Button B': [67, 21],
                   'Prize': [12748, 12176]}
        tokens = day13.calcTokens(machine)
        expected = None
        self.assertEqual(tokens, expected)

    def test_playMachines(self):
        machines = [
                {'Button A': [94,34], 'Button B': [22,67], 'Prize': [8400,5400]},
                {'Button A': [26, 66],'Button B': [67, 21],'Prize': [12748, 12176]},
                {'Button A': [17, 86],'Button B': [84, 37],'Prize': [7870, 6450]},
                {'Button A': [69, 23],'Button B': [27, 71],'Prize': [18641, 10279]}
                ]
        tokens = day13.playMachines(machines)
        expected = 480
        self.assertEqual(tokens, expected)

class TestPartTwo(unittest.TestCase):
    def test_convert(self):
        machine = {'Button A': [94,34],
                   'Button B': [22,67],
                   'Prize': [8400,5400]}
        converted = day13.convert(machine)
        self.assertEqual(converted['Prize'], [10000000008400, 10000000005400])

    def test_playMachines_convert(self):
        machines = [
                {'Button A': [94,34], 'Button B': [22,67], 'Prize': [8400,5400]},
                {'Button A': [26, 66],'Button B': [67, 21],'Prize': [12748, 12176]},
                {'Button A': [17, 86],'Button B': [84, 37],'Prize': [7870, 6450]},
                {'Button A': [69, 23],'Button B': [27, 71],'Prize': [18641, 10279]}
                ]
        should_convert = True
        tokens = day13.playMachines(machines, should_convert)
        self.assertTrue(tokens > 480)


