import unittest
import day18

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput18.txt'
        falling_bytes = day18.getInput(filename)
        self.assertEqual(len(falling_bytes), 25)
        expected = [[5,4],[4,2],[4,5],[3,0],[2,1],[6,3],[2,4],[1,5],[0,6],[3,3],[2,6],[5,1],[1,2],[5,5],[2,5],[6,5],[1,4],[0,4],[6,4],[1,1],[6,1],[1,0],[0,5],[1,6],[2,0]]
        for exp in expected:
            self.assertTrue(exp in falling_bytes)

    def test_corruptSpace(self):
        falling_bytes = [[5,4],[4,2],[4,5],[3,0],[2,1],[6,3],[2,4],[1,5],[0,6],[3,3],[2,6],[5,1],[1,2],[5,5],[2,5],[6,5],[1,4],[0,4],[6,4],[1,1],[6,1],[1,0],[0,5],[1,6],[2,0]]
        num_fallen = 12
        space_size = [7,7]
        corrupted = day18.corruptSpace(space_size, falling_bytes, num_fallen)
        self.assertEqual(corrupted[0][3], '#')
        expected = [['.','.','.','#','.','.','.'],
                    ['.','.','#','.','.','#','.'],
                    ['.','.','.','.','#','.','.'],
                    ['.','.','.','#','.','.','#'],
                    ['.','.','#','.','.','#','.'],
                    ['.','#','.','.','#','.','.'],
                    ['#','.','#','.','.','.','.']]
        self.assertEqual(corrupted, expected)

    def test_getNeighbors(self):
        location = [1,0]
        size = [7,7]
        neighbors = day18.getNeighbors(location, size)
        expected = [[0,0],[2,0], [1,1]]
        for exp in expected:
            self.assertTrue(exp in neighbors)

    def test_heatMap(self):
        easy = [['.' for y in range(7)] for x in range(7)]
        location = [0,0]
        distance = 0
        heatmap = day18.heatMap(easy, location, distance)
        expected = [['0','1','2','3','4','5','6'],
                    ['1','2','3','4','5','6','7'],
                    ['2','3','4','5','6','7','8'],
                    ['3','4','5','6','7','8','9'],
                    ['4','5','6','6','8','9','10'],
                    ['5','6','7','7','9','10','11'],
                    ['6','7','8','8','10','11','12']]
        self.assertEqual(heatmap, expected)

        corrupted = [['.','.','.','#','.','.','.'],
                    ['.','.','#','.','.','#','.'],
                    ['.','.','.','.','#','.','.'],
                    ['.','.','.','#','.','.','#'],
                    ['.','.','#','.','.','#','.'],
                    ['.','#','.','.','#','.','.'],
                    ['#','.','#','.','.','.','.']]
        
