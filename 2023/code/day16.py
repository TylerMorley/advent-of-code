#! usr/bin/python

def getContraption(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

def move(location, direction):
    if direction == 'r':
        location[1] += 1
    elif direction == 'l':
        location[1] -= 1
    elif direction == 'd':
        location[0] += 1
    elif direction == 'u':
        location[0] -= 1
    return location

def takeStep(location, direction, contents):
    if contents == '.':
        location = move(location, direction)

    return [location, direction]
