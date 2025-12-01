#! usr/bin/python

def getDiagram(filename):
    with open(filename) as f:
        diagram = dict()
        lines = [x.strip() for x in f]
        for line in lines:
            name, connections = line.split(': ')
            connections = connections.split(' ')
            diagram[name] = connections
        
        return diagram
