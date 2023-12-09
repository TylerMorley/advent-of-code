import unittest
from code import day09

class PartOne(unittest.TestCase):
    def test_getAnalysis(self):
        filename = 'inputs/testinput09.txt'
        analysis = day09.getAnalysis(filename)
        self.assertEqual(len(analysis), 3)
        self.assertEqual(analysis[-1][-1], 45)

    def test_getDifferences(self):
        line = [0, 3, 6, 9, 12, 15]
        diffs = day09.getDifferences(line)
        self.assertEqual(len(diffs), 5)
        self.assertEqual(diffs[2], 3)

    def test_getAllDifferences(self):
        line = [0, 3, 6, 9, 12, 15]
        all_diffs = day09.getAllDifferences(line)
        self.assertEqual(len(all_diffs), 3)
        self.assertEqual(all_diffs[1][4], 3)

    def test_extrapolate(self):
        report = [[0, 3, 6, 9, 12, 15],
                  [3, 3, 3, 3, 3],
                  [0, 0, 0, 0]
                  ]
        next_value = day09.extrapolate(report)
        self.assertEqual(next_value, 18)

    def test_getExtrValues(self):
        analysis = [[0, 3, 6, 9, 12, 15],
                    [1, 3, 6, 10, 15, 21],
                    [10, 13, 16, 21, 30, 45]
                    ]
        sum_extr_values = day09.getExtrValues(analysis)
        self.assertEqual(sum_extr_values, 114)

class PartTwo(unittest.TestCase):
    def test_extrapolateBwd(self):
        report = [[10, 13, 16, 21, 30, 45],
                  [3, 3, 5, 9, 15],
                  [0, 2, 4, 6],
                  [2, 2, 2],
                  [0, 0]
                  ]
        next_value = day09.extrapolateBwd(report)
        self.assertEqual(next_value, 5)

    def test_getExtrValues2(self):
        analysis = [[0, 3, 6, 9, 12, 15],
                  [1, 3, 6, 10, 15, 21],
                  [10, 13, 16, 21, 30, 45]
                  ]
        sum_extr_values = day09.getExtrValues(analysis, True)
        self.assertEqual(sum_extr_values, 2)
