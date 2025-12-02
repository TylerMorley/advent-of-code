# usr/bin/env python
import copy

def getInput(filename):
    with open(filename) as f:
        str_equations = [[y for y in line.strip().split(': ')] for line in f]
        equations = []
        for line in str_equations:
            target = int(line[0])
            nums = [int(x) for x in line[1].split(' ')]
            equations.append([target, nums])
        return equations

def operCombos(num_numbers, use_concat=False):
    combos = []
    for layer in range(num_numbers-1):
        new_combos = []
        if len(combos) == 0:
            combos = [['+'], ['*']]
            if use_concat:
                combos.append(['||'])
            continue
        for combo in combos:
            new_combos.append(combo + ['+'])
            new_combos.append(combo + ['*'])
            if use_concat:
                new_combos.append(combo + ['||'])
        combos = new_combos

    return combos

def checkCombo(combo, nums, test_value):
    subtotal = nums.pop(0)
    for i in range(len(combo)):
        oper = combo[i]
        num = nums.pop(0)
        if oper == '+':
            subtotal += num
        elif oper == '*':
            subtotal *= num
        elif oper == '||':
            subtotal = int(str(subtotal) + str(num))
    is_true = True if subtotal == test_value else False
    return is_true

def checkEquation(oper_combos, nums, test_value):
    for combo in oper_combos:
        if checkCombo(combo, nums.copy(), test_value):
            return True
    return False

def calibrate(equations, use_concat=False):
    result = 0
    for equation in equations:
        test_value, nums = equation
        oper_combos = operCombos(len(nums), use_concat)
        if checkEquation(oper_combos, nums.copy(), test_value):
            result += test_value

    return result

if __name__ == '__main__':
    filename = 'input07.txt'
    equations = getInput(filename)
    score = calibrate(equations)
    print(f'Part 1: {score}')

    use_concat = True
    score = calibrate(equations, use_concat)
    print(f'Part 2: {score}')
    #takes a good 20 seconds, could use optimization
