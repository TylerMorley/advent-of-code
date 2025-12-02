import unittest
import day04

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput04.txt'
        word_search = day04.getInput(filename)
        expected = ['..X...',
                    '.SAMX.',
                    '.A..A.',
                    'XMAS.S',
                    '.X....']
        self.assertEqual(word_search, expected)

    def test_searchableTransform(self):
        word_search = ['..X...',
                        '.SAMX.',
                        '.A..A.',
                        'XMAS.S',
                        '.X....']
        searchable = day04.searchableTransform(word_search)
        rows = word_search.copy()
        self.assertEqual(searchable[0], rows)
        
        columns = ['...X.',
                   '.SAMX',
                   'XA.A.',
                   '.M.S.',
                   '.XA..',
                   '...S.']
        self.assertEqual(searchable[1], columns)

        diagonal_nwse = ['.','..','.X.',
                          'XMAS',
                          '.A...',
                          '.S.S.',
                          '.AA.',
                          '.M.','XX','.']
        self.assertEqual(searchable[2], diagonal_nwse)

        diagonal_nesw = ['.','..','.SX',
                         'XAA.',
                         '.M.M.',
                         'XA.X.',
                         '.SA.',
                         '...','.S','.']
        self.assertEqual(searchable[3], diagonal_nesw)

    def test_transformDiag(self):
        word_search = ['..X...',
                        '.SAMX.',
                        '.A..A.',
                        'XMAS.S',
                        '.X....']
        diagonal = day04.transformDiag(word_search)
        expected = ['.','..','.X.',
                          'XMAS',
                          '.A...',
                          '.S.S.',
                          '.AA.',
                          '.M.','XX','.']
        self.assertEqual(diagonal, expected)

    def test_countInstances(self):
        word_search = ['..X...',
                        '.SAMX.',
                        '.A..A.',
                        'XMAS.S',
                        '.X....']
        rule = 'XMAS'
        num_xmas = day04.countInstances(word_search, rule)
        expected = 4
        self.assertEqual(num_xmas, expected)

        word_search = ['MMMSXXMASM',
                        'MSAMXMSMSA',
                        'AMXSXMAAMM',
                        'MSAMASMSMX',
                        'XMASAMXAMM',
                        'XXAMMXXAMA',
                        'SMSMSASXSS',
                        'SAXAMASAAA',
                        'MAMMMXMMMM',
                        'MXMXAXMASX']
        num_xmas = day04.countInstances(word_search, rule)
        expected = 18
        self.assertEqual(num_xmas, expected)

class TestPartTwo(unittest.TestCase):
    def test_getMasLocs(self):
        word_search = ['MMMSXXMASM',
                        'MSAMXMSMSA',
                        'AMXSXMAAMM',
                        'MSAMASMSMX',
                        'XMASAMXAMM',
                        'XXAMMXXAMA',
                        'SMSMSASXSS',
                        'SAXAMASAAA',
                        'MAMMMXMMMM',
                        'MXMXAXMASX']
        diagonal = day04.transformDiag(word_search.copy())
        word = 'MAS'
        locations = day04.getMasLocs(diagonal, word)
        self.assertTrue([5,2] in locations)
        self.assertTrue([8,1] in locations)
        self.assertTrue([10,2] in locations)
        self.assertTrue([10,5] in locations)
        self.assertEqual(len(locations), 4)
        word = 'SAM'
        locations = day04.getMasLocs(diagonal, word)
        self.assertEqual(len(locations), 8)

    def test_countInstances_x(self):
        word_search = ['MMMSXXMASM',
                        'MSAMXMSMSA',
                        'AMXSXMAAMM',
                        'MSAMASMSMX',
                        'XMASAMXAMM',
                        'XXAMMXXAMA',
                        'SMSMSASXSS',
                        'SAXAMASAAA',
                        'MAMMMXMMMM',
                        'MXMXAXMASX']
        rule = 'X-MAS'
        num_masxs = day04.countInstances(word_search, rule)
        expected = 9
        self.assertEqual(num_masxs, expected)

    def test_transposeNwse(self):
        word_search_size = [10,10]
        nwse_loc = [0,0]
        rectangle_loc = day04.transposeNwse(nwse_loc, word_search_size)
        expected = [0, 9]
        self.assertEqual(rectangle_loc, expected)
        
        nwse_loc = [9,0]
        rectangle_loc = day04.transposeNwse(nwse_loc, word_search_size)
        expected = [0, 0]
        self.assertEqual(rectangle_loc, expected)

        nwse_loc = [10,0]
        rectangle_loc = day04.transposeNwse(nwse_loc, word_search_size)
        expected = [1, 0]
        self.assertEqual(rectangle_loc, expected)

        nwse_loc = [11,0]
        rectangle_loc = day04.transposeNwse(nwse_loc, word_search_size)
        expected = [2, 0]
        self.assertEqual(rectangle_loc, expected)

        nwse_loc = [1,1]
        rectangle_loc = day04.transposeNwse(nwse_loc, word_search_size)
        expected = [1,9]
        self.assertEqual(rectangle_loc, expected)

        nwse_loc = [9,8]
        rectangle_loc = day04.transposeNwse(nwse_loc, word_search_size)
        expected = [8,8]
        self.assertEqual(rectangle_loc, expected)

        nwse_loc = [10,1]
        rectangle_loc = day04.transposeNwse(nwse_loc, word_search_size)
        expected = [2, 1]
        self.assertEqual(rectangle_loc, expected)

        nwse_loc = [14,3]
        rectangle_loc = day04.transposeNwse(nwse_loc, word_search_size)
        expected = [8, 3]
        self.assertEqual(rectangle_loc, expected)

    def test_transposeNesw(self):
        word_search_size = [10,10]
        nesw_loc = [0,0]
        rectangle_loc = day04.transposeNesw(nesw_loc, word_search_size)
        expected = [0,0]
        self.assertEqual(rectangle_loc, expected)

        nesw_loc = [1,0]
        rectangle_loc = day04.transposeNesw(nesw_loc, word_search_size)
        expected = [1,0]
        self.assertEqual(rectangle_loc, expected)

        nesw_loc = [10,0]
        rectangle_loc = day04.transposeNesw(nesw_loc, word_search_size)
        expected = [9,1]
        self.assertEqual(rectangle_loc, expected)
        
        nesw_loc = [1,1]
        rectangle_loc = day04.transposeNesw(nesw_loc, word_search_size)
        expected = [0,1]
        self.assertEqual(rectangle_loc, expected)

        nesw_loc = [9,8]
        rectangle_loc = day04.transposeNesw(nesw_loc, word_search_size)
        expected = [1,8]
        self.assertEqual(rectangle_loc, expected)

        nesw_loc = [10,1]
        rectangle_loc = day04.transposeNesw(nesw_loc, word_search_size)
        expected = [8,2]
        self.assertEqual(rectangle_loc, expected)

