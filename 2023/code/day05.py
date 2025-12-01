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

def seedToLocation(almanac, record, source):
    translations = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    if len(record) == 0:
        for translation in translations:
            record[translation] = dict()

    next_step = source
    new_translations = []
    destination = None
    for translation in translations:
        name = translation + '-' + str(next_step)
        if name not in record:
            new_translations.append(name)
            next_step = getDestination(almanac[translation], next_step)
        else:
            destination = record[name]
            print('break')
            break

    destination = next_step
    for new_t in new_translations:
        record[new_t] = destination

    return destination

def findLowestLocation(almanac):
    record = dict()
    locations = []
    for seed in almanac['seeds']:
        locations.append(seedToLocation(almanac, record, seed))

    return min(locations)

def buildSeedRanges(seeds):
    seed_ranges = []
    while len(seeds) > 1:
        seed_ranges.append(seeds[:2])
        seeds = seeds[2:]
    return seed_ranges

def findLowestLocation2(almanac):
    seed_ranges = buildSeedRanges(almanac['seeds'].copy())

    record = dict()
    locations = dict()
    for s_range in seed_ranges:
        start, length = s_range
        end = start + length
        for seed in range(start, end):
            if seed not in locations:
                locations.update({str(seed):(seedToLocation(almanac, record, seed))})

    return min(list(locations.values()))

if __name__ == '__main__':
    filename = 'inputs/testinput05.txt'
    almanac = buildAlmanac(filename)
    min_location = findLowestLocation(almanac)
    print(f'Part 1: {min_location}')

    min_location = findLowestLocation2(almanac)
    print(f'Part 2: {min_location}')
