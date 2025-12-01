import unittest
from code import day03

class PartOne(unittest.TestCase):
    def test_buildSchematic(self):
        filename = 'inputs/testinput03.txt'
        schematic = day03.buildSchematic(filename)
        self.assertEqual(schematic[0][0], '4')
        self.assertEqual(schematic[1], '...*......')
        self.assertEqual(schematic[-1][-1], '.')

    def test_getNumbers(self):
        schematic = ['467..114..',
                     '...*......',
                     '..35..633.',
                     '......#...',
                     '617*......',
                     '.....+.58.',
                     '..592.....',
                     '......755.',
                     '...$.*....',
                     '.664.598..']
        numbers = day03.getNumbers(schematic)
        self.assertTrue('467' in numbers)
        self.assertEqual(len(numbers), 10)

    def test_getNumsToCheck(self):
        schematic = ['467..114..',
                     '...*......',
                     '..35..633.',
                     '......#...',
                     '617*......',
                     '.....+.58.',
                     '..592.....',
                     '......755.',
                     '...$.*....',
                     '.664.598..']
        row = 0
        num = '467'
        to_check = day03.getNumsToCheck(schematic, row, num)
        self.assertEqual(len(to_check), 12)
        self.assertTrue([1,0] in to_check)

        row = 0
        num = '114'
        to_check = day03.getNumsToCheck(schematic, row, num)
        self.assertTrue([1,7] in to_check)

        row = 9
        num = '598'
        to_check = day03.getNumsToCheck(schematic, row, num)
        self.assertTrue([8,5] in to_check)

    def test_hasSymbol(self):
        schematic = ['467..114..',
                     '...*......',
                     '..35..633.',
                     '......#...',
                     '617*......',
                     '.....+.58.',
                     '..592.....',
                     '......755.',
                     '...$.*....',
                     '.664.598..']
        locations = [[1,3]]
        self.assertTrue(day03.hasSymbol(schematic, locations))

    def test_getPartNumbers(self):
        schematic = ['467..114..',
                     '...*......',
                     '..35..633.',
                     '......#...',
                     '617*......',
                     '.....+.58.',
                     '..592.....',
                     '......755.',
                     '...$.*....',
                     '.664.598..']
        numbers = ['467', '114', '35', '633', '617', '58', '592', '755', '664', '598']
        partNumbers = day03.getPartNumbers(schematic, numbers)
        self.assertEqual(len(partNumbers), 8)

