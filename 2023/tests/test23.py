import unittest
from code import day23

class PartOne(unittest.TestCase):
    def test_getTrails(self):
        filename = 'inputs/testinput23.txt'
        trails = day23.getTrails(filename)
        self.assertEqual(len(trails), 23)
        self.assertEqual(len(trails[0]), 23)
       
    def test_getSegments(self):
        trails = ['#.#####################',
                  '#.......#########...###',
                  '#######.#########.#.###',
                  '###.....#.>.>.###.#.###',
                  '###v#####.#v#.###.#.###',
                  '###.>...#.#.#.....#...#',
                  '###v###.#.#.#########.#',
                  '###...#.#.#.......#...#',
                  '#####.#.#.#######.#.###',
                  '#.....#.#.#.......#...#',
                  '#.#####.#.#.#########v#',
                  '#.#...#...#...###...>.#',
                  '#.#.#v#######v###.###v#',
                  '#...#.>.#...>.>.#.###.#',
                  '#####v#.#.###v#.#.###.#',
                  '#.....#...#...#.#.#...#',
                  '#.#########.###.#.#.###',
                  '#...###...#...#...#.###',
                  '###.###.#.###v#####v###',
                  '#...#...#.#.>.>.#.>.###',
                  '#.###.###.#.###.#.#v###',
                  '#.....###...###...#...#',
                  '#####################.#'
                  ]
        segments = day23.getSegments(trails)
        self.assertEqual(len(segments), 12) #might be wrong
