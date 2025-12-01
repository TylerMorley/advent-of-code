import unittest
from code import day07

class PartOne(unittest.TestCase):
    def test_getHands(self):
        filename = 'inputs/testinput07.txt'
        hands = day07.getHands(filename)
        self.assertEqual(len(hands), 5)
        self.assertEqual(len(hands[1]), 2)
        self.assertEqual(hands[2][1], 28)

    def test_isOfAKind(self):
        hand = 'AAAAA'
        isFive = day07.isOfAKind(hand)
        self.assertEqual(isFive, 'five')
        hand = 'AA8AA'
        isFour = day07.isOfAKind(hand)
        self.assertEqual(isFour, 'four')
        hand = '23332'
        isFullHouse = day07.isOfAKind(hand)
        self.assertEqual(isFullHouse, 'full')
        hand = 'T55J5'
        isThree = day07.isOfAKind(hand)
        self.assertEqual(isThree, 'three')
        hand = '23432'
        isTwoPair = day07.isOfAKind(hand)
        self.assertEqual(isTwoPair, 'two pair')
        hand = 'A23A4'
        isPair = day07.isOfAKind(hand)
        self.assertEqual(isPair, 'pair')
        hand = '32T5K'
        isThree = day07.isOfAKind(hand)
        self.assertEqual(isThree, 'high')

    def test_categorize(self):
        uncat_hands = [['32T3K', '765'], ['T55J5', '684'], ['KK677', '28'], ['KTJJT', '220'], ['QQQJA', '483']]
        cat_hands = day07.categorize(uncat_hands)
        self.assertEqual(len(cat_hands['three']), 2)

    def test_getBestHand(self):
        hands = ['33332', '2AAAA']
        card_index = 0
        ordered = day07.getBestHand(hands, card_index)
        self.assertEqual(ordered, ['33332'])

        hands = ['A22KK', 'A2345']
        card_index = 1
        ordered = day07.getBestHand(hands, card_index)
        self.assertEqual(len(ordered), 2)

        hands = ['TTTTT', 'TTTTT']
        card_index = 1
        ordered = day07.getBestHand(hands, card_index)
        self.assertEqual(len(ordered), 2)

        hands = ['QQQQ7', 'Q4444', 'K4KKK', 'AA4AA', 'A4444']
        card_index = 0
        ordered = day07.getBestHand(hands, card_index)
        self.assertEqual(ordered, ['AA4AA', 'A4444'])

        hands = ['AA4AA', 'A4444']
        card_index = 1
        ordered = day07.getBestHand(hands, card_index)
        self.assertEqual(ordered, ['AA4AA'])

    def test_orderHands(self):
        hands = ['2AAAA', '33332']
        ordered = day07.orderHands(hands)
        self.assertEqual(ordered, ['33332', '2AAAA'])

        hands = ['A22KK', 'A2345']
        ordered = day07.orderHands(hands)
        self.assertEqual(ordered, ['A2345', 'A22KK'])
        
        hands = ['T55J5','QQQJA']
        ordered = day07.orderHands(hands)
        self.assertEqual(ordered, ['QQQJA', 'T55J5'])

        hands = ['TTTTT','TTTTT']
        ordered = day07.orderHands(hands)
        self.assertEqual(ordered, ['TTTTT', 'TTTTT'])

        hands = ['77888','77788']
        ordered = day07.orderHands(hands)
        self.assertEqual(ordered, ['77888', '77788'])

        hands = ['KK677','KTJJT']
        ordered = day07.orderHands(hands)
        self.assertEqual(ordered, ['KK677', 'KTJJT'])

        hands = ['QQQQ7', 'Q4444', 'K4KKK', 'AA4AA', 'A4444']
        ordered = day07.orderHands(hands)
        self.assertEqual(ordered, ['AA4AA', 'A4444', 'K4KKK', 'QQQQ7', 'Q4444'])

    def test_rankHands(self):
        input_hands = [['32T3K', '765'], ['T55J5', '684'], ['KK677', '28'], ['KTJJT', '220'], ['QQQJA', '483']]
        ranked_hands = day07.rankHands(input_hands)
        expected = ['QQQJA', 'T55J5', 'KK677', 'KTJJT', '32T3K']
        self.assertEqual(ranked_hands, expected)

    def test_scoreHands(self):
        input_hands = [['32T3K', '765'], ['T55J5', '684'], ['KK677', '28'], ['KTJJT', '220'], ['QQQJA', '483']]
        ranked_hands = ['QQQJA', 'T55J5', 'KK677', 'KTJJT', '32T3K'] 
        score = day07.scoreHands(input_hands, ranked_hands)
        self.assertEqual(score, 6440)
