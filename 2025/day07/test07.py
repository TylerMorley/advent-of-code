import unittest
import day07

class PartOne(unittest.TestCase):
    def test_getInputs(self):
        diagram = day07.getInputs('testinput07.txt')
        self.assertEqual(len(diagram), 16)
        self.assertEqual(len(diagram[0]), 15)
        self.assertEqual(diagram[0], '.......S.......')

    def test_moveBeams(self):
        beams = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        cur_row = '...............'
        count_splits, new_beams = day07.moveBeams(beams, cur_row)
        self.assertEqual(count_splits, 0)
        self.assertEqual(new_beams, [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])

        beams = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        cur_row = '.......^.......'
        count_splits, new_beams = day07.moveBeams(beams, cur_row)
        self.assertEqual(count_splits, 1)
        self.assertEqual(new_beams, [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0])

        beams = [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]
        cur_row = '......^.^......'
        count_splits, new_beams = day07.moveBeams(beams, cur_row)
        self.assertEqual(count_splits, 2)
        self.assertEqual(new_beams, [0,0,0,0,0,1,0,2,0,1,0,0,0,0,0])

        beams = [0,1,0,1,5,4,0,7,4,0,2,1,0,1,0]
        cur_row = '.^.^.^.^.^...^.'
        count_splits, new_beams = day07.moveBeams(beams, cur_row)
        self.assertEqual(count_splits, 5)
        self.assertEqual(new_beams, [1,0,2,0,10,0,11,0,11,0,2,1,1,0,1])

    def test_countSplits(self):
        diagram = ['.......S.......',
                   '...............',
                   '.......^.......',
                   '...............',
                   '......^.^......',
                   '...............',
                   '.....^.^.^.....',
                   '...............',
                   '....^.^...^....',
                   '...............',
                   '...^.^...^.^...',
                   '...............',
                   '..^...^.....^..',
                   '...............',
                   '.^.^.^.^.^...^.',
                   '...............']
        num_splits = day07.countSplits(diagram)
        self.assertEqual(num_splits, 21)

class PartTwo(unittest.TestCase):
    def test_moveBeams2(self):
        beams = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        cur_row = '...............'
        is_quantum = True
        new_beams = day07.moveBeams(beams, cur_row, is_quantum)
        self.assertEqual(new_beams, [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])

        beams = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        cur_row = '.......^.......'
        is_quantum = True
        new_beams = day07.moveBeams(beams, cur_row, is_quantum)
        self.assertEqual(new_beams, [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0])

        beams = [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]
        cur_row = '......^.^......'
        is_quantum = True
        new_beams = day07.moveBeams(beams, cur_row, is_quantum)
        self.assertEqual(new_beams, [0,0,0,0,0,1,0,2,0,1,0,0,0,0,0])

        beams = [0,1,0,1,5,4,0,7,4,0,2,1,0,1,0]
        cur_row = '.^.^.^.^.^...^.'
        is_quantum = True
        new_beams = day07.moveBeams(beams, cur_row, is_quantum)
        self.assertEqual(new_beams, [1,0,2,0,10,0,11,0,11,0,2,1,1,0,1])

    def test_countTimelines(self):
        diagram = ['.......S.......',
                   '...............',
                   '.......^.......',
                   '...............',
                   '......^.^......',
                   '...............',
                   '.....^.^.^.....',
                   '...............',
                   '....^.^...^....',
                   '...............',
                   '...^.^...^.^...',
                   '...............',
                   '..^...^.....^..',
                   '...............',
                   '.^.^.^.^.^...^.',
                   '...............']
        num_timelines = day07.countTimelines(diagram)
        self.assertEqual(num_timelines, 40)
