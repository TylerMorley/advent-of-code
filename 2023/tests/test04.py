import unittest
from code import day04

class PartOne(unittest.TestCase):
    def test_getCards(self):
        filename = 'inputs/testinput04.txt'
        scratch_cards = day04.getCards(filename)
        self.assertEqual(len(scratch_cards), 6)
        self.assertEqual(len(scratch_cards[0]), 2)
        self.assertEqual(len(scratch_cards[0][0]), 5)

    def test_getWinners(self):
        card = [['41', '48', '83', '86', '17'], ['83', '86', '6', '31', '17', '9', '48', '53']]
        winners = day04.getWinners(card)
        self.assertEqual(len(winners), 4)

    def test_getAllWinners(self):
        cards = [[['41', '48', '83', '86', '17'], ['83', '86', '6', '31', '17', '9', '48', '53']],
                 [['13', '32', '20', '16', '61'], ['61', '30', '68', '82', '17', '32', '24', '19']],
                 [['1', '21', '53', '59', '44'], ['69', '82', '63', '72', '16', '21', '14', '1']],
                 [['41', '92', '73', '84', '69'], ['59', '84', '76', '51', '58', '5', '54', '83']],
                 [['87', '83', '26', '28', '32'], ['88', '30', '70', '12', '93', '22', '82', '36']],
                 [['31', '18', '13', '56', '72'], ['74', '77', '10', '23', '35', '67', '36', '11']]]
        winners = day04.getAllWinners(cards)
        self.assertEqual(len(winners), 6)
        self.assertEqual(len(winners[0]), 4)
        self.assertEqual(len(winners[1]), 2)
        self.assertEqual(len(winners[2]), 2)
        self.assertEqual(len(winners[3]), 1)
        self.assertEqual(len(winners[4]), 0)
        self.assertEqual(len(winners[5]), 0)

    def test_getScore(self):
        winners = ['48', '83', '17', '86']
        score = day04.getScore(winners)
        self.assertEqual(score, 8)

    def test_getScores(self):
        winners = [['48', '83', '17', '86'],
                   ['32', '61'],
                   ['1', '21'],
                   ['84'],
                   [],
                   []]
        score_total = day04.getScores(winners)
        self.assertEqual(score_total, 13)

class PartTwo(unittest.TestCase):
    def test_checkCard(self):
        stacks = [1, 1, 1, 1, 1, 1]
        card = [['41', '48', '83', '86', '17'], ['83', '86', '6', '31', '17', '9', '48', '53']]
        stack_index = 0
        updated_stacks = day04.checkCard(stacks, card, stack_index)
        self.assertEqual(updated_stacks, [1,2,2,2,2,1])

        stacks = [1, 2, 2, 2, 2, 1]
        card = [['13', '32', '20', '16', '61'], ['61', '30', '68', '82', '17', '32', '24', '19']]
        stack_index = 1
        updated_stacks = day04.checkCard(stacks, card, stack_index)
        self.assertEqual(updated_stacks, [1,2,4,4,2,1])

    def test_checkCards(self):
        cards = [[['41', '48', '83', '86', '17'], ['83', '86', '6', '31', '17', '9', '48', '53']],
                 [['13', '32', '20', '16', '61'], ['61', '30', '68', '82', '17', '32', '24', '19']],
                 [['1', '21', '53', '59', '44'], ['69', '82', '63', '72', '16', '21', '14', '1']],
                 [['41', '92', '73', '84', '69'], ['59', '84', '76', '51', '58', '5', '54', '83']],
                 [['87', '83', '26', '28', '32'], ['88', '30', '70', '12', '93', '22', '82', '36']],
                 [['31', '18', '13', '56', '72'], ['74', '77', '10', '23', '35', '67', '36', '11']]]
        score = day04.checkCards(cards)
        self.assertEqual(score, 30)
