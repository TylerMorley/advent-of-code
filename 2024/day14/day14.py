#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f]
        str_robots = [[y[2:].split(',') for y in x.split(' ')] for x in lines]
        robots = [[[int(z) for z in y] for y in x] for x in str_robots]
        return robots

def moveRobot(robot, room, seconds):
    x_pos,y_pos = robot[0]
    x_vel,y_vel = robot[1]
    width, height = room

    x_pos += x_vel * seconds
    x_pos = x_pos % width
    y_pos += y_vel * seconds
    y_pos = y_pos % height

    return [x_pos, y_pos]

def moveRobots(robots, room, seconds):
    positions = []
    for robot in robots:
        position = moveRobot(robot, room, seconds)
        positions.append(position)
    return positions

def stepRobots(robots, room):
    for robot in robots:
        position = moveRobot(robot, room, seconds)
        robot[0] = position
    return robots

def getSafetyFactor(positions, room):
    width, height = room

    quadrants = []
    quadrants.append([[0, width // 2 - 1], [0, height // 2 - 1]])
    quadrants.append([[-(width // -2), width - 1], [0, height // 2 - 1]])
    quadrants.append([[0, width // 2 - 1], [-(height // -2), height - 1]])
    quadrants.append([[-(width // -2), width - 1], [-(height // -2), height - 1]])

    score = 1
    for q in quadrants:
        num = 0
        for pos in positions:
            if pos[0] >= q[0][0] and pos[0] <= q[0][1] and pos[1] >= q[1][0] and pos[1] <= q[1][1]:
                num += 1
        score *= num

    return score

def getAdjacent(height, width, location):
    neighbors = []
    y,x = location

    if x-1 >= 0:
        neighbors.append([y, x-1])
    if x+1 < width:
        neighbors.append([y, x+1])
    if y-1 >= 0:
        neighbors.append([y-1, x])
    if y+1 < height:
        neighbors.append([y+1, x])
    if x-1 >= 0 and y-1 >= 0:
        neighbors.append([y-1, x-1])
    if x-1 >= 0 and y+1 < height:
        neighbors.append([y+1, x-1])
    if x+1 < width and y-1 >= 0:
        neighbors.append([y-1, x+1])
    if x+1 < width and y+1 < height:
        neighbors.append([y+1, x+1])

    return neighbors

def checkForImage(height, width, positions):
    for pos in positions:
        neighbors = getAdjacent(height, width, pos)
        count = len([x for x in neighbors if x in positions])
        if count > 5:
            return True
    return False

def lookForTree(robots, room):
    positions = []
    i = 1954
    is_candidate = False
    while not is_candidate:
        robots = stepRobots(robots, room)
        positions = [x[0] for x in robots]
        is_candidate = checkForImage(room[0], room[1], positions)
        i += 1
        if i % 100 == 0:
            print(i)

    return i

if __name__ == '__main__':
    filename = 'input14.txt'
    robots = getInput(filename)
    room = [101, 103]
    seconds = 100
    positions = moveRobots(robots.copy(), room, seconds)
    score = getSafetyFactor(positions, room)
    print(f'Part 1: {score}')

    i = lookForTree(robots, room)
    print(f'Part2: {i}')
