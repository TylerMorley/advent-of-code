#! usr/bin/python3

from enum import Enum

def openfile(filename):
    with open(filename) as f:
        instructions = [line.strip() for line in f]
        return instructions

def simplify(instructions):
    location = current_location

    for instruction in instructions:
        action = instruction.pop(0)
        value = int(instruction)

        if action == 'L' or action == 'R':
            facing = location[2]
            facing = turn(facing, action, value)
            location[2] = facing

        else:
            position = location[:2]
            north_south, east_west = move(position, action, value)
            location[0] += north_south
            location[1] += east_west

    return location

def turn(facing, action, distance):
    distance //= 90
    current_facing = facing.value
    new_facing = 0
    if action == 'R':
        new_facing = (current_facing + distance) % 4
    elif action == 'L':
        new_facing = (current_facing - distance) % 4

    return direction(new_facing)

def move(position, action, value):
    new_x = 0
    new_y = 0

    if action == 'N':
        new_x -= value
    elif action == 'S':
        new_x += value
    elif action == 'W':
        new_y -= value
    elif action == 'E':
        new_y += value

    return [new_x, new_y]

class direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    
nav_instructions = openfile('example12.txt')
current_location = [0, 0, direction.EAST]
new_location = simplify(nav_instructions)
manhattan_distance = abs(new_location[0]) + abs(new_location[1])
print(manhattan(distance)
