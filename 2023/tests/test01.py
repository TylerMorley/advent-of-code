import unittest
from code import day01

class TestPartOne(unittest.TestCase):
    def test_getInputs(self):
        filename = 'inputs/testinput01.txt'
        inputs = day01.getInputs(filename)
        expected = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']

        self.assertEqual(inputs, expected)

    def test_getCalibrationValue(self):
        text_line = '1abc2'
        calibration_value = day01.getCalibrationValue(text_line)

        self.assertEqual(calibration_value, 12)

        text2 = 'pqr3stu8vwx'
        calibration_value = day01.getCalibrationValue(text2)

        self.assertEqual(calibration_value, 38)

        text3 = 'treb7uchet'
        calibration_value = day01.getCalibrationValue(text3)

        self.assertEqual(calibration_value, 77)

    def test_getSum(self):
        input = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
        sum = day01.getSum(input)

        self.assertEqual(sum, 142)

class TestPartTwo(unittest.TestCase):
    def test_replaceSpelledNums(self):
        input = 'two1nine'
        replaced = day01.replaceSpelledNums(input)
        self.assertEqual(replaced, '219')
