#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

def checkNeighbors(maze, location):
    x,y = location
    options = []

    if maze[y-1][x] in ['.', 'S']:
        options.append('up')
    if maze[y][x+1] in ['.', 'S']:
        options.append('right')
    if maze[y+1][x] in ['.', 'S']:
        options.append('down')
    if maze[y][x-1] in ['.', 'S']:
        options.append('left')

    return options

def move(location, direction):
    x,y = location
    if direction == 'right':
        return [x+1,y]
    if direction == 'up':
        return [x,y-1]
    if direction == 'left':
        return [x-1,y]
    if direction == 'down':
        return [x,y+1]

def mapSection(maze, start, direction):
    end = None
    location = move(start, direction)
    options = checkNeighbors(maze, location)
    traveled = 1
    while len(options) == 2:
        location = move(location, direction)
        x,y = location
        options = checkNeighbors(maze, location)
        if len(options) == 1:
            end = f'x{x}y{y}'
        elif len(options) > 2 and len(options) < 5:
            end = f'x{x}y{y}'

        traveled += 1

    return [end, traveled, len(options)-1]

def mapSections(maze, start):
    direction = 'right'
    sections = dict()

    paths = checkNeighbors(maze, start)
    sections['start'] = dict()
    for path in paths:
        section = dict()
        direction = path
        section = mapSection(maze, start, direction)
        end = section.pop(0)
        sections['start'][end] = section
        sections[end] = dict()
    
    starts = [[3,13],[1,11]]
    paths2 = checkNeighbors(maze, starts[0])
    for path in paths2:
        section = dict()
        direction = path
        section = mapSection(maze, start, direction)
        end = section.pop(0)
        x,y = starts[0]
        sections[f'x{x}y{y}'][end] = section
        sections[end] = dict() 
        
    paths3 = checkNeighbors(maze, starts[1])
    for path in paths3:
        section = dict()
        direction = path
        section = mapSection(maze, start, direction)
        end = section.pop(0)
        x,y = starts[1]
        sections[f'x{x}y{y}'][end] = section
        sections[end] = dict() 
        
    return sections
