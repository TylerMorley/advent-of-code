import unittest
import day02

class PartOne(unittest.TestCase):
    def test_getInputs(self):
        filename = 'testinput02.txt'
        ranges = day02.getInputs(filename)

        self.assertEqual(len(ranges), 11)
        self.assertEqual(ranges[0], [11,22])

    def test_isValid(self):
        number = 12
        is_valid = day02.isValid(number)
        self.assertTrue(is_valid)

        number = 11
        is_valid = day02.isValid(number)
        self.assertFalse(is_valid)

        number = 101
        is_valid = day02.isValid(number)
        self.assertTrue(is_valid)

    def test_findInvalidIds(self):
        id_range = [11,22]
        num_invalid = day02.findInvalidIds(id_range)
        expected = [11,22]
        self.assertEqual(num_invalid, expected)
        
        id_range = [95,115]
        num_invalid = day02.findInvalidIds(id_range)
        expected = [99]
        self.assertEqual(num_invalid, expected)

    def test_sumInvalidIds(self):
        id_ranges = [[11, 22], [95, 115], [998, 1012], [1188511880, 1188511890], [222220, 222224], [1698522, 1698528], [446443, 446449], [38593856, 38593862], [565653, 565659], [824824821, 824824827], [2121212118, 2121212124]]
        invalid_sum = day02.sumInvalidIds(id_ranges)
        expected = 1227775554
        self.assertEqual(invalid_sum, expected)
        
        id_ranges = [[11, 22], [22,23]]
        invalid_sum = day02.sumInvalidIds(id_ranges)
        expected = 33
        self.assertEqual(invalid_sum, expected)

class PartTwo(unittest.TestCase):
    def test_checkSequence(self):
        sequence = '1'
        remainder = '1'
        is_invalid = day02.checkSequence(sequence, remainder)
        self.assertTrue(is_invalid)

        sequence = '1'
        remainder = '11'
        is_invalid = day02.checkSequence(sequence, remainder)
        self.assertTrue(is_invalid)

        
    def test_isValid2(self):
        number = 111
        is_valid = day02.isValid2(number)
        self.assertIsNotNone(is_valid)
        self.assertFalse(is_valid)

        number = 1112
        is_valid = day02.isValid2(number)
        self.assertIsNotNone(is_valid)
        self.assertTrue(is_valid)

        number = 12
        is_valid = day02.isValid2(number)
        self.assertIsNotNone(is_valid)
        self.assertTrue(is_valid)

    def test_findInvalidIds2(self):
        use_silly_patterns = True
        id_range = [11,22]
        num_invalid = day02.findInvalidIds(id_range, use_silly_patterns)
        expected = [11,22]
        self.assertEqual(num_invalid, expected)
        
        id_range = [95,115]
        num_invalid = day02.findInvalidIds(id_range, use_silly_patterns)
        expected = [99,111]
        self.assertEqual(num_invalid, expected)
        
    def test_sumInvalidIds2(self):
        use_silly_patterns = True
 
        id_ranges = [[11, 22], [95, 115], [998, 1012], [1188511880, 1188511890], [222220, 222224], [1698522, 1698528], [446443, 446449], [38593856, 38593862], [565653, 565659], [824824821, 824824827], [2121212118, 2121212124]]
        invalid_sum = day02.sumInvalidIds(id_ranges, use_silly_patterns)
        expected = 4174379265
        self.assertEqual(invalid_sum, expected)
