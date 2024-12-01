#! /usr/bin/env python

def getInputs(filename):
    with open(filename) as f:
        lines = [x.strip().split('   ') for x in f]
        str_lists = [list(t) for t in list(zip(*lines))]
        lists = [[int(x) for x in l] for l in str_lists]
        return lists

def getTotalDistance(locations):
    [x.sort() for x in locations]
    columns = [list(x) for x in list(zip(*locations))]
    distances = 0
    for loc_pair in columns:
        distances += abs(loc_pair[0] - loc_pair[1])

    return distances

def getSimilarityScore(locations):
    left_list, right_list = locations
    score = 0

    for location in left_list:
        score += location * right_list.count(location)

    return score

if __name__ == '__main__':
    filename = 'input01.txt'
    location_lists = getInputs(filename)
    total_distance = getTotalDistance(location_lists.copy())
    print(f'day 01: {total_distance}')

    score = getSimilarityScore(location_lists)
    print(f'day 02: {score}')
