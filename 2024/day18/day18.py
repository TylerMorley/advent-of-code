#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        return [[int(y) for y in x.strip().split(',')] for x in f]

def corruptSpace(size, falling_bytes, num_fallen):
    width, height = size
    space = [['.' for y in range(width)] for x in range(height)]
    for i in range(num_fallen):
        x,y = falling_bytes[i]
        space[y][x] = '#'
    return space

def getNeighbors(location, size):
    neighbors = []
    height, width = size
    x,y = location

    if x-1 >= 0:
        neighbors.append([x-1, y])
    if x+1 < width:
        neighbors.append([x+1, y])
    if y-1 >= 0:
        neighbors.append([x, y-1])
    if y+1 < height:
        neighbors.append([x, y+1])

    return neighbors

def heatMap(space, location, distance):
    x,y = location
    if space[y][x] != '.':
        return space

    space[y][x] = distance
    size = [len(space), len(space[0])]
    neighbors = getNeighbors(location, size)

    distance += 1
    for neighbor in neighbors:
        value = space[neighbor[1]][neighbor[0]]
        if value == '.' or (type(value) == int and value > distance):
            space = heatMap(space, neighbor, distance)
    return space
