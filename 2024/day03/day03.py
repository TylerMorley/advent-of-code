#! usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        return f.read().strip()

def isInstruction(candidate):
    if candidate.count(',') != 1:
        return False
    if ' ' in candidate:
        return False
    first, last = candidate.split(',')
    if first[:4] != 'mul(':
        return False
    try:
        int(first[4:])
    except ValueError:
        return False
    try:
        int(last[:-1])
    except ValueError:
        return False
    if last[-1] != ')':
        return False
    return True

def findUncorrupted(memory):
    if 'mul' not in memory:
        return [None, None]

    start = memory.find('mul(')
    end = memory.find(')', start + 4)
    candidate = memory[start:end+1]

    if isInstruction(candidate):
        return [candidate, memory[end+1:]]
    else:
        return [None, memory[start+4:]]

def multiplyNums(instruction):
    first, last = instruction.removeprefix('mul(').removesuffix(')').split(',')
    return int(first) * int(last)

def getUncorruptedInstructions(memory, checkEnabled=False):
    leftover = memory
    product = 0
    while leftover is not None:
        if checkEnabled:
            leftover = eliminateDont(leftover)
        instruction, leftover = findUncorrupted(leftover)
        if instruction is not None:
            product += multiplyNums(instruction)

    return product

def eliminateDont(memory):
    mul = memory.find('mul(')
    dont = memory.find('don\'t()')

    while mul > dont and dont >= 0:
        do = memory[dont+1:].find('do()')
        memory = memory[dont+do+5:]
        mul = memory.find('mul(')
        dont = memory.find('don\'t')

    return memory

if __name__ == '__main__':
    filename = 'input03.txt'
    memory = getInput(filename)
    memory2 = memory
    product = getUncorruptedInstructions(memory)
    print(f'Part 1: {product}')

    checkEnabled = True
    product = getUncorruptedInstructions(memory2, checkEnabled)
    print(f'Part 2: {product}')
