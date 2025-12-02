#! usr/bin/python3

from enum import Enum

def openfile(filename):
    with open(filename) as f:
        instructions = [line.strip() for line in f]
        return instructions

def simplify(instructions):
    boat_location = boat_start
    waypoint_location = waypoint_start

    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])

        if action == 'L' or action == 'R':
            waypoint_location = rotate(waypoint_location, action, value)

        elif action == 'F':
            boat_location = move_boat(boat_location, waypoint_location, value)
            
        else:
            waypoint_location = move_waypoint(waypoint_location, action, value)

        print(f'boat: {boat_location}')
        print(f'waypoint: {waypoint_location}')
            
    return boat_location

def rotate(current_waypoint, action, distance):
    new_waypoint = current_waypoint.copy()
    distance //= 90
    for i in range(distance):
        if action == 'R':
            new_waypoint = [new_waypoint[1] * (-1), new_waypoint[0]]
        elif action == 'L':
            new_waypoint = [new_waypoint[1], new_waypoint[0] * (-1)]

    return new_waypoint

def move_waypoint(position, action, value):
    new_position = position.copy()

    if action == 'N':
        new_position[1] -= value
    elif action == 'S':
        new_position[1] += value
    elif action == 'W':
        new_position[0] -= value
    elif action == 'E':
        new_position[0] += value

    return new_position

def move_boat(boat, waypoint, repetitions):
    new_location = boat.copy()

    new_location[0] += waypoint[0] * repetitions
    new_location[1] += waypoint[1] * repetitions

    return new_location
    
nav_instructions = openfile('input12.txt')
boat_start = [0, 0]
waypoint_start = [10, -1]
new_location = simplify(nav_instructions)
print(f'final: {new_location}')
manhattan_distance = abs(new_location[0]) + abs(new_location[1])
print(manhattan_distance)
