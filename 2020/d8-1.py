#! usr/bin/python3

def openfile(filename):
    with open(filename) as f:
        instructions = [line.strip() for line in f]
        return instructions
    
def runProgram(instructions):
    index = 0
    accumulator = 0
    indexTracker = set()
    infiniteLoopFound = False

    while not infiniteLoopFound:
        accMod, indexMod = execute(instructions[index])

        accumulator += accMod
        indexTracker.update([index])
        newIndex = index + indexMod

        if newIndex in indexTracker:
            infiniteLoopFound = True
        else:
            index = newIndex
            
    return accumulator

def execute(instruction):
    operation, argument = [x.strip() for x in instruction.split(' ')]
    argument = int(argument.replace('+', ''))
    
    if operation == 'nop':
        return [0, 1]

    elif operation == 'acc':
        return [argument, 1]

    elif operation == 'jmp':
        return [0, argument]
        
instructions = openfile('example8.txt')
accFinalValue = runProgram(instructions)
print(accFinalValue)
