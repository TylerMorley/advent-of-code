#! usr/bin/python

def buildSchematic(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

def getNumbers(schematic):
    numbers = []
    for row in schematic:
        numbers += (getRowNumbers(row))
    return numbers

def getRowNumbers(row):
    numbers = []
    untrimmed_nums = [x for x in row.split('.') if x]
    for num in untrimmed_nums:
        num = ''.join([x for x in num if x.isdigit()])
        if num:
             numbers.append(num)
    return numbers

def getPartNumbers(schematic, numbers):
    partNumbers = []
    for num in numbers:
        if(isPartNumber(schematic, num)):
            partNumbers.append(num)
    return partNumbers

def isPartNumber(schematic, num):
    to_check = []
    partNumbers = []
    for i in range(len(schematic)):
        row = schematic[i]
        if num in row:
            to_check = getNumsToCheck(schematic, i, num)
            if hasSymbol(schematic, to_check):
                partNumbers.append(num)
    return partNumbers

def getNumsToCheck(schematic, i, num):
    to_check = []
    row = schematic[i]
    j = row.index(num)
    end = j + len(num) -1

    to_check += [[i-1, j-1], [i, j-1], [i+1, j-1],
                 [i, end+1], [i-1, end+1], [i+1, end+1]
                 ]
    for k in range(j, end + 1):
        to_check.append([i-1, k])
    for k in range(j, end + 1):
        to_check.append([i+1, k])
    return to_check

def hasSymbol(schematic, locations):
    for location in locations:
        i = location[0]
        j = location[1]
        try:
            value = schematic[i][j]
            if not value.isdigit() and value != '.':
                return True
        except IndexError as e:
            e = 'dont worry'
    return False

filename = 'inputs/input03.txt'
schematic = buildSchematic(filename)
numbers_to_check = getNumbers(schematic)
part_numbers = getPartNumbers(schematic, numbers_to_check)
score = sum([int(x) for x in part_numbers])
#562984 is too high
print(f'part one: {score}')
