#! usr/bin/python3

import queue

def openfile(filename):
    with open(filename) as f:
        return [int(line.strip()) for line in f]

def findInvalidNumber(xmasFile):
    cypher, nextNumbers = initializeCypher(xmasFile)

    for number in nextNumbers:
        isValid = testNumberValidity(cypher, number)
        if not isValid:
            return number
        else:
            cypher.pop(0)
            cypher.append(number)

    print('None found.')

def initializeCypher(xmasFile):
    preamble = xmasFile[:25]
    nextNumbers = xmasFile[25:]
    # preamble = xmasFile[:5]
    # nextNumbers = xmasFile[5:]

    cypher = preamble
    
    return [cypher, nextNumbers]

def testNumberValidity(cypher, number):
    isValid = False
    
    for i in cypher:
        copyCypher = cypher.copy()
        copyCypher.remove(i)

        for j in copyCypher:
            if i + j == number:
                isValid = True
    return isValid

def findWeakness(xmasFile, invalidNumber):
    for i in range(0, len(xmasFile)):
        foundWeakness, contiguousSet = checkForWeakness(xmasFile, invalidNumber, i)
        if foundWeakness:
            weakness = calculateWeakness(contiguousSet)
            return weakness

    print('Found no weakness.')

def calculateWeakness(contiguousSet):
    weakness = max(contiguousSet) + min(contiguousSet)
    return weakness

def checkForWeakness(xmasFile, invalidNumber, startPoint):
    currentSum = 0
    currentSet = []
    index = startPoint
    while currentSum < invalidNumber:
        currentSum += xmasFile[index]
        currentSet.append(xmasFile[index])
        
        if currentSum == invalidNumber:
            return [True, currentSet]

        index += 1
        
    return [False, []]

xmasFile = openfile('input9.txt')
invalidNumber = findInvalidNumber(xmasFile)
print(f'invalidNumber: {invalidNumber}')
weakness = findWeakness(xmasFile, invalidNumber)
print(f'weakness: {weakness}')
