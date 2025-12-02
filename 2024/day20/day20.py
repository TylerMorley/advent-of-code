#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

def getStart(racetrack):
    start = []
    for i in range(len(racetrack)):
        row = racetrack[i]
        if 'S' in row:
            ind_s = row.index('S')
            start = [ind_s, i]
    return start

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

def runRace(racetrack):
    location = getStart(racetrack)
    track_size = [len(racetrack[0]), len(racetrack)]
    path = []
    
    while racetrack[location[1]][location[0]] != 'E':
        path.append(location)
        options = getNeighbors(location, track_size)
        options = [x for x in options if racetrack[x[1]][x[0]] != '#']
        options = [x for x in options if x not in path]
        if len(options) == 1:
            location = options[0]
        else:
            print(f'Wrong number of options: {options}')
            print(f'Path: {path}')
    
    return len(path)

'''
For the cheating, make a list of locations that surround the path.
Clear away any that are on the edge of the racetrack.
Clear away any that have no new '.' neighbors.
It might open up some pathing choices - always choose the cheat path?
'''
