import unittest
from code import day13

class PartOne(unittest.TestCase):
    def test_getPatterns(self):
        filename = 'inputs/testinput13.txt'
        patterns = day13.getPatterns(filename)
        self.assertEqual(len(patterns), 2)
        self.assertEqual(len(patterns[0]), 7)
        self.assertEqual(len(patterns[0][0]), 9)

    def test_findRefptCandidates(self):
        pattern = ['#.##..##.',
                   '..#.##.#.',
                   '##......#',
                   '##......#',
                   '..#.##.#.',
                   '..##..##.',
                   '#.#.##.#.'
                   ]
        candidates = day13.findRefptCandidates(pattern)
        self.assertEqual(len(candidates), 1)
