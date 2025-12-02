#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        return [list(x.strip()) for x in f]

def getLocations(antenna_map):
    antennas = dict()
    for i in range(len(antenna_map)):
        row = antenna_map[i]
        ants = [[x,i] for x,v in enumerate(row) if v != '.']
        for ant in ants:
            x,y = ant
            val = antenna_map[y][x]
            if val not in antennas:
                antennas[val] = [ant]
            else:
                antennas[val].append(ant)
    return antennas

def makeAntinode(current, other):
    cur_x, cur_y = current
    oth_x, oth_y = other
    distance_x = oth_x - cur_x 
    distance_y = oth_y - cur_y 
    close = [cur_x - distance_x, cur_y - distance_y]
    far = [oth_x + distance_x, oth_y + distance_y]

    str_close = f'x{close[0]}y{close[1]}'
    str_far = f'x{far[0]}y{far[1]}'

    return {str_close, str_far}

def makeAntinodes(antennas):
    antinodes = set()
    for frequency in antennas:
        freq = antennas[frequency].copy()
        while len(freq) > 0:
            current = freq.pop()
            for other in freq:
                new_antinodes = makeAntinode(current, other)
                antinodes.update(new_antinodes)

    return antinodes

def is_inbounds(height, width, antinode):
    x = int(antinode[1:antinode.find('y')])
    y = int(antinode[antinode.find('y')+1:])
    if x < 0 or x > width - 1:
        return False
    if y < 0 or y > height - 1:
        return False
    return True

def uniqueLocs(antenna_map):
    antennas = getLocations(antenna_map)
    height = len(antenna_map)
    width = len(antenna_map[0])

    antinodes = {x for x in makeAntinodes(antennas) if is_inbounds(height, width, x)}
    return antinodes

if __name__ == '__main__':
    filename = 'input08.txt'
    antenna_map = getInput(filename)
    score = len(uniqueLocs(antenna_map))
    print(f'Part 1: {score}')
