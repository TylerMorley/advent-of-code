#! usr/bin/env python

def getInputs(filename):
    with open(filename) as f:
        ranges = f.read().split(',')
        ranges = [[int(y) for y in x.split('-')] for x in ranges]
        return ranges

def isValid(num):
    if len(str(num))%2 != 0:
        return True

    else:
        number = str(num)
        midpoint = len(number)//2
        first = number[:midpoint]
        last = number[midpoint:]
        if first == last:
            return False
        else:
            return True

def checkSequence(sequence, remainder):
    if sequence == remainder:
        return True

    next_index = len(sequence)
    next_part = remainder[:next_index]
    if sequence == next_part:
        return checkSequence(sequence, remainder[next_index:])
    else:
        return False

def isValid2(num):
    number = str(num)
    midpoint = len(number)//2
    for i in range(1, midpoint+1):
        #if len(number)%i > 0 continue
        sequence = number[:i]
        remainder = number[i:]
        if checkSequence(sequence, remainder):
            return False
    return True


def findInvalidIds(id_range, use_silly_patterns=False):
    start,end = id_range
    invalid_nums = []
    for i in range(start, end+1):
        if (use_silly_patterns and not isValid2(i)) or (not use_silly_patterns and not isValid(i)):
            invalid_nums.append(i)

    return invalid_nums

def sumInvalidIds(id_ranges, use_silly_patterns=False):
    invalid_nums = set()
    for id_range in id_ranges:
        invalid_in_range = findInvalidIds(id_range, use_silly_patterns)
        for num in invalid_in_range:
            invalid_nums.add(num)

    return sum(invalid_nums)

if __name__ == '__main__':
    filename = 'input02.txt'
    id_ranges = getInputs(filename)
    invalid_sum = sumInvalidIds(id_ranges)
    print(f'Part 1: {invalid_sum}')

    use_silly_patterns = True
    invalid_sum2 = sumInvalidIds(id_ranges, use_silly_patterns)
    print(f'Part 2: {invalid_sum2}')
