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

    #Keep looking for infinite loop. If found, return False.
    #Also look for an index of len(instructions) - return acc then.
    while not infiniteLoopFound:
        # print(instructions)
        # print(f'index: {index}')
        accMod, indexMod = execute(instructions[index])

        accumulator += accMod
        indexTracker.update([index])
        newIndex = index + indexMod

        if newIndex == len(instructions):
            return [True, accumulator]
        
        if newIndex in indexTracker:
            infiniteLoopFound = True
        else:
            index = newIndex
            
    return [False, accumulator]

def execute(instruction):
    operation, argument = [x.strip() for x in instruction.split(' ')]
    # print(f'operation: {operation}')
    argument = int(argument.replace('+', ''))
    
    
    if operation == 'nop':
        return [0, 1]

    elif operation == 'acc':
        return [argument, 1]

    elif operation == 'jmp':
        return [0, argument]

def runPrograms(instructions):
    for index in range(0, len(instructions)-1):
        modifiedInstr = modify(instructions, index)
        isRepaired, accumulator = runProgram(modifiedInstr)

        if isRepaired:
            return accumulator

    print('Found Nothing.')

def modify(instructions, index):
    modifiedInstructions = instructions.copy()
    instruction = modifiedInstructions[index]
    operation, argument = instruction.split(' ')
    newOperation = ''
    
    if operation == 'nop':
        newOperation = 'jmp'

    elif operation == 'jmp':
        newOperation = 'nop'

    elif operation == 'acc':
        newOperation = 'acc'

    newInstruction = newOperation + ' ' + argument
    modifiedInstructions[index] = newInstruction

    return modifiedInstructions
        
instructions = openfile('input8.txt')
accFinalValue = runPrograms(instructions)
print(accFinalValue)
