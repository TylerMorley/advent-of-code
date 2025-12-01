import unittest
from code import day20

class PartOne(unittest.TestCase):
    def test_getConfig(self):
        filename = 'inputs/testinput20-1.txt'
        config = day20.getConfig(filename)
        self.assertEqual(len(config), 5)
        self.assertEqual(config['broadcaster']['destination'], ['a', 'b', 'c'])
        self.assertEqual(config['c']['prefix'], '%')
        self.assertEqual(config['c']['destination'], ['inv'])

    def test_sendPulse(self):
        config = {'broadcaster': {'destination': ['a', 'b', 'c']},
                  'a': {'destination': ['b'], 'prefix': '%'},
                  'b': {'destination': ['c'], 'prefix': '%'},
                  'c': {'destination': ['inv'], 'prefix': '%'},
                  'inv': {'destination': ['a'], 'prefix': '&'}
                  }

        pulse = ['broadcaster', 'low', 'a']
        destination, config = day20.sendPulse(pulse, config)
        self.assertTrue(config['a']['isOn'])
        self.assertEqual(destination, [['a', 'high', 'b']])

        config = {'broadcaster': {'destination': ['a', 'b', 'c']},
                  'a': {'destination': ['b'], 'prefix': '%'},
                  'b': {'destination': ['c'], 'prefix': '%'},
                  'c': {'destination': ['inv'], 'prefix': '%'},
                  'inv': {'destination': ['a'], 'prefix': '&'}
                  }
        pulse = ['c', 'high', 'inv']
        destination, config = day20.sendPulse(pulse, config)
        self.assertEqual(config['inv']['mem']['c'], 'high')
        self.assertEqual(destination, [['inv', 'low', 'a']])
