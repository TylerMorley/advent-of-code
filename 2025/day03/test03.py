import unittest
import day03

class PartOne(unittest.TestCase):
    def test_getInputs(self):
        filename = 'testinput03.txt'
        banks = day03.getInputs(filename)
        self.assertEqual(len(banks), 4)

        exp_first = [9,8,7,6,5,4,3,2,1,1,1,1,1,1,1]
        self.assertEqual(banks[0], exp_first)

    def test_getLargestBatteries(self):
        bank = [9,8,7,6,5,4,3,2,1,1,1,1,1,1,1]
        largest = day03.getLargestBatteries(bank)
        expected = 98
        self.assertEqual(largest, expected)
        
        bank = [8,1,1,1,1,1,1,1,1,1,1,1,1,1,9]
        largest = day03.getLargestBatteries(bank)
        expected = 89
        self.assertEqual(largest, expected)

        bank = [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8]
        largest = day03.getLargestBatteries(bank)
        expected = 78
        self.assertEqual(largest, expected)

        bank = [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1]
        largest = day03.getLargestBatteries(bank)
        expected = 92
        self.assertEqual(largest, expected)

    def test_getTotalJoltage(self):
        banks = [[9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1],
                 [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
                 [2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8],
                 [8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1]]
        total_joltage = day03.getTotalJoltage(banks)
        expected = 357
        self.assertEqual(total_joltage, expected)
