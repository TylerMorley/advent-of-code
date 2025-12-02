import unittest
import day19

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.patterns = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
        self.designs = ['brwrr',
                        'bggr',
                        'gbbr',
                        'rrbgbr',
                        'ubwu',
                        'bwurrg',
                        'brgr',
                        'bbrgwb']
        
    def test_getInput(self):
        filename = 'testinput19.txt'
        patterns, designs = day19.getInput(filename)
        self.assertEqual(patterns, self.patterns)
        self.assertEqual(designs, self.designs)

    def test_buildDesign(self):
        patterns = self.patterns.copy()
        design = 'brwrr'
        record = dict()
        num_builds = day19.buildDesign(patterns, design, record)
        self.assertTrue(num_builds > 0)
        self.assertTrue('r' in record)
        self.assertTrue('wrr' in record)

        design = 'bggr'
        record = dict()
        num_builds = day19.buildDesign(patterns, design, record)
        self.assertTrue(num_builds > 0)

        design = 'gbbr'
        record = dict()
        num_builds = day19.buildDesign(patterns, design, record)
        self.assertTrue(num_builds > 0)

        design = 'rrbgbr'
        record = dict()
        num_builds = day19.buildDesign(patterns, design, record)
        self.assertTrue(num_builds > 0)

        design = 'ubwu'
        record = dict()
        num_builds = day19.buildDesign(patterns, design, record)
        self.assertFalse(num_builds > 0)

    def test_findPossible(self):
        patterns = self.patterns.copy()
        designs = self.designs.copy()
        num_possible = day19.findPossible(patterns, designs)
        expected = 6
        self.assertEqual(num_possible, expected)

class TestPartTwo(unittest.TestCase):
    def setUp(self):
        self.patterns = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
        self.designs = ['brwrr',
                        'bggr',
                        'gbbr',
                        'rrbgbr',
                        'ubwu',
                        'bwurrg',
                        'brgr',
                        'bbrgwb']
        
    def test_buildDesign_all(self):
        patterns = self.patterns.copy()
        count_all = True
        design = 'brwrr'
        num_buildable = day19.buildDesign(patterns, design, dict(), count_all)
        self.assertEqual(num_buildable, 2)

        count_all = True
        design = 'rrbgbr'
        num_buildable = day19.buildDesign(patterns, design, dict(), count_all)
        self.assertEqual(num_buildable, 6)

    def test_findPossible_all(self):
        patterns = self.patterns.copy()
        designs = self.designs.copy()
        count_all = True
        num_possible = day19.findPossible(patterns, designs, count_all)
        expected = 16
        self.assertEqual(num_possible, expected)

        
