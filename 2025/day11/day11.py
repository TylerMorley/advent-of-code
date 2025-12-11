#! usr/bin/env python

def getInputs(filename):
    with open(filename) as f:
        lines = [x.strip().split(' ') for x in f]
        racks = {x[0][:-1]:x[1:] for x in lines}
        return racks

def getPaths(racks, location):
    if location == 'out':
        return 1
    else:
        num_paths = sum([getPaths(racks, x) for x in racks[location]])
        return num_paths

if __name__ == '__main__':
    racks = getInputs('input11.txt')
    start = 'you'
    num_paths = getPaths(racks, start)
    print(f'Part 1: {num_paths}')
