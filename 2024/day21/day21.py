#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

def targetLocation(pad, button):
    for y in range(len(pad)):
        row = pad[y]
        if button in row:
            x = row.index(button)
            return [x,y]
    return False

def arrowToNum(code):
    numpad = [['7', '8', '9'],
              ['4', '5', '6'],
              ['1', '2', '3'],
              [' ', '0', 'A']]
    buttons = ''
    location = [2,3]
    for digit in code:
        target = targetLocation(numpad, digit)

        x_dist = target[0] - location[0]
        y_dist = target[1] - location[1]
        if x_dist < 0:
            x_buttons = ['<' for x in range(abs(x_dist))]
        else:
            x_buttons = ['>' for x in range(x_dist)]
        if y_dist < 0:
            y_buttons = ['^' for y in range(abs(y_dist))]
        else:
            y_buttons = ['v' for y in range(y_dist)]

        buttons += ''.join(x_buttons)
        buttons += ''.join(y_buttons)
        buttons += 'A'
        location = target

    return buttons

def arrowToArrow(arrows):
    arrowpad = [[' ', '^', 'A'],
                ['<', 'v', '>']]
    buttons = ''
    location = [2,0]
    for arrow in arrows:
        target = targetLocation(arrowpad, arrow)

        x_dist = target[0] - location[0]
        y_dist = target[1] - location[1]
        if x_dist < 0:
            x_buttons = ['<' for x in range(abs(x_dist))]
        else:
            x_buttons = ['>' for x in range(x_dist)]
        if y_dist < 0:
            y_buttons = ['^' for y in range(abs(y_dist))]
        else:
            y_buttons = ['v' for y in range(y_dist)]

        buttons += ''.join(x_buttons)
        buttons += ''.join(y_buttons)
        buttons += 'A'
        location = target

    return buttons

def getComplexity(code):
    first_arrows = arrowToNum(code)
    second_arrows = arrowToArrow(first_arrows)
    third_arrows = arrowToArrow(second_arrows)

    leading = code[0]
    while leading == '0':
        code = code[1:]
        leading = code[0]
    complexity = int(code[:-1]) * len(third_arrows)
    return complexity

if __name__ == '__main__':
    filename = 'input21.txt'
    codes = getInput(filename)
    score = 0
    for code in codes:
        score += getComplexity(code)
    print(f'Part 1: {score}')
