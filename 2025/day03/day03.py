#! usr/bin/env python

def getInputs(filename):
    with open(filename) as f:
        banks = [[int(y) for y in list(x.strip())] for x in f]
        return banks

def getLargestBatteries(bank):
    largest = []
    largest.append(max(bank))
    max_index = bank.index(max(bank))
    remainder = bank[max_index+1:]
    if len(remainder) > 0:
        largest.append(max(remainder))
    else:
        remainder = bank.copy()
        remainder.pop(max_index)
        largest = [max(remainder)] + largest

    joltage = int(str(largest[0]) + str(largest[1]))
    return joltage

def getTotalJoltage(banks):
    joltage = 0
    for bank in banks:
        joltage += getLargestBatteries(bank)

    return joltage

if __name__ == '__main__':
    filename = 'input03.txt'
    banks = getInputs(filename)
    total_output_joltage = getTotalJoltage(banks)
    print(f'Part 1: {total_output_joltage}')
