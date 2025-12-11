#! usr/bin/env python
import operator
import functools

def getInputs(filename):
    with open(filename) as f:
        lines = [x.strip().split(' ') for x in f]
        racks = {x[0][:-1]:x[1:] for x in lines}
        return racks

def getPaths(racks, location, target):
    if location == target:
        return 1
    elif location == 'out':
        return 0
    else:
        num_paths = sum([getPaths(racks, x, target) for x in racks[location]])
            
        return num_paths

def getPathsQuick(racks, location, target, mem):
    if location+target in mem:
        return mem[location+target]
    elif location == target:
        return 1
    elif location == 'out':
        return 0
    else:
        num_paths = sum([getPathsQuick(racks, x, target, mem) for x in racks[location]])
        mem[location+target] = num_paths
        return num_paths

def getPathsDF(racks):
    second = third = None
    if getPaths(racks, 'dac','fft') == 0:
        second,third = ['fft','dac']
    elif getPaths(racks,'fft','dac') == 0:
        second,third = ['dac','fft']
    else:
        print(f'ERROR - both middles lead to each other')

    segments = [['svr',second],[second,third],[third,'out']]
    num_paths = []
    mem = dict()
    for segment in segments:
        start,end = segment
        num_paths.append(getPathsQuick(racks, start, end, mem))

    return functools.reduce(operator.mul, num_paths)

if __name__ == '__main__':
    racks = getInputs('input11.txt')
    start = 'you'
    end = 'out'
    num_paths = getPaths(racks, start, end)
    print(f'Part 1: {num_paths}')

    num_df_paths = getPathsDF(racks)
    print(f'Part 2: {num_df_paths}')
