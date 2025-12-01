import unittest
from code import day12

class PartOne(unittest.TestCase):
    def test_getDamagedRecord(self):
        filename = 'inputs/testinput12.txt'
        damaged_record = day12.getDamagedRecord(filename)
        self.assertEqual(len(damaged_record), 6)
        self.assertEqual(damaged_record[4][1], [1,6,5])

    def test_checkFit(self):
        possibility = '###?'
        check = 3
        fits = day12.checkFit(possibility, check)
        self.assertTrue(fits)

        possibility = '#?'
        check = 3
        fits = day12.checkFit(possibility, check)
        self.assertFalse(fits)

        possibility = '#.##.'
        check = 3
        fits = day12.checkFit(possibility, check)
        self.assertFalse(fits)

    def test_getNumArrangements(self): 
        springs = '###?'
        checksum = [3]
        num_arrangements = day12.getNumArrangements(springs, checksum)
        self.assertEqual(num_arrangements, 2)

        springs = '?##'
        checksum = [3]
        num_arrangements = day12.getNumArrangements(springs, checksum)
        self.assertEqual(num_arrangements, 1)
        
        springs = '???.###'
        checksum = [1,1,3]
        num_arrangements = day12.getNumArrangements(springs, checksum)
        self.assertEqual(num_arrangements, 1)

        springs = '###.###'
        checksum = [3]
        num_arrangements = day12.getNumArrangements(springs, checksum)
        self.assertEqual(num_arrangements, 0)

        springs = '??'
        checksum = [1]
        num_arrangements = day12.getNumArrangements(springs, checksum)
        self.assertEqual(num_arrangements, 2)

        springs = '.??..??...?##.'
        checksum = [1,1,3]
        num_arrangements = day12.getNumArrangements(springs, checksum)
        self.assertEqual(num_arrangements, 4)

        springs = '?#?#?#?#?#?#?#?'
        checksum = [1,3,1,6]
        num_arrangements = day12.getNumArrangements(springs, checksum)
        self.assertEqual(num_arrangements, 1)

        springs = '????.#...#...'
        checksum = [4,1,1]
        num_arrangements = day12.getNumArrangements(springs, checksum)
        self.assertEqual(num_arrangements, 1)

        springs = '????.######..#####.'
        checksum = [1,6,5]
        num_arrangements = day12.getNumArrangements(springs, checksum)
        self.assertEqual(num_arrangements, 4)

        springs = '?###????????'
        checksum = [3,2,1]
        num_arrangements = day12.getNumArrangements(springs, checksum)
        self.assertEqual(num_arrangements, 10)
