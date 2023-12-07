import unittest
from code import day05

class PartOne(unittest.TestCase):
    def test_buildAlmanac(self):
        filename = 'inputs/testinput05.txt'
        almanac = day05.buildAlmanac(filename)
        self.assertEqual(len(almanac), 8)
        self.assertTrue(79 in almanac['seeds'])
        self.assertEqual(len(almanac['seed-to-soil']), 2)
        self.assertEqual(len(almanac['soil-to-fertilizer']), 3)
        self.assertEqual(len(almanac['fertilizer-to-water']), 4)
        self.assertEqual(len(almanac['water-to-light']), 2)
        self.assertEqual(len(almanac['light-to-temperature']), 3)
        self.assertEqual(len(almanac['temperature-to-humidity']), 2)
        self.assertEqual(len(almanac['humidity-to-location']), 2)

    def test_getDestination(self):
        almanac_map = [[50, 98, 2], [52, 50, 48]]
        source = 79
        destination = day05.getDestination(almanac_map, source)
        self.assertEqual(destination, 81)
        source = 14
        destination = day05.getDestination(almanac_map, source)
        self.assertEqual(destination, 14)
        source = 55
        destination = day05.getDestination(almanac_map, source)
        self.assertEqual(destination, 57)
        source = 13
        destination = day05.getDestination(almanac_map, source)
        self.assertEqual(destination, 13)

    def test_seedToLocation(self):
        almanac = {'seeds': [79, 14, 55, 13], 
                   'seed-to-soil': [[50, 98, 2], [52, 50, 48]], 
                   'soil-to-fertilizer': [[0, 15, 37], [37, 52, 2], [39, 0, 15]], 
                   'fertilizer-to-water': [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]], 
                   'water-to-light': [[88, 18, 7], [18, 25, 70]], 
                   'light-to-temperature': [[45, 77, 23], [81, 45, 19], [68, 64, 13]], 
                   'temperature-to-humidity': [[0, 69, 1], [1, 0, 69]], 
                   'humidity-to-location': [[60, 56, 37], [56, 93, 4]]
                   }
        record = dict()
        seed = 79
        location = day05.seedToLocation(almanac, record, seed)
        self.assertEqual(location, 82)
        seed = 14
        location = day05.seedToLocation(almanac, seed)
        self.assertEqual(location, 43)
        seed = 55
        location = day05.seedToLocation(almanac, seed)
        self.assertEqual(location, 86)
        seed = 13
        location = day05.seedToLocation(almanac, seed)
        self.assertEqual(location, 35)

class PartTwo(unittest.TestCase):
    def test_buildSeedRanges(self):
        seeds = [79, 14, 55, 13]
        seed_ranges = day05.buildSeedRanges(seeds)
        self.assertEqual(seed_ranges, [[79, 14], [55, 13]])

    def test_findLowestLocation2(self):
        almanac = {'seeds': [79, 14, 55, 13], 
                   'seed-to-soil': [[50, 98, 2], [52, 50, 48]], 
                   'soil-to-fertilizer': [[0, 15, 37], [37, 52, 2], [39, 0, 15]], 
                   'fertilizer-to-water': [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]], 
                   'water-to-light': [[88, 18, 7], [18, 25, 70]], 
                   'light-to-temperature': [[45, 77, 23], [81, 45, 19], [68, 64, 13]], 
                   'temperature-to-humidity': [[0, 69, 1], [1, 0, 69]], 
                   'humidity-to-location': [[60, 56, 37], [56, 93, 4]]
                   }
        location = day05.findLowestLocation2(almanac)
        self.assertEqual(location, 46)
