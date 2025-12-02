#! usr/bin/python3

def openfile (filename):
    expenseReport = []
    with open(filename) as f:
        expenseReport = [int(line.strip()) for line in f]
        
    return expenseReport

def findSum(entries):
    for entry in entries:
        first = entry
        second = 2020-entry
        checkEntries = entries.copy()
        checkEntries.remove(first)

        if second in checkEntries:
            return first * second

report = openfile('input1.txt')
answer = findSum(report)
print(answer)
