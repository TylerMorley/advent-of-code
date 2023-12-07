import unittest
from code import day06

class PartOne(unittest.TestCase):
    def test_getRaces(self):
        filename = 'inputs/testinput06.txt'
        races = day06.getRaces(filename)
        self.assertEqual(len(races), 3)
        self.assertEqual(races[2][1], 200)

    def test_runRace(self):
        race = [7, 9]
        outcome = day06.runRace(race)
        self.assertEqual(outcome, 4)
        race = [15, 40]
        outcome = day06.runRace(race)
        self.assertEqual(outcome, 8)
        race = [30, 200]
        outcome = day06.runRace(race)
        self.assertEqual(outcome, 9)

    def test_runRaces(self):
        races = [[7,9],[15,40],[30,200]]
        margin_of_error = day06.runRaces(races)
        self.assertEqual(margin_of_error, 288)

class PartTwo(unittest.TestCase):
    def test_getRace2(self):
        filename = 'inputs/testinput06.txt'
        race = day06.getRace2(filename)
        self.assertEqual(race[0], 71530)
        self.assertEqual(race[1], 940200)
