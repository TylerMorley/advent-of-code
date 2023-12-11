#! usr/bin/python

def getPipes(filename):
    with open(filename) as f:
        pipe_list = [list(x.strip()) for x in f]
        pipe_dict = dict()
        for i in range(len(pipe_list)):
            row = pipe_list[i]
            for j in range(len(row)):
                tile = row[j]
                pipe_dict[f'x{j}y{i}'] = tile
        return pipe_dict

def getXAndY(key):
    x_ind = key.index('x')
    y_ind = key.index('y')
    x = key[x_ind+1:y_ind]
    y = key[y_ind+1:]
    return [int(x), int(y)]

def getStartingPoint(pipes):
    location_index = list(pipes.values()).index('S')
    location = list(pipes.keys())[location_index]

    shape = ''
    x,y = getXAndY(location)
    up_location = f'x{str(x)}y{str(y-1)}'
    hasUp = up_location in pipes and pipes[up_location] in ['|', '7', 'F']
    down_location = f'x{str(x)}y{str(y+1)}'
    hasDown = down_location in pipes and pipes[down_location] in ['|', 'L', 'J']
    left_location = f'x{str(x-1)}y{str(y)}'
    hasLeft = left_location in pipes and pipes[left_location] in ['-', 'L', 'F']
    right_location = f'x{str(x+1)}y{str(y)}'
    hasRight = right_location in pipes and pipes[right_location] in ['-', '7', 'J']
    if hasUp & hasDown:
        shape = '|'
    elif hasUp & hasRight:
        shape = 'L'
    elif hasUp & hasLeft:
        shape = 'J'
    elif hasDown & hasRight:
        shape = 'F'
    elif hasDown & hasLeft:
        shape = '7'
    elif hasLeft & hasRight:
        shape = '-'

    return [location, shape]

def getConnections(pipes, tile):
    connections = []
    x,y = getXAndY(tile)
    shape = pipes[tile]
    if shape in ['S', '|', 'L', 'J']:
        connections.append(f'x{str(x)}y{str(y-1)}')
    if shape in ['S', '|', '7', 'F']:
        connections.append(f'x{str(x)}y{str(y+1)}')
    if shape in ['S', '-', 'J', '7']:
        connections.append(f'x{str(x-1)}y{str(y)}')
    if shape in ['S', '-', 'L', 'F']:
        connections.append(f'x{str(x+1)}y{str(y)}')
    return connections

def getMainLoop(pipes):
    loop_tiles = []
    start, shape = getStartingPoint(pipes)
    pipes[start] = shape
    tiles_to_check = [start]
    
    while len(tiles_to_check) > 0:
        tile = tiles_to_check.pop(0)
        loop_tiles.append(tile)
        new_connections = getConnections(pipes, tile)
        for conn in new_connections:
            if conn not in tiles_to_check and conn not in loop_tiles:
                tiles_to_check.append(conn)
    
    return loop_tiles

def hasOddCrosses(pipes, tile):
    x,y = getXAndY(tile)
    above = []
    for i in range(y):
        above.append(pipes[f'x{x}y{i}'])

    count = 0
    count += above.count('-')
    count += above.count('F')
    count += above.count('7')
    count += above.count('J')
    count += above.count('L')

    if count % 4 != 0:
        return True
    return False

def countInternals(pipes):
    count = 0
    for tile_key in list(pipes.keys()):
        if pipes[tile_key] == '.' and hasOddCrosses(pipes, tile_key):
            count += 1
    return count

if __name__ == '__main__':
    filename = 'inputs/input10.txt'
    pipes = getPipes(filename)
    loop_length = getMainLoop(pipes)
    farthest = len(loop_length) // 2
    print(f'Part 1: {farthest}')
