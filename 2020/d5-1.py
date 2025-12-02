#! usr/bin/python3

def openfile(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def translate(passList):
    seatIDs = []
    for bPass in passList:
        binaryString = lettersToBinary(bPass)
        seatID = binaryToDecimal(binaryString)
        seatIDs.append(seatID)

    return seatIDs
        
def lettersToBinary(letters):
    numbers = letters.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')

    return numbers

def binaryToDecimal(binaryString):
    decimal = 0
    binaryList = [int(x) for x in binaryString]
    
    power = 0
    for index in range(len(binaryList) - 1, -1, -1):
        decimal += binaryList[index] * (2**power)
        power += 1

    return decimal

nearbyPasses = openfile('input5.txt')
seatIDs = translate(nearbyPasses)
print(seatIDs)
highestSeatID = max(seatIDs)
print(highestSeatID)
