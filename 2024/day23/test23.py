import unittest
import day23

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput23.txt'
        connections = day23.getInput(filename)
        expected = [['kh', 'tc'], ['qp', 'kh'], ['de', 'cg'], ['ka', 'co'], ['yn', 'aq'], ['qp', 'ub'], ['cg', 'tb'], ['vc', 'aq'], ['tb', 'ka'], ['wh', 'tc'], ['yn', 'cg'], ['kh', 'ub'], ['ta', 'co'], ['de', 'co'], ['tc', 'td'], ['tb', 'wq'], ['wh', 'td'], ['ta', 'ka'], ['td', 'qp'], ['aq', 'cg'], ['wq', 'ub'], ['ub', 'vc'], ['de', 'ta'], ['wq', 'aq'], ['wq', 'vc'], ['wh', 'yn'], ['ka', 'de'], ['kh', 'ta'], ['co', 'tc'], ['wh', 'qp'], ['tb', 'vc'], ['td', 'yn']]
        self.assertEqual(connections, expected)

    def test_buildNetwork(self):
        connections = [['kh', 'tc'], ['qp', 'kh'], ['de', 'cg'], ['ka', 'co'], ['yn', 'aq'], ['qp', 'ub'], ['cg', 'tb'], ['vc', 'aq'], ['tb', 'ka'], ['wh', 'tc'], ['yn', 'cg'], ['kh', 'ub'], ['ta', 'co'], ['de', 'co'], ['tc', 'td'], ['tb', 'wq'], ['wh', 'td'], ['ta', 'ka'], ['td', 'qp'], ['aq', 'cg'], ['wq', 'ub'], ['ub', 'vc'], ['de', 'ta'], ['wq', 'aq'], ['wq', 'vc'], ['wh', 'yn'], ['ka', 'de'], ['kh', 'ta'], ['co', 'tc'], ['wh', 'qp'], ['tb', 'vc'], ['td', 'yn']]
        network = day23.buildNetwork(connections)
        self.assertTrue('kh' in network)
        self.assertTrue('qp' in network['kh'])

    def test_common(self):
        first = ['kh', {'tc', 'qp', 'ub', 'ta'}]
        second = ['ka', {'ta', 'de', 'tc', 'qq'}]
        common = day23.common(first, second)
        expected = [{'kh', 'ka', 'tc'}, {'kh', 'ka', 'ta'}]
        self.assertEqual(len(common), len(expected))
        for exp in expected:
            self.assertTrue(exp in common)

    def test_findSets(self):
        network = {'kh': {'tc', 'qp', 'ub', 'ta'}, 'tc': {'kh', 'wh', 'td', 'co'},
                   'qp': {'kh', 'ub', 'td', 'wh'}, 'de': {'cg', 'co', 'ta', 'ka'},
                   'cg': {'de', 'tb', 'yn', 'aq'}, 'ka': {'co', 'tb', 'ta', 'de'},
                   'co': {'ka', 'ta', 'de', 'tc'}, 'yn': {'aq', 'cg', 'wh', 'td'},
                   'aq': {'yn', 'vc', 'cg', 'wq'}, 'ub': {'qp', 'kh', 'wq', 'vc'},
                   'tb': {'cg', 'ka', 'wq', 'vc'}, 'vc': {'aq', 'ub', 'wq', 'tb'},
                   'wh': {'tc', 'td', 'yn', 'qp'}, 'ta': {'co', 'ka', 'de', 'kh'},
                   'td': {'tc', 'wh', 'qp', 'yn'}, 'wq': {'tb', 'ub', 'aq', 'vc'}}
        sets_of_three = day23.findSets(network)
        self.assertEqual(len(sets_of_three), 12)

    def test_getTSets(self):
        sets = [{'aq','cg','yn'},
                {'aq','vc','wq'},
                {'co','de','ka'},
                {'co','de','ta'},
                {'co','ka','ta'},
                {'de','ka','ta'},
                {'kh','qp','ub'},
                {'qp','td','wh'},
                {'tb','vc','wq'},
                {'tc','td','wh'},
                {'td','wh','yn'},
                {'ub','vc','wq'}]
        t_sets = day23.getTSets(sets)
        self.assertEqual(len(t_sets), 7)
