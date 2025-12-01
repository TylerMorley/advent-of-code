#! /usr/bin/env python

def getInputs(filename):
    with open(filename) as f:
        rotations = list(f)
        rotations = [x.strip() for x in rotations]
        rotations = [[x[0],int(x[1:])] for x in rotations]
        return rotations

def turn(arrow_start, rotation, use_method=False):
    direction, distance = rotation
    arrow = None

    if direction == 'R':
        arrow = (arrow_start + distance) % 100
    elif direction == 'L':
        arrow = (arrow_start - distance) % 100

    if not use_method:
        return [arrow, None]
    else:
        crossed_zero = None
        if direction == 'R':
            crossed_zero = (arrow_start + distance) // 100
        elif direction == 'L':
            crossed_zero = abs((arrow_start - distance) // 100)
            if arrow_start == 0 and distance > 0:
                crossed_zero -= 1
            if arrow == 0:
                crossed_zero += 1

        return [arrow, crossed_zero]

def getPassword(start, rotations, use_method=False):
    arrow = start
    zeroes = 0
    for rotation in rotations:
        arrow, crossed_zero = turn(arrow, rotation, use_method)
        if use_method:
            zeroes += crossed_zero
        elif arrow == 0:
            zeroes += 1

    return zeroes

if __name__ == '__main__':
    start = 50
    rotations = getInputs('input01.txt')
    password = getPassword(start, rotations)
    print(f'Part 1: {password}')

    start = 50
    use_method = True
    password2 = getPassword(start, rotations, use_method)
    print(f'Part 2: {password2}')
