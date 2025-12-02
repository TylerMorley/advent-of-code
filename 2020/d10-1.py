#! usr/bin/python3

def openfile(filename):
    with open(filename) as f:
        adapterList = [int(line.strip()) for line in f]
        return adapterList

def organize(adapterList):
    outlet = 0
    adapterList.append(outlet)
    device = max(adapterList) + 3
    adapterList.append(device)
    
    adapterList.sort()

    return adapterList
    
def calculateJoltage(orderedAdapters):
    nextAdapter = None
    oneJoltDiff = 0
    threeJoltDiff = 0
    
    for i in range(0, len(orderedAdapters) - 1):
        adapter = orderedAdapters[i]
        nextAdapter = orderedAdapters[i+1]
        joltageDiff = nextAdapter - adapter
        
        if joltageDiff == 1:
            oneJoltDiff +=1
        elif joltageDiff == 3:
            threeJoltDiff += 1
        
    print(f'one: {oneJoltDiff}, three: {threeJoltDiff}')
    return (oneJoltDiff * threeJoltDiff)

adapterList = openfile('input10.txt')
organizedAdapters = organize(adapterList)
joltage = calculateJoltage(organizedAdapters)
print(joltage)
