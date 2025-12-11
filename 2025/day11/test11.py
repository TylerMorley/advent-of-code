import unittest
import day11

class PartOne(unittest.TestCase):
    def test_getInputs(self):
        server_rack = day11.getInputs('testinput11.txt')
        self.assertEqual(len(server_rack), 10)
        self.assertEqual(server_rack['aaa'], ['you','hhh'])

    def test_getPaths(self):
        racks = {'aaa': ['you', 'hhh'], 'you': ['bbb', 'ccc'], 'bbb': ['ddd', 'eee'],
                 'ccc': ['ddd', 'eee', 'fff'], 'ddd': ['ggg'], 'eee': ['out'],
                 'fff': ['out'], 'ggg': ['out'], 'hhh': ['ccc', 'fff', 'iii'],
                 'iii': ['out']} 
        start = 'you'
        paths = day11.getPaths(racks, start)
        self.assertEqual(paths, 5)
