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
        end = 'out'
        paths = day11.getPaths(racks, start, end)
        self.assertEqual(paths, 5)

class PartTwo(unittest.TestCase):
    def test_getPathsQuick(self):
        racks = {'aaa': ['you', 'hhh'], 'you': ['bbb', 'ccc'], 'bbb': ['ddd', 'eee'],
                 'ccc': ['ddd', 'eee', 'fff'], 'ddd': ['ggg'], 'eee': ['out'],
                 'fff': ['out'], 'ggg': ['out'], 'hhh': ['ccc', 'fff', 'iii'],
                 'iii': ['out']} 
        start = 'you'
        end = 'out'
        mem = dict()
        paths = day11.getPathsQuick(racks, start, end, mem)
        self.assertEqual(paths, 5)

        racks = {'svr': ['aaa', 'bbb'], 'aaa': ['fft'], 'fft': ['ccc'],
                 'bbb': ['tty'], 'tty': ['ccc'], 'ccc': ['ddd', 'eee'],
                 'ddd': ['hub'], 'hub': ['fff'], 'eee': ['dac'], 'dac': ['fff'],
                 'fff': ['ggg', 'hhh'], 'ggg': ['out'], 'hhh': ['out']}
        start = 'fft'
        end = 'dac'
        mem = dict()
        paths = day11.getPathsQuick(racks, start, end, mem)
        self.assertEqual(paths, 1)

    def test_getPathsDF(self):
        racks = {'svr': ['aaa', 'bbb'], 'aaa': ['fft'], 'fft': ['ccc'],
                 'bbb': ['tty'], 'tty': ['ccc'], 'ccc': ['ddd', 'eee'],
                 'ddd': ['hub'], 'hub': ['fff'], 'eee': ['dac'], 'dac': ['fff'],
                 'fff': ['ggg', 'hhh'], 'ggg': ['out'], 'hhh': ['out']}
        paths = day11.getPathsDF(racks)
        self.assertEqual(paths, 2)
