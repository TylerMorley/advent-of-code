import unittest
import day03

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput03.txt'
        memory = day03.getInput(filename)
        expected = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
        self.assertTrue(type(memory) is str)
        self.assertEqual(memory, expected)

    def test_isInstruction(self):
        candidate = 'mul(2,4)'
        result = day03.isInstruction(candidate)
        self.assertTrue(result)
        candidate = 'mul(2f,3])'
        result = day03.isInstruction(candidate)
        self.assertFalse(result)
        candidate = 'mul( 3,6)'
        result = day03.isInstruction(candidate)
        self.assertFalse(result)

    def test_findUncorrupted(self):
        memory = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
        instruction,leftover = day03.findUncorrupted(memory)
        exp_instruction, exp_leftover = ['mul(2,4)', '%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))']
        self.assertEqual(instruction, exp_instruction)
        self.assertEqual(leftover, exp_leftover)
        
        memory = 'mul(32,64]then(mul(11,8)mul(8,5))'
        instruction,leftover = day03.findUncorrupted(memory)
        exp_instruction, exp_leftover = [None, '32,64]then(mul(11,8)mul(8,5))']
        self.assertEqual(instruction, exp_instruction)
        self.assertEqual(leftover, exp_leftover)

        memory = 'ul(8,5))'
        instruction,leftover = day03.findUncorrupted(memory)
        exp_instruction, exp_leftover = [None, None]
        self.assertEqual(instruction, exp_instruction)
        self.assertEqual(leftover, exp_leftover)

    def test_multiplyNums(self):
        instruction = 'mul(2,4)'
        product = day03.multiplyNums(instruction)
        expected = 8
        self.assertEqual(product, expected)

    def test_getUncorruptedInstructions(self):
        memory = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
        answer = day03.getUncorruptedInstructions(memory)
        expected = 161
        self.assertEqual(answer, expected)

class TestPartTwo(unittest.TestCase):
    def test_eliminateDont(self):
        memory = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'
        leftover = day03.eliminateDont(memory)
        expected = memory
        self.assertEqual(leftover, expected)
        
        memory = '&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'
        leftover = day03.eliminateDont(memory)
        expected = '?mul(8,5))'
        self.assertEqual(leftover, expected)

        memory = '&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64]don\'t()(mul(11,8)undo()?mul(8,5))'
        leftover = day03.eliminateDont(memory)
        expected = '?mul(8,5))'
        self.assertEqual(leftover, expected)

        memory = '&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64]do()don\'t()(mul(11,8)undo()?mul(8,5))'
        leftover = day03.eliminateDont(memory)
        expected = '?mul(8,5))'
        self.assertEqual(leftover, expected)

    def test_getUncorruptedInstructions_dont(self):
        memory = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'
        checkEnabled = True
        answer = day03.getUncorruptedInstructions(memory, checkEnabled)
        expected = 48
        self.assertEqual(answer, expected)

        memory = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+do()don\'t()mul(32,64](mul(11,8)undo()?mul(8,5))'
        checkEnabled = True
        answer2 = day03.getUncorruptedInstructions(memory, checkEnabled)
        expected = 48
        self.assertEqual(answer2, expected)

