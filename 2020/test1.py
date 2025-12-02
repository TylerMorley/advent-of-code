import unittest
from dayonepartone import findSum, openfile

class TestExamples(unittest.TestCase):
    def testExample1(self):
        example1 = [1721, 979, 366, 299, 675, 1456]
        findExample = openfile('example1.txt')
        self.assertEqual(findExample, example1)

        output = findSum(example1)
        self.assertEqual(output, 514579)
