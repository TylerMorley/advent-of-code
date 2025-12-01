#! usr/bin/python

def getDamagedRecord(filename):
    with open(filename) as f:
        record = [x.strip().split(' ') for x in f]
        for line in record:
            line[1] = [int(x) for x in line[1].split(',')]

    return record

def checkFit(springs, size):
    if len(springs) < size:
        return False
    for spring in springs[:size]:
        if spring == '.':
            return False
    return True

def getNumArrangements(springs, checksum):
    if len(checksum) == 0:
        if springs.count('#') == 0:
            return 1
        else:
            return 0
    if len(springs) == 0 and len(checksum) > 0:
        return 0

    count = 0
    if springs[0] == '.':
        count += getNumArrangements(springs[1:], checksum)

    elif springs[0] == '#':
        fits = checkFit(springs, checksum[0])
        if fits:
            count += getNumArrangements(springs[checksum[0]+1:], checksum[1:])
            count += getNumArrangements(springs[1:], checksum)
        else:
            return 0

    elif springs[0] == '?':
        #count += getNumArrangements('.' + springs[1:], checksum)
        count += getNumArrangements('#' + springs[1:], checksum)

    return count
