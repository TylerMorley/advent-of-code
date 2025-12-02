import unittest
import day21

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput21.txt'
        codes = day21.getInput(filename)
        expected = ['029A',
                    '980A',
                    '179A',
                    '456A',
                    '379A']
        self.assertEqual(codes, expected)

    def test_targetLocation(self):
        numpad = [['7', '8', '9'],
                  ['4', '5', '6'],
                  ['1', '2', '3'],
                  [' ', '0', 'A']]
        button = '0'
        location = day21.targetLocation(numpad, button)
        expected = [1,3]
        self.assertEqual(location, expected)

    def test_arrowToNum(self):
        code = '029A'
        presses = day21.arrowToNum(code)
        expected = ['<A^A>^^AvvvA', '<A^A^>^AvvvA','<A^A^^>AvvvA']
        self.assertTrue(presses in expected)

    def test_arrowToArrow(self):
        arrows = '<A^A>^^AvvvA'
        presses = day21.arrowToArrow(arrows)
        expected = 'v<<A>>^A<A>AvA<^AA>A<vAAA>^A'
        self.assertEqual(len(presses), len(expected))

        arrows = 'v<<A>>^A<A>AvA<^AA>A<vAAA>^A'
        presses = day21.arrowToArrow(arrows)
        expected = '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'
        self.assertEqual(len(presses), len(expected))

    def test_getComplexity(self):
        code = '029A'
        complexity = day21.getComplexity(code)
        expected = 1972
        self.assertEqual(complexity, expected)

        code = '980A'
        complexity = day21.getComplexity(code)
        expected = 58800
        self.assertEqual(complexity, expected)

        code = '179A'
        complexity = day21.getComplexity(code)
        expected = 12172
        self.assertEqual(complexity, expected)

        code = '456A'
        complexity = day21.getComplexity(code)
        expected = 29184
        self.assertEqual(complexity, expected)

        code = '379A'
        complexity = day21.getComplexity(code)
        expected = 24256
        self.assertEqual(complexity, expected)
