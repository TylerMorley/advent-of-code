import unittest
import day05

class PartOne(unittest.TestCase):
    def test_getInputs(self):
        filename = 'testinput05.txt'
        ranges, ids = day05.getInputs(filename)
        self.assertEqual(len(ranges), 4)
        self.assertEqual(len(ids), 6)

        self.assertEqual(ranges[0], [3,5])
        self.assertEqual(ids[0], 1)

    def test_checkFreshness(self):
        ranges = [[3, 5], [10, 14], [16, 20], [12, 18]]
        ingredient_id = 1
        is_fresh = day05.checkFreshness(ingredient_id, ranges)
        self.assertFalse(is_fresh)

    def test_countFreshIngredients(self):
        ranges = [[3, 5], [10, 14], [16, 20], [12, 18]]
        ingredient_ids = [1, 5, 8, 11, 17, 32]
        num_fresh = day05.countFreshIngredients(ingredient_ids, ranges)
        self.assertEqual(num_fresh, 3)
