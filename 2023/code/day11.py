#! usr/bin/python

def getImage(filename):
    with open(filename) as f:
        return [list(x.strip()) for x in f]

def expand(image):
    expanded_rows = []
    for line in image:
        expanded_rows.append(line)
        empty_line = ['.'] * len(line)
        if line == empty_line:
            expanded_rows.append(empty_line)

    rotated = [list(x) for x in list(zip(*expanded_rows[::-1]))]
    expanded_cols = []
    for line in rotated:
        expanded_cols.append(line)
        empty_line = ['.'] * len(line)
        if line == empty_line:
            expanded_cols.append(empty_line)

    expanded = [list(x) for x in list(zip(*expanded_cols))]
    return expanded

def getGalaxyPairs(image):
    galaxies = dict()
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == '#':
                name = str(len(galaxies)+1)
                galaxies[name] = [j,i]
    
    unpaired = galaxies.copy()
    galaxy_pairs = []
    for key in list(galaxies.keys()) > 0:
        galaxy = galaxies[key]
        del unpaired[key]
        #what's next prob needs to change:
        for other in unpaired:
            if galaxy != other:
                galaxy_pairs.append([galaxy[0], other[0]])
    return [galaxies, galaxy_pairs]

def getSumPaths(galaxies, paths):
    paths_sum = 0
    for path in paths:
        first = [x[1] for x in galaxies if x[0] == path[0]][0]
        second = [x[1] for x in galaxies if x[0] == path[1]][0]

        paths_sum += abs(first[0] - second[0]) + abs(first[1] - second[1])

    return paths_sum

def expand2(image, galaxies, scale):
    expanded_galaxies = galaxies.copy()
    for i in range(len(image)):
        line = image[i]
        empty_line = ['.'] * len(line)
        if line == empty_line:
            #add {scale} to the expanded galaxy
            return False


if __name__ == '__main__':
    filename = 'inputs/input11.txt'
    image = getImage(filename)
    expanded = expand(image)
    galaxies, pairs = getGalaxyPairs(expanded)
    output = getSumPaths(galaxies, pairs)
    print(f'Part 1: {output}')

    sm_galaxies, pairs = getGalaxyPairs(image)
    galaxies = expand(sm_galaxies, 1000000)
