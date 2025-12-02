#! usr/bin/python3

def openfile (filename):
    expenseReport = []
    with open(filename) as f:
        expenseReport = [int(line.strip()) for line in f]
        
    return expenseReport

def findTwoNumbers(entries, target):
    for entry in entries:
        second = entry
        third = target - second
        checkEntries = entries.copy()
        checkEntries.remove(second)

        if third in checkEntries:
            return second * third

    return None

def findThreeNumbers(entries):
    for entry in entries:
        first = entry
        target = 2020 - entry
        checkEntries = entries.copy()
        checkEntries.remove(first)

        attempt = findTwoNumbers(checkEntries, target)
        if attempt:
            return first * attempt
    return 'Found Nothing'
        
report = openfile('input1.txt')
answer = findThreeNumbers(report)
print(answer)
