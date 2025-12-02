import unittest
import day05

class TestPartOne(unittest.TestCase):
    def test_getInputs(self):
        filename = 'testinput05.txt'
        rules, pages = day05.getInputs(filename)
        self.assertEqual(rules[0], [47,53])
        self.assertEqual(len(rules), 21)
        self.assertEqual(pages[0], [75,47,61,53,29])
        self.assertEqual(len(pages), 6)

    def test_checkRule(self):
        rule = [75,47]
        update = [75,47,61,53,29]
        isOrdered = day05.checkRule(rule, update)
        self.assertTrue(isOrdered)

        rule = [97,75]
        update = [75,97,47,61,53]
        isOrdered = day05.checkRule(rule, update)
        self.assertFalse(isOrdered)

    def test_checkRules(self):
        rules = [[47, 53], [97, 13], [97, 61], [97, 47], [75, 29], [61, 13], [75, 53], [29, 13], [97, 29], [53, 29], [61, 53], [97, 53], [61, 29], [47, 13], [75, 47], [97, 75], [47, 61], [75, 61], [47, 29], [75, 13], [53, 13]]
        update = [75,47,61,53,29]
        isOrdered = day05.checkRules(rules, update)
        self.assertTrue(isOrdered)

        update = [75,97,47,61,53]
        isOrdered = day05.checkRules(rules, update)
        self.assertFalse(isOrdered)

    def test_middlePages(self):
        updates = [[75,47,61,53,29],
                    [97,61,53,29,13],
                    [75,29,13]]
        score = day05.middlePages(updates)
        expected = 143
        self.assertEqual(score, expected)

class TestPartTwo(unittest.TestCase):
    def test_applyRule(self):
        rule = [97,75]
        update = [75,97,47,61,53]
        new_update = day05.applyRule(rule, update)
        expected = [97, 75, 47, 61, 53]
        self.assertEqual(new_update, expected)

    def test_applyRules(self):
        rules = [[47, 53], [97, 13], [97, 61], [97, 47], [75, 29], [61, 13], [75, 53], [29, 13], [97, 29], [53, 29], [61, 53], [97, 53], [61, 29], [47, 13], [75, 47], [97, 75], [47, 61], [75, 61], [47, 29], [75, 13], [53, 13]]
        update = [75,97,47,61,53]
        new_update = day05.applyRules(rules, update)
        expected = [97, 75, 47, 61, 53]
        self.assertEqual(new_update, expected)

        update = [61, 13, 29]
        new_update = day05.applyRules(rules, update)
        expected = [61, 29, 13]
        self.assertEqual(new_update, expected)

        update = [97, 13, 75, 29, 47]
        new_update = day05.applyRules(rules, update)
        expected = [97, 75, 47, 29, 13]
        self.assertEqual(new_update, expected)

    def test_divideByRules(self):
        rules = [[47, 53], [97, 13], [97, 61], [97, 47], [75, 29], [61, 13], [75, 53], [29, 13], [97, 29], [53, 29], [61, 53], [97, 53], [61, 29], [47, 13], [75, 47], [97, 75], [47, 61], [75, 61], [47, 29], [75, 13], [53, 13]]
        updates = [[75,47,61,53,29],
                    [97,61,53,29,13],
                    [75,29,13],
                    [75,97,47,61,53],
                    [61,13,29],
                    [97,13,75,29,47]]
        ordered, unordered = day05.divideByRules(rules, updates)
        exp_ordered = [[75,47,61,53,29],
                        [97,61,53,29,13],
                        [75,29,13]]
        exp_unordered = [[75,97,47,61,53],
                        [61,13,29],
                        [97,13,75,29,47]]
        self.assertEqual(ordered, exp_ordered)
        self.assertEqual(unordered, exp_unordered)

    def test_reorderUpdates(self):
        rules = [[47, 53], [97, 13], [97, 61], [97, 47], [75, 29], [61, 13], [75, 53], [29, 13], [97, 29], [53, 29], [61, 53], [97, 53], [61, 29], [47, 13], [75, 47], [97, 75], [47, 61], [75, 61], [47, 29], [75, 13], [53, 13]]
        unordered = [[75,97,47,61,53],
                    [61,13,29],
                    [97,13,75,29,47]]
        reordered = day05.reorderUpdates(rules, unordered)
        expected = [[97,75,47,61,53],
                    [61,29,13],
                    [97,75,47,29,13]]
        self.assertEqual(reordered, expected)
