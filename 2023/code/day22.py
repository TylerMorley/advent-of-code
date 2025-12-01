#! usr/bin/python

def getBricks(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f]
        bricks = []
        for line in lines:
            brick = []
            ends = [x.split(',') for x in line.split('~')]
            for end in ends:
                brick.append([int(x) for x in end])

            bricks.append(brick)

        return bricks

def dropBrick(tower, brick):
    return False
