#! usr/bin/python

def getInputs(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

def replaceSpelledNums(line):
    ones = line.replace('one', 'o1e') 
    twos = ones.replace('two', 't2o')
    threes = twos.replace('three', 't3e')
    fours = threes.replace('four', 'f4r')
    fives = fours.replace('five', 'f5e')
    sixes = fives.replace('six', 's6x')
    sevens = sixes.replace('seven', 's7n')
    eights = sevens.replace('eight', 'e8t')
    nines = eights.replace('nine', 'n9e')
    final = nines.replace('zero', 'z0o')

    return final

def getCalibrationValue(input):
    digit_list = [x for x in input if x.isdigit()]
    cal_value = int(''.join(digit_list[0] + digit_list[-1]))
    return cal_value

def getSum(document):
    values = []
    for docline in document:
        values.append(getCalibrationValue(docline))

    return sum(values)

filename = 'inputs/input01.txt'
document = getInputs(filename)
part_one = getSum(document)
print(f'part one: {part_one}')

replaced = [replaceSpelledNums(x) for x in document]
part_two = getSum(replaced)
print(f'part two: {part_two}')
