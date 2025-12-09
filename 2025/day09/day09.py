#! usr/bin/env python

def getInputs(filename):
    with open(filename) as f:
        return [[int(y) for y in x.strip().split(',')] for x in f]

def calcArea(corners):
    x1,y1 = corners[0]
    x2,y2 = corners[1]
    width = abs(x1-x2) + 1
    height = abs(y1-y2) + 1
    return height * width

def findBiggestRect(red_tiles):
    unpaired = red_tiles.copy()
    pairs = []
    while len(unpaired) > 1:
        cur_tile = unpaired.pop(0)
        pairs += [[cur_tile,x] for x in unpaired]
    areas = [calcArea(pair) for pair in pairs]
    return max(areas)

if __name__ == '__main__':
    red_tiles = getInputs('input09.txt')
    max_area = findBiggestRect(red_tiles)
    print(f'Part 1: {max_area}')
