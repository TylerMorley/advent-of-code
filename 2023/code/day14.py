#! usr/bin/python

def getPlatform(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

def tiltNorth(platform):
    return False
