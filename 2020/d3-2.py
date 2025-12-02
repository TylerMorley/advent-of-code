#! usr/bin/python3

def openfile(filename):
    mapfile = []
    with open(filename) as f:
        mapfile = [line for line in f]

    return mapfile

def organize(rawMap):
    listMap = listify(rawMap)
    repeatingMap = wrapper(listMap)

    return repeatingMap

def listify(rawMap):
    listMap = []
    for line in rawMap:
        row = list(line)
        listMap.append(row)

    return listMap

def wrapper(listMap):
    #TODO: Put the modular here
    return listMap

def applySlope(usableMap, slope):
    treeCount = 0
    currentPosX = 0
    currentPosY = 0

    while currentPosY < (len(usableMap) - 1):
        if usableMap[currentPosY][currentPosX] == '#':
            treeCount += 1
        currentPosX = (currentPosX + slope[0]) % (len(usableMap[0]) - 1)
        currentPosY += slope[1]

    if usableMap[currentPosY][currentPosX] == '#':
        treeCount += 1
    return treeCount

def applySlopes(usableMap, slopes):
    treeCounts = []
    for slope in slopes:
        treeCounts.append(applySlope(usableMap, slope))

    return treeCounts

def multiply(treeCounts):
    product = 1
    for num in treeCounts:
        product = product * num

    return product

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

rawMap = openfile('input3.txt')
usableMap = organize(rawMap)
numTreesHit = applySlopes(usableMap, slopes)
product = multiply(numTreesHit)
print(product)
