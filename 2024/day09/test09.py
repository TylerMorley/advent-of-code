import unittest
import day09

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput09.txt'
        layout = day09.getInput(filename)
        expected = '2333133121414131402'
        self.assertEqual(layout, expected)

    def test_formBlocks(self):
        layout = '2333133121414131402'
        blocks = day09.formBlocks(layout)
        expected = ['0', '0', '.', '.', '.', '1', '1', '1', '.', '.', '.', '2', '.', '.', '.', '3', '3', '3', '.', '4', '4', '.', '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '7', '7', '7', '.', '8', '8', '8', '8', '9', '9']
        self.assertEqual(blocks, expected)

        layout = '111010101010101010101'
        blocks = day09.formBlocks(layout)
        expected = ['0', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.assertEqual(blocks, expected)


    def test_moveBlocks(self):
        unmoved = ['0', '0', '.', '.', '.', '1', '1', '1', '.', '.', '.', '2', '.', '.', '.', '3', '3', '3', '.', '4', '4', '.', '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '7', '7', '7', '.', '8', '8', '8', '8', '9', '9']
        moved = day09.moveBlocks(unmoved)
        expected = ['0', '0', '9', '9', '8', '1', '1', '1', '8', '8', '8', '2', '7', '7', '7', '3', '3', '3', '6', '4', '4', '6', '5', '5', '5', '5', '6', '6']
        self.assertEqual(moved, expected)

    def test_calcChecksum(self):
        layout = '2333133121414131402'
        checksum = day09.calcChecksum(layout)
        expected = 1928
        self.assertEqual(checksum, expected)
        
        layout = '111010101010101010101'
        checksum = day09.calcChecksum(layout)
        expected = 340
        self.assertEqual(checksum, expected)
        
        layout = '12345'
        checksum = day09.calcChecksum(layout)
        expected = 60
        self.assertEqual(checksum, expected)
       
class TestPartTwo(unittest.TestCase):
    def test_moveFiles(self):
        unmoved = list('00...111...2...333.44.5555.6666.777.888899')
        moved = day09.moveFiles(unmoved)
        self.assertEqual(moved[2:3], ['9','9'])
#        expected = list('00992111777.44.333....5555.6666.....8888..')
#        self.assertEqual(moved, expected)
