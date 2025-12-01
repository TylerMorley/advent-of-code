#! usr/bin/python

def getTrajectories(filename):
    with open(filename) as f:
        trajectories = []
        lines = [x.strip() for x in f]
        for line in lines:
            trajectories.append([x.split(', ') for x in line.split(' @ ')])
        return trajectories
