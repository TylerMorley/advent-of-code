import unittest
import day25

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.images = [['#####',
                     '.####',
                     '.####',
                     '.####',
                     '.#.#.',
                     '.#...',
                     '.....'],
                    ['#####',
                     '##.##',
                     '.#.##',
                     '...##',
                     '...#.',
                     '...#.',
                     '.....'],
                    ['.....',
                     '#....',
                     '#....',
                     '#...#',
                     '#.#.#',
                     '#.###',
                     '#####'],
                    ['.....',
                     '.....',
                     '#.#..',
                     '###..',
                     '###.#',
                     '###.#',
                     '#####'],
                    ['.....',
                     '.....',
                     '.....',
                     '#....',
                     '#.#..',
                     '#.#.#',
                     '#####']]
    def test_getInput(self):
        filename = 'testinput25.txt'
        key_images = day25.getInput(filename)
        expected = self.images
        self.assertEqual(len(key_images), len(expected))
        self.assertEqual(len(key_images[0]), 7)
        self.assertEqual(key_images, expected)

    def test_imageToNums(self):
        image = ['#####',
                 '.####',
                 '.####',
                 '.####',
                 '.#.#.',
                 '.#...',
                 '.....']
        key_or_lock, heights = day25.imageToNums(image)
        self.assertEqual(key_or_lock, 'locks')
        exp_heights = [0,5,3,4,3]
        self.assertEqual(heights, exp_heights)

        image = ['.....',
                 '#....',
                 '#....',
                 '#...#',
                 '#.#.#',
                 '#.###',
                 '#####',]
        key_or_lock, heights = day25.imageToNums(image)
        self.assertEqual(key_or_lock, 'keys')
        exp_heights = [5,0,2,1,3]
        self.assertEqual(heights, exp_heights)


    def test_checkFit(self):
        key = [5,0,2,1,3]
        lock = [0,5,3,4,3]
        fit = day25.checkFit(lock, key)
        self.assertFalse(fit)

    def test_countLKPairs(self):
        locks = [[0,5,3,4,3],
                 [1,2,0,5,3]]
        keys = [[5,0,2,1,3],
                [4,3,4,0,2],
                [3,0,2,0,1]]
        num_pairs = day25.countLKPairs(locks, keys)
        expected = 3
        self.assertEqual(num_pairs, expected)

    def test_testLocksAndKeys(self):
        images = self.images.copy()
        count = day25.testLocksAndKeys(images)
        expected = 3
        self.assertEqual(count, expected)
