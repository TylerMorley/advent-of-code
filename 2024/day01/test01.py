import unittest
from day01 import day01

class TestPartOne(unittest.TestCase):
    def test_getInputs(self):
        filename = 'day01/testinput01.txt'
        lists = day01.getInputs(filename)
        expected = [[3,4,2,1,3,3],[4,3,5,3,9,3]]
        
        self.assertEqual(lists, expected)

    def test_getTotalDistance(self):
        locations = [[3,4,2,1,3,3], [4,3,5,3,9,3]]
        total_distance = day01.getTotalDistance(locations)
        expected = 11
        self.assertEqual(total_distance, expected)

class TestPartTwo(unittest.TestCase):
    def test_getSimilarityScore(self):
        lists = [[3,4,2,1,3,3],[4,3,5,3,9,3]]
        score = day01.getSimilarityScore(lists)
        expected = 31
        self.assertEqual(score, expected)
