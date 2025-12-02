import unittest
import day22

class TestPartOne(unittest.TestCase):
    def test_getInput(self):
        filename = 'testinput22.txt'
        secrets = day22.getInput(filename)
        expected = [1, 10, 100, 2024]
        self.assertEqual(secrets, expected)

    def test_mix(self):
        secret = 42
        to_mix = 15
        mixed = day22.mix(secret, to_mix)
        expected = 37
        self.assertEqual(mixed, expected)

    def test_prune(self):
        secret = 100000000
        pruned = day22.prune(secret)
        expected = 16113920
        self.assertEqual(pruned, expected)

    def test_nextSecret(self):
        secret = 123
        next_secret = day22.nextSecret(secret)
        expected = 15887950
        self.assertEqual(next_secret, expected)

    def test_nextSecrets(self):
        secret = 123
        tenth = day22.nextSecrets(secret, 10)
        expected = 5908254
        self.assertEqual(tenth, expected)

        secret = 1
        two_thousandth = day22.nextSecrets(secret, 2000)
        expected = 8685429
        self.assertEqual(two_thousandth, expected)

        secret = 10
        two_thousandth = day22.nextSecrets(secret, 2000)
        expected = 4700978
        self.assertEqual(two_thousandth, expected)

        secret = 100
        two_thousandth = day22.nextSecrets(secret, 2000)
        expected = 15273692
        self.assertEqual(two_thousandth, expected)

        secret = 2024
        two_thousandth = day22.nextSecrets(secret, 2000)
        expected = 8667524
        self.assertEqual(two_thousandth, expected)

    def test_allBuyers(self):
        secrets = [1, 10, 100, 2024]
        score = day22.allBuyers(secrets)
        expected = 37327623
        self.assertEqual(score, expected)

class TestPartTwo(unittest.TestCase):
    def test_getChange(self):
        secret = 123
        new_secret = 15887950
        change = day22.getChange(secret, new_secret)
        expected = -3
        self.assertEqual(change, expected)

    def test_nextSecrets_changes(self):
        secret = 123
        get_changes = True
        tenth, changes = day22.nextSecrets(secret, 10, get_changes)
        expected = [-3,6,-1,-1,0,2,-2,0,-2]
        self.assertEqual(changes, expected)
