#! usr/bin/env python

def getInputs(filename):
    with open(filename) as f:
        ranges, ids = [x.split('\n') for x in f.read().strip().split('\n\n')]
        ranges = [[int(y) for y in x.split('-')] for x in ranges]
        ids = [int(x) for x in ids]
        return [ranges, ids]

def checkFreshness(ingredient_id, ranges):
    for id_range in ranges:
        low, high = id_range
        if low < ingredient_id < high+1:
            return True
        
    return False

def countFreshIngredients(ingredient_ids, ranges):
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        if checkFreshness(ingredient_id, ranges):
            fresh_count += 1

    return fresh_count

if __name__ == '__main__':
    ranges, ingredient_ids = getInputs('input05.txt')
    num_fresh = countFreshIngredients(ingredient_ids, ranges)
    print(f'Part 1: {num_fresh}')
