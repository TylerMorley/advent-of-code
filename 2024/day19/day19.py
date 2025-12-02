#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f]
        patterns = lines[0].split(', ')
        designs = lines[2:]
        return [patterns, designs]

def buildDesign(patterns, design, record, count_all=False):
    if len(design) == 0:
        return 1
    candidates = [x for x in patterns if design[:len(x)] == x]
    if len(candidates) == 0:
        return 0
    if design in record:
        return record[design]

    count = 0
    for candidate in candidates:
        leftover = design[len(candidate):]
        num = buildDesign(patterns, leftover, record)
        count += num
        record[design] = count

    return count

def findPossible(patterns, designs, count_all=False):
    count = 0
    for design in designs:
        record = dict()
        if count_all:
            count += buildDesign(patterns, design, record, count_all)
        elif buildDesign(patterns, design, record, count_all):
            count += 1

    return count

if __name__ == '__main__':
    filename = 'input19.txt'
    patterns, designs = getInput(filename)
    score = findPossible(patterns, designs)
    print(f'Part 1: {score}')

    count_all = True
    score = findPossible(patterns, designs, count_all)
    print(f'Part 2: {score}')
