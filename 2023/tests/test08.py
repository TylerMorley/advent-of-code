import unittest
from code import day08

class PartOne(unittest.TestCase):
    def test_getDocument(self):
        filename = 'inputs/testinput08.txt'
        instructions, network = day08.getDocument(filename)
        self.assertEqual(instructions, 'RL')
        self.assertEqual(len(network), 7)
        self.assertEqual(network['AAA'], ['BBB', 'CCC'])
        self.assertEqual(network['CCC'], ['ZZZ', 'GGG'])

    def test_getNextNode(self):
        direction = 'R'
        node = ['BBB', 'CCC']
        next_node = day08.getNextNode(node, direction)
        self.assertEqual(next_node, 'CCC')

        direction = 'L'
        node = ['ZZZ', 'GGG']
        next_node = day08.getNextNode(node, direction)
        self.assertEqual(next_node, 'ZZZ')

    def test_planJourney(self):
        instructions = 'RL'
        network = {'AAA': ['BBB', 'CCC'],
                   'BBB': ['DDD', 'EEE'],
                   'CCC': ['ZZZ', 'GGG'],
                   'DDD': ['DDD', 'DDD'],
                   'EEE': ['EEE', 'EEE'],
                   'GGG': ['GGG', 'GGG'],
                   'ZZZ': ['ZZZ', 'ZZZ']
                   }
        steps = day08.planJourney(instructions, network)
        self.assertEqual(steps, 2)

        instructions = 'LLR'
        network = {'AAA': ['BBB', 'BBB'],
                   'BBB': ['AAA', 'ZZZ'],
                   'ZZZ': ['ZZZ', 'ZZZ']
                   }
        steps = day08.planJourney(instructions, network)
        self.assertEqual(steps, 6)

class PartTwo(unittest.TestCase):
    def test_getStartNodes(self):
        network = {'11A': ['11B', 'XXX'],
                   '11B': ['XXX', '11Z'],
                   '11Z': ['11B', 'XXX'],
                   '22A': ['22B', 'XXX'],
                   '22B': ['22C', '22C'],
                   '22C': ['22Z', '22Z'],
                   '22Z': ['22B', '22B'],
                   'XXX': ['XXX', 'XXX']
                   }
        startNodes = day08.getStartNodes(network)
        self.assertEqual(len(startNodes), 2)

    def test_checkForEndNodes(self):
        nodes = ['11Z', '22Z']
        atEndNodes = day08.checkForEndNodes(nodes)
        self.assertTrue(atEndNodes)

        nodes = ['11A', '22A']
        atEndNodes = day08.checkForEndNodes(nodes)
        self.assertFalse(atEndNodes)

        nodes = ['11Z', '22A']
        atEndNodes = day08.checkForEndNodes(nodes)
        self.assertFalse(atEndNodes)

    def test_planJourney2(self):
        instructions = 'LR'
        network = {'11A': ['11B', 'XXX'],
                   '11B': ['XXX', '11Z'],
                   '11Z': ['11B', 'XXX'],
                   '22A': ['22B', 'XXX'],
                   '22B': ['22C', '22C'],
                   '22C': ['22Z', '22Z'],
                   '22Z': ['22B', '22B'],
                   'XXX': ['XXX', 'XXX']
                   }
        steps = day08.planJourney2(instructions, network)
        self.assertEqual(steps, 6)

