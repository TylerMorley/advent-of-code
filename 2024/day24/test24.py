import unittest
import day24

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput24.txt'
        start_values, wires = day24.getInput(filename)
        self.assertEqual(len(start_values), 6)
        exp_values = {'x00': 1,
                      'x01': 1,
                      'x02': 1,
                      'y00': 0,
                      'y01': 1,
                      'y02': 0}
        self.assertEqual(start_values, exp_values)
        self.assertEqual(len(wires), 3)
        exp_wires = [{'inputs': ['x00', 'y00'], 'command': 'AND', 'output': 'z00'},
                     {'inputs': ['x01', 'y01'], 'command': 'XOR', 'output': 'z01'},
                     {'inputs': ['x02', 'y02'], 'command': 'OR', 'output': 'z02'}]
        self.assertEqual(wires, exp_wires)

    def test_simulateGate(self):
        gate = {'inputs': ['x00', 'y00'], 'command': 'AND', 'output': 'z00'}
        values = {'x00': 1, 'y00': 1}
        values = day24.simulateGate(gate, values)
        self.assertTrue('z00' in values)
        self.assertEqual(values['z00'], 1)

        gate = {'inputs': ['x01', 'y01'], 'command': 'XOR', 'output': 'z01'}
        values = {'x01': 1, 'y01': 1}
        values = day24.simulateGate(gate, values)
        self.assertTrue('z01' in values)
        self.assertEqual(values['z01'], 0)

    def test_simulateGates(self):
        values = {'x00': 1,
                  'x01': 1,
                  'x02': 1,
                  'y00': 0,
                  'y01': 1,
                  'y02': 0}
        gates = [{'inputs': ['x00', 'y00'], 'command': 'AND', 'output': 'z00'},
                 {'inputs': ['x01', 'y01'], 'command': 'XOR', 'output': 'z01'},
                 {'inputs': ['x02', 'y02'], 'command': 'OR', 'output': 'z02'}]
        output = day24.simulateGates(gates, values)
        self.assertEqual(output, 4)
