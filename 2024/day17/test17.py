import unittest
import day17

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput17.txt'
        register, program = day17.getInput(filename)
        self.assertTrue(len(register), 3)
        self.assertTrue(len(program), 6)

        exp_program = [0,1,5,4,3,0]
        self.assertEqual(program, exp_program)
        exp_register = [['Register A', 729],
                        ['Register B', 0],
                        ['Register C', 0]]
        self.assertEqual(register, exp_register)

    def test_performInstruction(self):
        opcode = 0
        register = {'a':2}
        operand = 3
        result, register = day17.performInstruction(opcode, register_a, operand)
        self.assertEqual(register['a'], 1)
