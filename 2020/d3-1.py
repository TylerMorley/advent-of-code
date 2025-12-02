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

def applySlope(usableMap):
    treeCount = 0
    slope = [3,1]
    currentPosX = 0
    currentPosY = 0
    # print(len(usableMap) -1)
    while currentPosY < (len(usableMap) - 1):
        print(f'X: {currentPosX}, Y: {currentPosY}')
        if usableMap[currentPosY][currentPosX] == '#':
            treeCount += 1
        currentPosX = (currentPosX + slope[0]) % (len(usableMap[0]) - 1)
        currentPosY += slope[1]

    if usableMap[currentPosY][currentPosX] == '#':
        treeCount += 1
    return treeCount

rawMap = openfile('input3.txt')
usableMap = organize(rawMap)
numTreesHit = applySlope(usableMap)
print(numTreesHit)
