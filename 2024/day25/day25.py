#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        lines = ''.join(list(f)).split('\n\n')
        keys = []
        for line in lines:
            keys.append(line.strip().split('\n'))
        return keys

def imageToNums(image):
    key_or_lock = None
    if image[0] == '#####':
        key_or_lock = 'locks'
    elif image[0] == '.....':
        key_or_lock = 'keys'

    heights = []
    rotated = list(zip(*(image.copy())))
    for row in rotated:
        heights.append(row.count('#') - 1)

    return [key_or_lock, heights]

def checkFit(lock, key):
    key_fits = None
    comparison = [sum(x) for x in list(zip(lock, key))]
    key_fits = max(comparison) < 6
    return key_fits

def countLKPairs(locks, keys):
    count = 0
    for lock in locks:
        for key in keys:
            if checkFit(lock, key):
                count += 1

    return count

def testLocksAndKeys(images):
    objects = {'locks':[], 'keys':[]}
    for image in images:
        locks = []
        keys = []
        kind, nums = imageToNums(image)
        objects[kind].append(nums)
    count = countLKPairs(objects['locks'], objects['keys'])
    return count

if __name__ == '__main__':
    filename = 'input25.txt'
    images = getInput(filename)
    score = testLocksAndKeys(images)
    print(f'Part 1: {score}')
