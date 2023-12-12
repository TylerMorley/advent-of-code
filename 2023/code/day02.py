#! usr/bin/python

def buildRecord(filename):
    with open(filename) as f:
        games = [x.strip() for x in f]
        record = dict()

        for game in games:
            title, handfuls = game.split(': ')
            rgame = []
            for handful in handfuls.split('; '):
                subsets = []
                for subset in handful.split(', '):
                    cubes = subset.split(' ')
                    subsets.append([cubes[1], int(cubes[0])])
                rgame.append(subsets)
                
            record.update({title: rgame})

        return record

def checkPossibility(game, bag):
    for handful in game:
        for cubes in handful:
            color, num = cubes
            if color not in bag or num > bag[color]:
                return False
    return True

def getScore(games, bag):
    score = 0
    for name in games:
        if checkPossibility(games[name], bag):
            score += int(name.split(' ')[1])
    return score

def getPower(game):
    min_bag = dict()
    power = 1
    for handful in game:
        for cubes in handful:
            color, num = cubes
            if color not in min_bag or num > min_bag[color]:
                min_bag[color] = num

    for color in min_bag:
        power *= min_bag[color]
    return power
        
if __name__ == '__main__':
    filename = 'inputs/input02.txt'
    games = buildRecord(filename)
    bag = {'red': 12, 'green':13, 'blue':14}
    score = getScore(games, bag)
    print(f'Part 1: {score}')

    power = 0
    for game in list(games.values()):
        power += getPower(game)
    print(f'Part 2: {power}')
