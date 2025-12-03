#! usr/bin/env python

def getInputs(filename):
    with open(filename) as f:
        banks = [[int(y) for y in list(x.strip())] for x in f]
        return banks

def getLargestBatteries(bank, safety_override=False):
    largest = []
    batteries_to_find = 12 if safety_override else 2
    remainder = bank.copy()
    while batteries_to_find > 0:
        scope = len(remainder) - batteries_to_find + 1
        max_index = remainder.index(max(remainder[:scope]))
        largest.append(remainder[max_index])
        remainder = remainder[max_index+1:]
        batteries_to_find -= 1

    joltage = int(''.join([str(x) for x in largest]))
    return joltage

def getTotalJoltage(banks, safety_override=False):
    joltage = 0
    for bank in banks:
        joltage += getLargestBatteries(bank, safety_override)

    return joltage

if __name__ == '__main__':
    filename = 'input03.txt'
    banks = getInputs(filename)
    total_output_joltage = getTotalJoltage(banks)
    print(f'Part 1: {total_output_joltage}')

    safety_override=True
    total_output_joltage = getTotalJoltage(banks, safety_override)
    print(f'Part 2: {total_output_joltage}')
