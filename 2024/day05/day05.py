# usr/bin/env python
import math

def getInputs(filename):
    with open(filename) as f:
        rules, updates = [x for x in f.read().strip().split('\n\n')]
        rules = [[int(y) for y in x.split('|')] for x in rules.split('\n')]
        updates = [[int(y) for y in x.split(',')] for x in updates.split('\n')]

        return [rules, updates]

def checkRule(rule, update):
    try:
        before = update.index(rule[0])
        after = update.index(rule[1])
    except ValueError:
        return True
    return before < after

def checkRules(rules, update):
    isOrdered = True
    for rule in rules:
        if not checkRule(rule, update):
            isOrdered = False

    return isOrdered

def middlePages(updates):
    score = 0
    for update in updates:
        middle = math.ceil(len(update)/2) - 1
        score += update[middle]

    return score

def applyRule(rule, update):
    target = update.index(rule[1])
    value = update.pop(target)
    destination = update.index(rule[0]) + 1
    update.insert(destination, value)

    return update

def applyRules(rules, update):
    for rule in rules:
        if not checkRule(rule, update):
            update = applyRule(rule, update)
    return update

def divideByRules(rules, updates):
    ordered = []
    unordered = []
    for update in updates:
        if checkRules(rules, update):
            ordered.append(update)
        else:
            unordered.append(update)

    return [ordered, unordered]

def reorderUpdates(rules, unordered):
    reordered = []
    for update in unordered:
        while not checkRules(rules, update):
            update = applyRules(rules, update)
        reordered.append(update)
        
    return reordered

if __name__ == '__main__':
    filename = 'input05.txt'
    rules, updates = getInputs(filename)
    ordered, unordered = divideByRules(rules, updates)
    score = middlePages(ordered)
    print(f'Part 1: {score}')

    reordered = reorderUpdates(rules, unordered)
    score = middlePages(reordered)
    print(f'Part 2: {score}')
