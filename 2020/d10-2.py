#! usr/bin/python3

def openfile(filename):
    with open(filename) as f:
        adapterList = [int(line.strip()) for line in f]
        adapterList.sort()
        return adapterList

def segmentate (adapterList):
    segmented_list = []
    segment = []
    next_adapter = None
    for i in range(0, len(adapterList) - 1):
        adapter = adapterList[i]
        next_adapter = adapterList[i+1]
        joltageDiff = next_adapter - adapter

        segment.append(adapter)
        if joltageDiff == 3:
            segment.append(next_adapter)
            segmented_list.append(segment)
            segment = []

    if len(segment) > 0:
        segment.append(next_adapter)
        segmented_list.append(segment)

    return segmented_list

def calculate_segmented_joltage(seg_adapter_list):
    total = 1
    for segment in seg_adapter_list:
        subtotal = calculateJoltage(segment, segment[0], True) + 1
        total *= subtotal

    return total

def calculateJoltage(adapter_list, adapter, isMain):
    count = 0

    if adapter == max(adapter_list):
        return count

    choices = [a for a in adapter_list if (a > adapter and a <= (adapter + 3))]
    
    if len(choices) == 1:
        choice = choices[0]
        if choice == (adapter + 3) and not isMain:
            return count
        else:
            count += calculateJoltage(adapter_list, choice, isMain)

    else:
        mainChoice = choices.pop(0)
        count += calculateJoltage(adapter_list, mainChoice, isMain)
        
        for choice in choices:
            count += 1
            count += calculateJoltage(adapter_list, choice, isMain)

    return count

adapterList = openfile('input10.txt')
charger = max(adapterList) + 3
outlet = 0
adapterList.insert(outlet, 0)

segmented_adp_list = segmentate(adapterList)
joltage = calculate_segmented_joltage(segmented_adp_list)

print(joltage)
