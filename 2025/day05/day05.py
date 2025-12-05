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

def compareRanges(new_range, existing_range):
        new_low, new_high = new_range
        existing_low, existing_high = existing_range

        #new range completely within current range
        if new_low >= existing_low and new_high <= existing_high:
            return ['subset', None]
        #new range above current range
        if new_low > existing_high:
            return ['disjoint', None]
        #new range below current range
        if new_high < existing_low:
            return ['disjoint', None]
        #new range overlaps on high side
        if new_low >= existing_low and new_high > existing_high:
            message = 'update'
            update = [existing_low, new_high]
            return [message, update]
        #new range overlaps on low side
        if new_low < existing_low and new_high <= existing_high:
            overlap = new_high - existing_low
            message = 'update'
            update = [new_low, existing_high]
            return [message, update]
        #new range completely contains current range
        if new_low < existing_low and new_high > existing_high:
            overlap = existing_high - existing_low
            message = 'update'
            return [message, new_range]
        else:
            print(f'Error')
            print(f'new_range: {new_range}, existing_range: {existing_range}') 

def buildIdDb(new_range, cur_db):
    for i in range(len(cur_db)):
        message, update = compareRanges(new_range, cur_db[i])
        if message == 'disjoint':
            continue
        elif message == 'subset':
            return cur_db
        elif message == 'update':
            updated_range = update
            temp_db = cur_db[:i] + cur_db[i+1:]
            updated_db = buildIdDb(updated_range, temp_db)
            return updated_db
  
    cur_db.append(new_range)
    new_low, new_high = new_range
    add_to_count = new_high - new_low
    return cur_db

def countFreshIds(ranges):
    fresh_id_count = 0
    id_database = []
    for cur_range in ranges:
        id_database = buildIdDb(cur_range, id_database)

    for c_range in id_database:
        start, end = c_range
        fresh_id_count += end+1 - start

    return fresh_id_count

if __name__ == '__main__':
    ranges, ingredient_ids = getInputs('input05.txt')
    num_fresh = countFreshIngredients(ingredient_ids, ranges)
    print(f'Part 1: {num_fresh}')

    num_possible_fresh = countFreshIds(ranges)
    print(f'Part 2: {num_possible_fresh}')
