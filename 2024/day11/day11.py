#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().strip().split(' ')]

def transformStone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        half = len(str(stone)) // 2
        return [int(str(stone)[:half]), int(str(stone)[half:])]
    else:
        return [stone * 2024]

def updateZeros(stones, generation):
    z_to_update = [i for i,v in enumerate(stones) if type(v) == str]
    for z in z_to_update:
        stones[z] = 'z' + str(int(stones[z][1:]) + 1)

    new_zeroes = [i for i,v in enumerate(stones) if v == 0]
    for i in new_zeroes:
        stones[i] = 'z0'

    return [stones]

def updateSim(simulation, record, generation):
    simulation = blink(simulation)
    simulation = updateZeros(simulation, generation)

    gen_size = generationSize(simulation, record)
    record.update({'z'+str(generation):gen_size})

    return [simulation, record]

def generationSize(stones, sim):
    oz_sum = 0
    old_zeroes = [x for x in stones if type(x) == str]
    for oz in old_zeroes:
        oz_sum += sim[oz]

    generation_size = len(stones) + oz_sum - len(old_zeroes)
    return generation_size

def blink(stones):
    new_stones = []
    for stone in stones:
        if type(stone) == int:
            new_stones += transformStone(stone)
        elif type(stone) == str:
            new_stones.append(stone)
    return new_stones

def blinks(stones, num):
    simulation = []
    record = dict()
    z_gen = None
    for i in range(num):
        stones = blink(stones)
        stones = updateZeros(stones, z_gen)
        
        if z_gen == None and 'z0' in stones:
            simulation = [0]
            z_gen = 0
            record.update({'z0':1})
        elif z_gen != None:
            simulation, sim_record = updateSim(simulation, sim_record, z_gen)
            z_gen += 1
    
    return generationSize(stones, record)

if __name__ == '__main__':
    filename = 'input11.txt'
    stones = getInput(filename)
    twenty_five = blinks(stones.copy(), 25)
    print(f'Part 1: {twenty_five}')

#    seventy_five = blinks(stones.copy(), 75)
#    print(f'Part 2: {seventy_five}')
