# usr/bin/env python
import copy

def getInput(filename):
    with open(filename) as f:
        return [list(x.strip()) for x in f]

def rotate(floormap, cur_location):
    new_map = list(zip(*floormap))[::-1]
    new_map = [list(row) for row in new_map]
    width = len(floormap[0])
    new_location = [width - cur_location[1] - 1, cur_location[0]]

    return [new_map, new_location]

def moveToObstacle(floormap, cur_location):
    y,x = cur_location
    indices = [i for i,v in enumerate(floormap[y]) if v == '#' and i < x]
    if len(indices) > 0:
        new_x = max(indices) + 1
    else:
        new_x = 0

    floormap[y][new_x:x+1] = ['X' for i in floormap[y][new_x:x+1]]
    return [floormap, [y,new_x]]

def getStartLocation(floormap):
    y = x = 0
    for row in floormap:
        if '^' in row:
            x = row.index('^')
            return [y,x]
        y += 1

    return False

def countVisited(floormap):
    count = 0
    for row in floormap:
        count += len([x for x in row if x == 'X'])
    return count

def getVisited(floormap):
    locs = []
    for i in range(len(floormap)):
        exes = [x for x,v in enumerate(floormap[i]) if v == 'X']
        locs += [[i,x] for x in exes]
    return locs

def predictGuard(floormap, get_locs=False):
    location = getStartLocation(floormap)
    test_visited = 0
    count_unchanged = 0
    rotations = 0
    while location[1] != 0:
        floormap, location = rotate(floormap, location)
        rotations += 1
        floormap, location = moveToObstacle(floormap, location)

        new_visited = countVisited(floormap)
        if new_visited == test_visited:
            count_unchanged += 1
            if count_unchanged > 2:
                return None
        else:
            count_unchanged = 0
        test_visited = new_visited

    rotations_past_true = rotations % 4
    to_fix = (4 - rotations_past_true) % 4
    for r in range(to_fix):
        floormap, location = rotate(floormap, location)

    if get_locs:
        locations_visited = getVisited(floormap)
    else:
        locations_visited = countVisited(floormap)
    return(locations_visited)

def tryObstacles(clean_map):
    obstacles = []
    get_locs = True
    path = predictGuard(clean_map.copy(), get_locs)
    start = getStartLocation(clean_map)
    path.remove(start)
    i = 0

    for loc in path:
        y,x = loc
        test_map = copy.deepcopy(clean_map)
        test_map[y][x] = '#'

        if predictGuard(test_map) == None:
            obstacles.append(loc)
        print(f'{i}/{len(path)}')
        i += 1
    return len(obstacles)

if __name__ == '__main__':
    filename = 'input06.txt'
    floormap = getInput(filename)
    score = predictGuard(floormap.copy())
    print(f'Part 1: {score}')

    score = tryObstacles(floormap.copy())
    print(f'Part 2: {score}')
