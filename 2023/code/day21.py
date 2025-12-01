#! usr/bin/python

def getGardenMap(filename):
    with open(filename) as f:
        return [x.strip() for x in f]
