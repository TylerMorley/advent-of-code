#! usr/bin/python

def getDigPlan(filename):
    with open(filename) as f:
        plan = []
        lines = [x.strip() for x in f]
        for line in lines:
            direction = line.split(' ')
            direction[1] = int(direction[1])
            direction[2] = direction[2][1:-1]
            plan.append(direction)
        return plan

def dig(trench, position, direction):
    x = int(position[position.find('x')+1:position.find('y')])
    y = int(position[position.find('y')+1:])
    cardinal = direction[0]
    distance = direction[1]
    new_position = ''

    if cardinal == 'R':
        new_x = x + distance
        new_position = f'x{new_x}y{y}'
        for i in range(x + 1, new_x + 1):
            trench[f'x{i}y{y}'] = '#'
    elif cardinal == 'D':
        new_y = y + distance
        new_position = f'x{x}y{new_y}'
        for i in range(y + 1, new_y + 1):
            trench[f'x{x}y{i}'] = '#'
    elif cardinal == 'L':
        new_x = x - distance
        new_position = f'x{new_x}y{y}'
        for i in range(x - 1, new_x - 1, -1):
            trench[f'x{i}y{y}'] = '#'
    elif cardinal == 'U':
        new_y = y - distance
        new_position = f'x{x}y{new_y}'
        for i in range(y - 1, new_y - 1, -1):
            trench[f'x{x}y{i}'] = '#'

    return [trench, new_position]

def digTrench(directions):
    trench = {'x0y0': '#'}
    position = 'x0y0'
    for line in directions:
        trench, position  = dig(trench, position, line)
    return trench

def isInside(row, index):
    if index == 0:
        return False
    left = row[:index]
    if '#' not in left:
        return False
    
    count = 0
    left = left[left.find('#'):]
    while len(left) > 0:
        if '#' not in left:
            left = ''
        elif '.' not in left:
            left = ''
            count += 1
        else:
            left = left[left.find('.'):]
            left = left[left.find('#'):]
            count += 1

    isOdd = count % 2 == 1
    return isOdd

def dict_to_list(d_trench):
    keys = list(d_trench.keys())
    width = max([int(x[x.find('x')+1:x.find('y')]) for x in keys]) + 1
    height = max([int(x[x.find('y')+1:]) for x in keys]) + 1

    l_trench = []
    for i in range(height):
        line = ''
        for j in range(width):
            if f'x{j}y{i}' in d_trench:
                line += '#'
            else:
                line += '.'
        l_trench.append(line)

    for line in l_trench:
        print(line)
    return l_trench

def fillTrench(trench):
    filled = []
    for row in trench:
        filled_row = []
        for i in range(len(row)):
            cube = row[i]
            if cube == '#':
                filled_row.append('#')
            elif isInside(row, i):
                filled_row.append('#')
            else:
                filled_row.append('.')
        filled.append(filled_row)

    return filled

if __name__ == '__main__':
    filename = 'inputs/testinput18.txt'
    digPlan = getDigPlan(filename)
    dict_trench = digTrench(digPlan)
    trench = dict_to_list(dict_trench)
    filled = fillTrench(trench)
    count = 0
    for line in filled:
        count += line.count('#')
    #17661 is too low
    print(f'Part 1: {count}')
