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

xmasFile = openfile('input9.txt')
invalidNumber = findInvalidNumber(xmasFile)
print(invalidNumber)
