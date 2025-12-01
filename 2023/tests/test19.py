import unittest
from code import day19

class PartOne(unittest.TestCase):
    def test_getInputs(self):
        filename = 'inputs/testinput19.txt'
        workflows, parts = day19.getInputs(filename)
        self.assertEqual(len(workflows), 11)
        self.assertTrue('pv' in workflows)
        self.assertEqual(len(workflows['rfg']), 3)
        self.assertEqual(len(parts), 5)
        self.assertEqual(parts[2]['x'], 2036)

    def test_flow(self):
        workflow = ['s<1351:px', 'qqz']
        part = {'x': 787, 'm': 2655, 'a': 1222, 's': 2876}
        next_flow = day19.flow(workflow, part)
        self.assertEqual(next_flow, 'qqz')
