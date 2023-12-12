import unittest
from code import day02

class PartOne(unittest.TestCase):
    def test_buildRecord(self):
        filename = 'inputs/testinput02.txt'
        record = day02.buildRecord(filename)
        self.assertTrue('Game 1' in record)
        self.assertTrue('Game 2' in record)
        self.assertTrue(len(record['Game 1']) == 3)
        self.assertTrue([['green', 2]] in record['Game 1'])

    def test_checkPossibility(self):
        bag = {'red': 12, 'green': 13, 'blue': 14}

        game = [[['blue', 3], ['red', 4]], 
                [['red', 1], ['green', 2], ['blue', 6]], 
                [['green', 2]]
                ]
        isPossible = day02.checkPossibility(game, bag)
        self.assertTrue(isPossible)

        game = [[['blue', 1], ['green', 2]],
                [['green', 3], ['blue', 4], ['red', 1]],
                [['green', 1], ['blue', 1]]]
        isPossible = day02.checkPossibility(game, bag)
        self.assertTrue(isPossible)

        game = [[['green', 8], ['blue', 6], ['red', 20]],
                [['blue', 5], ['red', 4], ['green', 13]],
                [['green', 5], ['red', 1]]]
        isPossible = day02.checkPossibility(game, bag)
        self.assertFalse(isPossible)

        game = [[['green', 1], ['red', 3], ['blue', 6]],
                [['green', 3], ['red', 6]],
                [['green', 3], ['blue', 15], ['red', 14]]]
        isPossible = day02.checkPossibility(game, bag)
        self.assertFalse(isPossible)

        game = [[['red', 6], ['blue', 1], ['green', 3]],
                [['blue', 2], ['red', 1], ['green', 2]]]
        isPossible = day02.checkPossibility(game, bag)
        self.assertTrue(isPossible)

    def test_getScore(self):
        games = {'Game 1': [[['blue', 3], ['red', 4]], 
                            [['red', 1], ['green', 2], ['blue', 6]], 
                            [['green', 2]]],
                'Game 2': [[['blue', 1], ['green', 2]],
                            [['green', 3], ['blue', 4], ['red', 1]],
                            [['green', 1], ['blue', 1]]],
                'Game 3': [[['green', 8], ['blue', 6], ['red', 20]],
                            [['blue', 5], ['red', 4], ['green', 13]],
                            [['green', 5], ['red', 1]]],
                'Game 4': [[['green', 1], ['red', 3], ['blue', 6]],
                            [['green', 3], ['red', 6]],
                            [['green', 3], ['blue', 15], ['red', 14]]],
                'Game 5': [[['red', 6], ['blue', 1], ['green', 3]],
                            [['blue', 2], ['red', 1], ['green', 2]]]
                }
        bag = {'red': 12, 'green': 13, 'blue': 14}
        score = day02.getScore(games, bag)
        self.assertEqual(score, 8)

class PartTwo(unittest.TestCase):
    def test_getPower(self):
        game = [[['blue', 3], ['red', 4]], 
                [['red', 1], ['green', 2], ['blue', 6]], 
                [['green', 2]]
                ]
        power = day02.getPower(game)
        self.assertEqual(power, 48)
        
        game = [[['blue', 1], ['green', 2]],
                [['green', 3], ['blue', 4], ['red', 1]],
                [['green', 1], ['blue', 1]]]
        power = day02.getPower(game)
        self.assertEqual(power, 12)

        game = [[['green', 8], ['blue', 6], ['red', 20]],
                [['blue', 5], ['red', 4], ['green', 13]],
                [['green', 5], ['red', 1]]]
        power = day02.getPower(game)
        self.assertEqual(power, 1560)
       
        game = [[['green', 1], ['red', 3], ['blue', 6]],
                [['green', 3], ['red', 6]],
                [['green', 3], ['blue', 15], ['red', 14]]]
        power = day02.getPower(game)
        self.assertEqual(power, 630)

        game = [[['red', 6], ['blue', 1], ['green', 3]],
                [['blue', 2], ['red', 1], ['green', 2]]]
        power = day02.getPower(game)
        self.assertEqual(power, 36)

