#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        return [list(x.strip()) for x in f]

def getNeighbors(location, height, width):
    y,x = location
    neighbors = []
    if x > 0:
        neighbors.append([y, x-1])
    if y > 0:
        neighbors.append([y-1, x])
    if x < width - 1:
        neighbors.append([y, x+1])
    if y < height - 1:
        neighbors.append([y+1, x])

    return neighbors

def addPlot(record, plot):
    plant, location = plot
    if plant not in record:
        record.update({plant:[location]})
    else:
        record[plant].append(location)
    return record

def updatePerimeter(neighbors, plots):
    num_regional_neighbors = len([x for x in neighbors if x in plots])
    if len(plots) == 0:
        return 4
    elif num_regional_neighbors == 0:
        return 0
    elif num_regional_neighbors == 1:
        return 2
    elif num_regional_neighbors == 2:
        return 0
    elif num_regional_neighbors == 3:
        return -2
    elif num_regional_neighbors == 4:
        return -4
    else:
        print(num_regional_neighbors)

def updateRegion(garden, record, location):
    neighbors = getNeighbors(location, len(garden), len(garden[0]))
    record['perimeter'] += updatePerimeter(neighbors, record['plots'])
    record['plots'].append(location)
    y,x = location
    garden[y][x] = '.'

    new_locs = []
    for plot in neighbors:
        y,x = plot
        if garden[y][x] == record['type']:
            new_locs.append(plot)
    return [garden, record, new_locs]

def findNewRegion(garden):
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if garden[i][j] != '.':
                return [i,j]
    return None

def mapRegion(garden, start):
    y,x = start
    p_type = garden[y][x]
    record = {'type':p_type, 'plots':[], 'perimeter':0}
    to_check = [start]

    while len(to_check) > 0:
        loc = to_check.pop(0)
        garden, record, new_to_check = updateRegion(garden, record, loc)
        to_add = [x for x in new_to_check if x not in to_check]
        to_add = [x for x in to_add if x not in record['plots']]
        to_check += to_add
    return record

def calculateFencing(garden):
    score = 0
    region = dict()
    next_region = findNewRegion(garden)
    while next_region != None:
        region = mapRegion(garden, next_region)
        score += region['perimeter'] * len(region['plots'])
        next_region = findNewRegion(garden)
    return score

if __name__ == '__main__':
    filename = 'input12.txt'
    garden = getInput(filename)
    score = calculateFencing(garden)
    print(f'Part 1: {score}')
