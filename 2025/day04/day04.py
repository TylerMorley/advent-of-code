#! usr/bin/env python

def getInputs(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

def getAdjacent(loc, grid):
    adjacents = []
    width = len(grid[0])
    height = len(grid)
    x,y = loc
    
    right_okay = (x+1) < width
    down_okay = (y+1) < height
    left_okay = (x-1) >= 0
    up_okay = (y-1) >= 0

    if right_okay:
        adjacents.append([x+1,y])
        if down_okay:
            adjacents.append([x+1,y+1])
        if up_okay:
            adjacents.append([x+1,y-1])
    if down_okay:
        adjacents.append([x,y+1])
    if left_okay:
        adjacents.append([x-1,y])
        if down_okay:
            adjacents.append([x-1,y+1])
        if up_okay:
            adjacents.append([x-1,y-1])
    if up_okay:
        adjacents.append([x,y-1])

    return adjacents

def countPaperRolls(locations, grid):
    num_rolls = 0
    for location in locations:
        x,y = location
        if grid[y][x] == '@':
            num_rolls += 1

    return num_rolls

def getForkliftAccessibility(grid, remove_rolls=False):
    locs_accessible = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '@':
                adjacent = getAdjacent([x,y], grid)
                num_adj_rolls = countPaperRolls(adjacent, grid)
                if num_adj_rolls < 4:
                    locs_accessible.append([x,y])

    if remove_rolls:
        return locs_accessible
    else:
        return len(locs_accessible)

def removeRolls(to_remove, grid):
    for location in to_remove:
        x,y = location
        temp = list(grid[y])
        temp[x] = 'X'
        grid[y] = ''.join(temp)

    return grid

def getMaxAccessibility(input_grid):
    num_accessible = 0
    grid = input_grid.copy()
    remove_rolls = True
    to_remove = [[-1,-1]]
    while len(to_remove) > 0:
        to_remove = getForkliftAccessibility(grid, remove_rolls)
        num_accessible += len(to_remove)
        grid = removeRolls(to_remove, grid) 

    return num_accessible

if __name__ == '__main__':
    grid = getInputs('input04.txt')
    num_accessible = getForkliftAccessibility(grid)
    print(f'Part 1: {num_accessible}')

    remove_rolls = True
    max_num_accessible = getMaxAccessibility(grid)
    print(f'Part 2: {max_num_accessible}')
