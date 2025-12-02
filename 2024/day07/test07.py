import unittest
import day07

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput07.txt'
        equations = day07.getInput(filename)
        self.assertEqual(len(equations), 9)
        self.assertEqual(len(equations[0]), 2)
        self.assertEqual(len(equations[0][1]), 2)
        expected = [[190, [10, 19]],
                    [3267, [81, 40, 27]],
                    [83, [17, 5]],
                    [156, [15, 6]],
                    [7290, [6, 8, 6, 15]],
                    [161011, [16, 10, 13]],
                    [192, [17, 8, 14]],
                    [21037, [9, 7, 18, 13]],
                    [292, [11, 6, 16, 20]]]
        self.assertEqual(equations, expected)

    def test_operCombos(self):
        num_nums = 2
        combos = day07.operCombos(num_nums)
        expected = [['+'], ['*']]
        self.assertEqual(combos, expected)

        num_nums = 3
        combos = day07.operCombos(num_nums)
        expected = [['+','+'], ['+','*'], ['*','+'], ['*','*']]
        self.assertEqual(combos, expected)

    def test_checkCombo(self):
        combo = ['+']
        nums = [10, 19]
        test_value = 190
        is_true = day07.checkCombo(combo, nums, test_value)
        self.assertFalse(is_true)
        
        combo = ['*']
        nums = [10, 19]
        test_value = 190
        is_true = day07.checkCombo(combo, nums, test_value)
        self.assertTrue(is_true)

        combo = ['+','*']
        nums = [81, 40, 27]
        test_value = 3267
        is_true = day07.checkCombo(combo, nums, test_value)
        self.assertTrue(is_true)

    def test_checkEquation(self):
        oper_combos = [['+'], ['*']]
        nums = [10, 19]
        test_value = 190
        is_true = day07.checkEquation(oper_combos, nums, test_value)
        self.assertTrue(is_true)

        oper_combos = [['+','+'], ['+','*'], ['*','+'], ['*','*']]
        nums = [81, 40, 27]
        test_value = 3267
        is_true = day07.checkEquation(oper_combos, nums, test_value)
        self.assertTrue(is_true)

    def test_calibrate(self):
        equations = [[190, [10, 19]],
                    [3267, [81, 40, 27]],
                    [83, [17, 5]],
                    [156, [15, 6]],
                    [7290, [6, 8, 6, 15]],
                    [161011, [16, 10, 13]],
                    [192, [17, 8, 14]],
                    [21037, [9, 7, 18, 13]],
                    [292, [11, 6, 16, 20]]]
        calibration_result = day07.calibrate(equations)
        expected = 3749
        self.assertEqual(calibration_result, expected)

class TestPartTwo(unittest.TestCase):
    def test_operCombos_concat(self):
        num_nums = 2
        use_concat = True
        combos = day07.operCombos(num_nums, use_concat)
        expected = [['+'], ['*'], ['||']]
        self.assertEqual(combos, expected)

        num_nums = 3
        use_concat = True
        combos = day07.operCombos(num_nums, use_concat)
        expected = [['+','+'], ['+','*'], ['*','+'], ['*','*'], ['+','||'], ['*', '||'], ['||', '+'], ['||', '*'], ['||','||']]
        self.assertEqual(len(combos), len(expected))
        for exp in expected:
            self.assertTrue(exp in combos)

    def test_checkCombo_concat(self):
        combo = ['||']
        nums = [15, 6]
        test_value = 156
        is_true = day07.checkCombo(combo, nums, test_value)
        self.assertTrue(is_true)
        
        combo = ['*', '||', '*']
        nums = [6,8,6,15]
        test_value = 7290
        is_true = day07.checkCombo(combo, nums, test_value)
        self.assertTrue(is_true)
        
    def test_checkEquation_concat(self):
        oper_combos = [['*', '||', '*']]
        nums = [6,8,6,15]
        test_value = 7290
        is_true = day07.checkEquation(oper_combos, nums, test_value)
        self.assertTrue(is_true)

    def test_calibrate_concat(self):
        equations = [[190, [10, 19]],
                    [3267, [81, 40, 27]],
                    [83, [17, 5]],
                    [156, [15, 6]],
                    [7290, [6, 8, 6, 15]],
                    [161011, [16, 10, 13]],
                    [192, [17, 8, 14]],
                    [21037, [9, 7, 18, 13]],
                    [292, [11, 6, 16, 20]]]
        use_concat = True
        calibration_result = day07.calibrate(equations, use_concat)
        expected = 11387
        self.assertEqual(calibration_result, expected)


