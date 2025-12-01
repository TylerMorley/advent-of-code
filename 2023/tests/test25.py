import unittest
from code import day25

class PartOne(unittest.TestCase):
    def test_getDiagram(self):
        filename = 'inputs/testinput25.txt'
        diagram = day25.getDiagram(filename)
        self.assertEqual(len(diagram), 13)
        self.assertTrue('frs' in diagram)
        self.assertEqual(diagram['frs'], ['qnr', 'lhk', 'lsr'])

    def test_buildApparatus(self):
        diagram = {'jqt':['rhn', 'xhk', 'nvd'],
                   'rsh':['frs', 'pzl', 'lsr'],
                   'xhk':['hfx'],
                   'cmg':['qnr', 'nvd', 'lhk', 'bvb'],
                   'rhn':['xhk', 'bvb', 'hfx'],
                   'bvb':['xhk', 'hfx'],
                   'pzl':['lsr', 'hfx', 'nvd'],
                   'qnr':['nvd'],
                   'ntq':['jqt', 'hfx', 'bvb', 'xhk'],
                   'nvd':['lhk'],
                   'lsr':['lhk'],
                   'rzs':['qnr', 'cmg', 'lsr', 'rsh'],
                   'frs':['qnr', 'lhk', 'lsr']
                   }
        apparatus = day25.getApparatus(diagram)
        self.assertEqual(len(apparatus), 13)

