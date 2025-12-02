#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f]
        program = lines.pop().removeprefix('Program: ').split(',')
        program = [int(x) for x in program]
        
        register = [x.split(': ') for x in lines[:-1]]
        for reg in register:
            reg[1] = int(reg[1])
        
        return [register, program]
