#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

def findTrailheads(top_map):
    trailheads = []
    for i in range(len(top_map)):
        x_values = [x for x,val in enumerate(top_map[i]) if val == '0']
        trailheads += [[i,x] for x in x_values]

    return trailheads

def getAdjacent(height, width, location):
    neighbors = []
    y,x = location

    if x-1 >= 0:
        neighbors.append([y, x-1])
    if x+1 < width:
        neighbors.append([y, x+1])
    if y-1 >= 0:
        neighbors.append([y-1, x])
    if y+1 < height:
        neighbors.append([y+1, x])

    return neighbors


def countCompleteTrails(top_map, location, count_distinct=False):
    summits = []
    y,x = location
    elevation = top_map[y][x]
    
    if elevation == '9':
        return [location]
    
    height = len(top_map)
    width = len(top_map[0])
    neighbors = getAdjacent(height, width, location)
    
    uphill = str(int(top_map[y][x]) + 1)
    candidates = [n for n in neighbors if top_map[n[0]][n[1]] == uphill]
    for cand in candidates:
        new_summits = countCompleteTrails(top_map, cand, count_distinct)
        if count_distinct:
            summits += new_summits
        else:
            summits += [s for s in new_summits if s not in summits]

    return summits

def getMapScore(top_map, count_distinct=False):
    score = 0
    trailheads = findTrailheads(top_map)
    for th in trailheads:
        score += len(countCompleteTrails(top_map, th, count_distinct))

    return score

if __name__ == '__main__':
    filename = 'input10.txt'
    top_map = getInput(filename)
    score = getMapScore(top_map)
    print(f'Part 1: {score}')

    count_distinct = True
    score2 = getMapScore(top_map, count_distinct)
    print(f'Part 2: {score2}')
