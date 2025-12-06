#! usr/bin/env python

def getInputs(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f]
        numbers = [[int(y) for y in x.split()] for x in lines[:-1]] + [lines[-1].split()]
        problems = [list(x) for x in list(zip(*numbers))]
        return problems

def solve(problem):
    operator = problem.pop(-1)
    if operator == '+':
        solution = 0
        for num in problem:
            solution += num
        return solution
    elif operator == '-':
        solution = 0
        for num in problem:
            solution -= num
        return solution
    elif operator == '*':
        solution = 1
        for num in problem:
            solution *= num
        return solution
    else:
        print(f'ERROR operator: {operator}')
        print(problem)

def complete(worksheet):
    grand_total = 0
    for problem in worksheet:
        grand_total += solve(problem)

    return grand_total

if __name__ == '__main__':
    worksheet = getInputs('input06.txt')
    grand_total = complete(worksheet)
    print(f'Part 1: {grand_total}')
