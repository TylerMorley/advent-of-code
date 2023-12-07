#! usr/bin/python

def buildAlmanac(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f if x != '\n']
        maps = dict()
        cur_title = 'seeds'
        cur_ranges = [int(x) for x in lines[0].split(': ')[1].split(' ')]
        for line in lines[1:]:
            if 'map' in line:
                maps.update({cur_title: cur_ranges})
                cur_title = line[:line.index(' map:')]
                cur_ranges = []
            else:
                cur_ranges.append([int(x) for x in line.split(' ')])
        maps.update({cur_title: cur_ranges})
        return maps

def getDestination(almanac_map, source):
    for a_range in almanac_map:
        a_dest, a_source, a_length = a_range
        if source in range(a_source, a_source+a_length):
            modifier = source - a_source
            return a_dest + modifier
    return source

def seedToLocation(almanac, source):
    translations = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    destination = source
    for translation in translations:
        destination = getDestination(almanac[translation], destination)

    return destination

def findLowestLocation(almanac):
    locations = []
    for seed in almanac['seeds']:
        locations.append(seedToLocation(almanac, seed))

    return min(locations)

def buildSeedRanges(seeds):
    seed_ranges = []
    while len(seeds) > 1:
        seed_ranges.append(seeds[:2])
        seeds = seeds[2:]
    return seed_ranges

def findLowestLocation2(almanac):
    seed_ranges = buildSeedRanges(almanac['seeds'].copy())

    locations = dict()
    for s_range in seed_ranges:
        start = s_range[0]
        end = s_range[0] + s_range[1]
        for seed in range(start, end):
            if seed not in locations:
                locations.update({str(seed):(seedToLocation(almanac, seed))})

    return min(list(locations.values()))

if __name__ == '__main__':
    filename = 'inputs/input05.txt'
    almanac = buildAlmanac(filename)
    min_location = findLowestLocation(almanac)
    print(f'Part 1: {min_location}')

    min_location = findLowestLocation2(almanac)
    print(f'Part 2: {min_location}')
