#! usr/bin/python

def getRaces(filename):
    with open(filename) as f:
        lines = [x for x in f]
        time = [int(x) for x in lines[0].split()[1:]]
        distance = [int(x) for x in lines[1].split()[1:]]

        return list(zip(time,distance))
'''
def runRace(race):
    time = race[0]
    record = race[1]
    ways2win = 0

    for i in range(1, (time // 2) + 1):
        score = (time - i) * i
        if score > record:
            ways2win += 1

    ways2win *= 2
    if not time % 2:
        ways2win -= 1
    return ways2win
'''
def runRace(race):
    time = race[0]
    record = race[1]

    lower_bound = 1
    upper_bound = time // 2
    while upper_bound - lower_bound > 1:
        i = (upper_bound + lower_bound) // 2
        score = (time - i) * i
        if score > record:
            upper_bound = i
        elif score <= record:
            lower_bound = i
    
    cutoff = upper_bound
    if (time - lower_bound) * lower_bound > record:
        cutoff = lower_bound

    ways2win = ((time // 2) - cutoff + 1) * 2
    if not time % 2:
        ways2win -= 1
    return ways2win

def runRaces(races):
    margin_of_error = 1
    for race in races:
        margin_of_error *= runRace(race)

    return margin_of_error

def getRace2(filename):
    with open(filename) as f:
        lines = [x for x in f]
        time = int(lines[0].split(':')[1].replace(' ', ''))
        distance = int(lines[1].split(':')[1].replace(' ', ''))

    return [time, distance]

if __name__ == '__main__':
    filename = 'inputs/input06.txt'
    races = getRaces(filename)
    margin = runRaces(races)
    print(f'Part 1: {margin}')

    race = getRace2(filename)
    margin = runRace(race)
    print(f'Part 2: {margin}')
