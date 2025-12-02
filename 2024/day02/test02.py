import unittest
import day02

class TestPartOne(unittest.TestCase):
    def test_getInputs(self):
        filename = 'testinput02.txt'
        data = day02.getInputs(filename)
        expected = [[7, 6, 4, 2, 1],
                    [1, 2, 7, 8, 9],
                    [9, 7, 6, 2, 1],
                    [1, 3, 2, 4, 5],
                    [8, 6, 4, 4, 1],
                    [1, 3, 6, 7, 9]]

        self.assertEqual(data, expected)

    def test_compareLevels(self):
        levels = [7, 6]
        difference = day02.compareLevels(levels)
        expected = ['decreasing', 1]
        self.assertEqual(difference, expected)

        levels = [2, 7]
        difference = day02.compareLevels(levels)
        expected = ['increasing', 5]
        self.assertEqual(difference, expected)

    def test_checkReportSafety(self):
        report = [7, 6, 4, 2, 1]
        is_safe, i = day02.checkReportSafety(report)
        self.assertTrue(is_safe)

        report = [1, 2, 7, 8, 9]
        is_safe, i = day02.checkReportSafety(report)
        expected_index = 1
        self.assertFalse(is_safe)
        self.assertEqual(i, expected_index) 
        
    def test_countSafeReports(self):
        reports = [[7, 6, 4, 2, 1],
                    [1, 2, 7, 8, 9],
                    [9, 7, 6, 2, 1],
                    [1, 3, 2, 4, 5],
                    [8, 6, 4, 4, 1],
                    [1, 3, 6, 7, 9]]
        num_safe_reports = day02.countSafeReports(reports)
        expected = 2
        self.assertEqual(num_safe_reports, expected)

class TestPartTwo(unittest.TestCase):
    def test_countSafeReports_dampened(self):
        dampened = True
        reports = [[7, 6, 4, 2, 1],
                    [1, 2, 7, 8, 9],
                    [9, 7, 6, 2, 1],
                    [1, 3, 2, 4, 5],
                    [8, 6, 4, 4, 1],
                    [1, 3, 6, 7, 9]]
        num_safe_reports = day02.countSafeReports(reports, dampened)
        expected = 4
        self.assertEqual(num_safe_reports, expected)
        
        reports = [[1, 7, 2, 3, 4],
                    [48, 46, 47, 49, 51, 54, 56],
                    [1, 1, 2, 3, 4, 5],
                    [1, 2, 3, 4, 5, 5],
                    [5, 1, 2, 3, 4, 5],
                    [1, 4, 3, 2, 1],
                    [1, 6, 7, 8, 9],
                    [1, 2, 3, 4, 3],
                    [9, 8, 7, 6, 7],
                    [7, 10, 8, 10, 11],
                    [29, 28, 27, 25, 26, 25, 22, 20]]
        num_safe_reports = day02.countSafeReports(reports, dampened)
        expected = 11
        self.assertEqual(num_safe_reports, expected)

    def test_checkDampenedSafety(self):
        reports = [[1, 7, 2, 3, 4],
                    [48, 46, 47, 49, 51, 54, 56],
                    [1, 1, 2, 3, 4, 5],
                    [1, 2, 3, 4, 5, 5],
                    [5, 1, 2, 3, 4, 5],
                    [1, 4, 3, 2, 1],
                    [1, 6, 7, 8, 9],
                    [1, 2, 3, 4, 3],
                    [9, 8, 7, 6, 7],
                    [7, 10, 8, 10, 11],
                    [29, 28, 27, 25, 26, 25, 22, 20]]
        for report in reports:
            is_safe, i = day02.checkReportSafety(report)
            is_dampened_safe = day02.checkDampenedSafety(report, i)
            self.assertTrue(is_dampened_safe)
