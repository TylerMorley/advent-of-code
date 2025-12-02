import unittest
import day11

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput11.txt'
        stones = day11.getInput(filename)
        expected = [0, 1, 10, 99, 999]
        self.assertEqual(stones, expected)

    def test_transformStone(self):
        stone_in = 0
        transformed = day11.transformStone(stone_in)
        expected = [1]
        self.assertEqual(transformed, expected)

        stone_in = 1
        transformed = day11.transformStone(stone_in)
        expected = [2024]
        self.assertEqual(transformed, expected)

        stone_in = 10
        transformed = day11.transformStone(stone_in)
        expected = [1,0]
        self.assertEqual(transformed, expected)

        stone_in = 99
        transformed = day11.transformStone(stone_in)
        expected = [9,9]
        self.assertEqual(transformed, expected)

        stone_in = 999
        transformed = day11.transformStone(stone_in)
        expected = [2021976]
        self.assertEqual(transformed, expected)

    def test_blink(self):
        stones = [0, 1, 10, 99, 999]
        blinked = day11.blink(stones)
        expected = [1, 2024, 1, 0, 9, 9, 2021976]
        self.assertEqual(blinked, expected)

    def test_blinks(self):
        stones = [125, 17]
        six_blinks = day11.blinks(stones, 6)
        expected = 22
        self.assertEqual(six_blinks, expected)
        
        stones = [125, 17]
        twenty_five = day11.blinks(stones, 25)
        expected = 55312
        self.assertEqual(twenty_five, expected)

class TestPartTwo(unittest.TestCase):
    def test_simulateZeros(self):
        stones = [2,0,2,4]
        i = 4
        simulation = {'z0':1, 'z1':1, 'z2':1, 'z3':2}
        stones, simulation, i = day11.simulateZeros(stones, simulation, i)
        exp_stones = [2,'z0',2,4]
        self.assertEqual(stones, exp_stones)
        self.assertEqual(len(simulation), 5)
        self.assertEqual(simulation['z4'], 4)
        
        stones = [4096,'z0',4096,8192]
        i = 5
        simulation = {'z0':1, 'z1':1, 'z2':1, 'z3':2, 'z4':4}
        stones, simulation, i = day11.simulateZeros(stones, simulation, i)
        self.assertEqual(stones, [4096, 'z1', 4096, 8192])
        self.assertEqual(simulation['z5'], 4)
        
        stones = [40,96,'z1',40,96,81,92]
        i = 6
        simulation = {'z0':1, 'z1':1, 'z2':1, 'z3':2, 'z4':4, 'z5':4}
        stones, simulation, i = day11.simulateZeros(stones, simulation, i)
        self.assertEqual(stones, [40,96,'z2',40,96,81,92])
        self.assertEqual(simulation['z6'], 7)
        
        stones = [4,0,9,6,'z2',4,0,9,6,8,1,9,2]
        i = 7
        simulation = {'z0':1, 'z1':1, 'z2':1, 'z3':2, 'z4':4, 'z5':4, 'z6':7}
        stones, simulation, i = day11.simulateZeros(stones, simulation, i)
        self.assertEqual(stones, [4,'z0',9,6,'z3',4,'z0',9,6,8,1,9,2])
        self.assertEqual(simulation['z7'], 13)
        
        stones = [8192,'z0',18216,12144,'z3',8192,'z0',8192,18216,16384,2024,18216,4096]
        i = 8
        simulation = {'z0':1, 'z1':1, 'z2':1, 'z3':2, 'z4':4, 'z5':4, 'z6':7, 'z7':13}
        stones, simulation , i = day11.simulateZeros(stones, simulation, i)
        self.assertEqual(stones, [8192,'z1',18216,12144,'z4',8192,'z1',8192,18216,16384,2024,18216,4096])
        self.assertEqual(simulation['z8'], 14)

    def test_generationSize(self):
        stones = [8192,'z0',18216,12144,'z3',8192,'z0',8192,18216,16384,2024,18216,4096]
        simulation = {'z0':1, 'z1':1, 'z2':1, 'z3':2, 'z4':4, 'z5':4, 'z6':7, 'z7':13}
        gen_size = day11.generationSize(stones, simulation)
        self.assertEqual(gen_size, 14)

    def test_blink_zeroes(self):
        stones = ['z0', 1, 10, 99, 999]
        blinked = day11.blink(stones)
        expected = ['z0', 2024, 1, 0, 9, 9, 2021976]
        self.assertEqual(blinked, expected)

    def test_updateSim(self):
        simulation = dict()
        z_gen = None
        

    def test_blinks_zeroes(self):
        stones = [125, 17]
        gen = None
        simulation = dict()
        stones, simulation, gen = day11.simulateZeros(stones, simulation, gen)
        self.assertEqual(gen, None)

        stones = [253, 0, 2024, 14168]
        gen = None
        simulation = dict()
        stones, simulation, gen = day11.simulateZeros(stones, simulation, gen)
        self.assertEqual(gen, 0)
        self.assertEqual(simulation['z0'], 1)
