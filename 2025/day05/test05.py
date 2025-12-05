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

class PartTwo(unittest.TestCase):
    def test_compareRanges(self):
        existing_range = [3,5]
        new_range = [10,14]
        message, updates = day05.compareRanges(new_range, existing_range)
        self.assertEqual(message, 'disjoint')
        self.assertIsNone(updates)

        existing_range = [3,10]
        new_range = [5,9]
        message, updates = day05.compareRanges(new_range, existing_range)
        self.assertEqual(message, 'subset')
        self.assertEqual(updates, None)

        existing_range = [10,14]
        new_range = [12,18]
        message, updates = day05.compareRanges(new_range, existing_range)
        self.assertEqual(message, 'update')
        self.assertEqual(updates, [10,18])

        existing_range = [10,14]
        new_range = [7,12]
        message, updates = day05.compareRanges(new_range, existing_range)
        self.assertEqual(message, 'update')
        self.assertEqual(updates, [7,14])

        existing_range = [10,14]
        new_range = [9,20]
        message, updates = day05.compareRanges(new_range, existing_range)
        self.assertEqual(message, 'update')
        self.assertEqual(updates, [9,20])

    def test_buildIdDb(self):
        counted = [[3,5]]
        id_range = [10,14]
        new_counted = day05.buildIdDb(id_range, counted)
        self.assertTrue(id_range in new_counted)

        counted = [[3,10]]
        id_range = [5,9]
        new_counted = day05.buildIdDb(id_range, counted)
        self.assertEqual(new_counted, [[3,10]])

        counted = [[3,5], [10,14]]
        id_range = [12,18]
        new_counted = day05.buildIdDb(id_range, counted)
        self.assertEqual(new_counted, [[3,5], [10,18]])

        counted = [[3,5], [10,14]]
        id_range = [7,12]
        new_counted = day05.buildIdDb(id_range, counted)
        self.assertEqual(new_counted, [[3,5], [7,14]])

        counted = [[3,5]]
        id_range = [2,10]
        new_counted = day05.buildIdDb(id_range, counted)
        self.assertEqual(new_counted, [[2,10]])

        counted = [[3,5],[10,14],[16,20]]
        id_range = [12,18]
        new_counted = day05.buildIdDb(id_range, counted)
        self.assertEqual(new_counted, [[3,5],[10,20]])

    def test_countFreshIds(self):
        ranges = [[3, 5], [10, 14], [16, 20], [12, 18]]
        fresh_ids = day05.countFreshIds(ranges)
        self.assertEqual(fresh_ids, 14)

