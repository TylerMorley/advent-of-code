#! usr/bin/python

def getHands(filename):
    with open(filename) as f:
        hands = [x.strip().split(' ') for x in f]
        for hand in hands:
            hand[1] = int(hand[1])
        return hands

def isOfAKind(hand):
    for char in hand:
        num_copies = hand.count(char)
        if num_copies == 5:
            return 'five'
        elif num_copies == 4:
            return 'four'
        elif num_copies == 3:
            rest = hand.replace(char, '')
            if isOfAKind(rest) == 'pair':
                return 'full'
            else:
                return 'three'
        elif num_copies == 2:
            rest = hand.replace(char, '')
            other_kinds = isOfAKind(rest)
            if other_kinds == 'three':
                return 'full'
            elif other_kinds == 'pair':
                return 'two pair'
            else:
                return 'pair'
    return 'high'

def categorize(uncat_hands):
    hands = {'five': [], 'four': [], 'full': [], 'three': [], 'two pair': [], 'pair': [], 'high': []}
    for hand in uncat_hands:
        category = isOfAKind(hand[0])
        hands[category].append(hand)
    return hands

def getBestHand(hands, card_index):
    card_value = {'A':13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1, '1':0}
    first = ['11111']
    for hand in hands:
        hand_value = card_value[hand[card_index]]
        first_value = card_value[first[0][card_index]]
        if hand_value > first_value:
            first = [hand]
        elif hand_value == first_value:
            first.append(hand)
    return first

def orderHands(u_hands):
    unordered_hands = u_hands.copy()
    if len(unordered_hands) < 2:
        return unordered_hands

    current_best = unordered_hands
    ordered_hands = []
    i = 0
    while len(current_best) > 0:
        best = getBestHand(current_best, i)
        if len(best) == 1:
            ordered_hands.append(best[0])
            current_best.remove(best[0])
            i = 0
            
        else:
            for card in best:
                current_best.remove(card)
            current_best = best + current_best
            i += 1
            if i > 4:
                print(f'same card: {u_hands}')
                return u_hands

    return ordered_hands

def rankHands(input_hands):
    ranked_hands = []
    categorized_hands = categorize(input_hands)
    categories = ['five', 'four', 'full', 'three', 'two pair', 'pair', 'high']
    for category in categories:
        rankless_hands = [x[0] for x in categorized_hands[category]]
        ranked_hands += orderHands(rankless_hands)

    return ranked_hands

def scoreHands(input_hands, ranked_hands):
    hands_and_bets = dict()
    for hand in input_hands:
        hands_and_bets[hand[0]] = hand[1]

    score = 0
    hands = ranked_hands.copy()
    hands.reverse()
    for i in range(len(hands)):
        hand = hands[i]
        bet = hands_and_bets[hand]
        score += int(bet) * (i + 1)
    return score

if __name__ == '__main__':
    filename = 'inputs/input07.txt'
    input_hands = getHands(filename)
    ranked_hands = rankHands(input_hands)
    score = scoreHands(input_hands, ranked_hands)
    print(f'Part 1: {score}')
    # Too high 253934202
