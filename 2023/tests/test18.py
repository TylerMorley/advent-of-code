import unittest
from code import day18

class PartOne(unittest.TestCase):
    def test_getDigPlan(self):
        filename = 'inputs/testinput18.txt'
        dig_plan = day18.getDigPlan(filename)
        self.assertEqual(len(dig_plan), 14)
        self.assertEqual(dig_plan[0][1], 6)

    def test_dig(self):
        trench = {'x0y0':'#'}
        position = 'x0y0'

        direction = ['R', 6, '#70c710']
        trench, position = day18.dig(trench, position, direction)
        self.assertEqual(trench['x0y0'], '#')
        self.assertEqual(trench['x6y0'], '#')
        self.assertTrue('x7y0' not in trench)
        self.assertEqual(position, 'x6y0')
        
        direction = ['D', 5, '#0dc571']
        trench, position = day18.dig(trench, position, direction)
        self.assertEqual(trench['x6y0'], '#')
        self.assertEqual(trench['x6y5'], '#')
        self.assertTrue('x6y6' not in trench)
        self.assertEqual(position, 'x6y5')
        
        direction = ['L', 2, '#5713f0']
        trench, position = day18.dig(trench, position, direction)
        self.assertEqual(trench['x6y5'], '#')
        self.assertEqual(trench['x4y5'], '#')
        self.assertTrue('x3y5' not in trench)
        self.assertEqual(position, 'x4y5')

        direction = ['U', 1, '#d2c081']
        trench, position = day18.dig(trench, position, direction)
        self.assertEqual(trench['x4y4'], '#')
        self.assertTrue('x4y3' not in trench)
        self.assertEqual(position, 'x4y4')

    def test_digTrench(self):
        directions = [['R', 6, '#70c710'],
                      ['D', 5, '#0dc571'],
                      ['L', 2, '#5713f0'],
                      ['D', 2, '#d2c081'],
                      ['R', 2, '#59c680'],
                      ['D', 2, '#411b91'],
                      ['L', 5, '#8ceee2'],
                      ['U', 2, '#caa173'],
                      ['L', 1, '#1b58a2'],
                      ['U', 2, '#caa171'],
                      ['R', 2, '#7807d2'],
                      ['U', 3, '#a77fa3'],
                      ['L', 2, '#015232'],
                      ['U', 2, '#7a21e3']]
        trench = day18.digTrench(directions)
        self.assertEqual(len(trench), 38)
        self.assertFalse('x5y1' in trench)
        self.assertEqual(trench['x2y2'], '#')

    def test_isInside(self):
        row = '#.....#'
        ind = 1
        response = day18.isInside(row, ind)
        self.assertEqual(response, True)

        row = '..#...#'
        ind = 1
        response = day18.isInside(row, ind)
        self.assertEqual(response, False)

        row = '#.#.#.#'
        ind = 3
        response = day18.isInside(row, ind)
        self.assertEqual(response, False)

        row = '##..###'
        ind = 2
        response = day18.isInside(row, ind)
        self.assertEqual(response, True)


    def test_fillTrench(self):
        outline = ['#######',
                   '#.....#',
                   '###...#',
                   '..#...#',
                   '..#...#',
                   '###.###', 
                   '#...#..',
                   '##..###',
                   '.#....#',
                   '.######']
        filled = day18.fillTrench(outline)

        count = 0
        for line in filled:
            count += line.count('#')
        self.assertEqual(count, 62)
