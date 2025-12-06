import unittest
import day06

class PartOne(unittest.TestCase):
    def test_getInputs(self):
        problems = day06.getInputs('testinput06.txt')
        self.assertEqual(len(problems), 4)
        self.assertEqual(problems[0], [123, 45, 6, '*'])

    def test_solve(self):
        problem = [123,45,6,'*']
        solution = day06.solve(problem)
        expected = 33210
        self.assertEqual(solution, expected)

    def test_complete(self):
        worksheet = [[123, 45, 6, '*'],
                     [328, 64, 98, '+'],
                     [51, 387, 215, '*'],
                     [64, 23, 314, '+']]
        grand_total = day06.complete(worksheet)
        expected = 4277556
        self.assertEqual(grand_total, expected)
