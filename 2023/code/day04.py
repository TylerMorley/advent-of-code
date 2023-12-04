#! usr/bin/python
from math import floor

def getCards(filename):
    with open(filename) as f:
        lines = [x.strip()[x.index(':')+2:].split(' | ') for x in f]
        cards = []
        for line in lines:
            winners = line[0].strip().replace('  ', ' ').split(' ')
            havers = line[1].strip().replace('  ', ' ').split(' ')
            cards.append([winners, havers])

        return cards

def getWinners(card):
    winning_nums = set(card[0])
    nums_you_have = set(card[1])
    return list(winning_nums & nums_you_have)

def getAllWinners(cards):
    winners_list = []
    for card in cards:
        winners_list.append(getWinners(card))
    return winners_list

def getScore(winners):
    return floor(2**(len(winners)-1))

def getScores(winners_list):
    score = 0
    for card in winners_list:
        score += getScore(card)
    return score

def checkCard(stacks, card, stack_index):
    num_new_cards = len(getWinners(card))
    starting_pos = stack_index + 1
    for i in range(starting_pos, starting_pos+num_new_cards):
        multiplier = stacks[stack_index]
        stacks[i] += multiplier
    return stacks

def checkCards(cards):
    stacks = [1]*len(cards)
    for i in range(len(cards)):
        stacks = checkCard(stacks, cards[i], i)
    return sum(stacks)

filename = 'inputs/input04.txt'
cards = getCards(filename)
winners = getAllWinners(cards)
score = getScores(winners)
print(f'Part 1: {score}')

score2 = checkCards(cards)
print(f'Part 2: {score2}')
