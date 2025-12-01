#! usr/bin/python

def getTrails(filename):
    with open(filename) as f:
        return [x.strip() for x in f]
