#! usr/bin/python

def getHeatMap(filename):
    with open(filename) as f:
        str_map = [x.strip() for x in f]
        heat_map = []
        for line in str_map:
            heat_map.append([int(x) for x in list(line)])

    return heat_map
