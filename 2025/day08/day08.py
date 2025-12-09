#! usr/bin/env python
import math
import operator
import functools

def getInputs(filename):
    with open(filename) as f:
        return [[int(y) for y in x.strip().split(',')] for x in f]

def measureDistance(point1, point2):
    x1,y1,z1 = point1
    x2,y2,z2 = point2
    return math.isqrt(abs(x1-x2)**2 + abs(y1-y2)**2 + abs(z1-z2)**2)

def orderConnections(j_boxes):
    unmeasured = j_boxes.copy()
    connections = []
    #might be able to turn these into list comprehensions
    #make a list of possible connections, then measure each one
    while len(unmeasured) > 0:
        cur_box = unmeasured.pop(0)
        for other_box in unmeasured:
            distance = measureDistance(cur_box, other_box)
            connections.append([distance, [cur_box,other_box]])

    connections.sort()
    return connections

def connect(circuits, box1, box2):
    #Beware: assumes there's only one option
    existing1 = [c for c in circuits if box1 in c][0]
    existing2 = [c for c in circuits if box2 in c][0]

    if existing1 != existing2:
        new_circuit = existing1 + existing2
        circuits.remove(existing1)
        circuits.remove(existing2)
        circuits.append(new_circuit)

    return circuits

def getCircuitSizes(j_boxes, num_to_connect):
    circuits = [[x] for x in j_boxes]
    ordered_cons = orderConnections(j_boxes)
    connections = ordered_cons[:num_to_connect]
    for connection in connections:
        first, second = connection[1]
        connect(circuits, first, second)

    lengths = [len(x) for x in circuits]
    lengths.sort(reverse=True)
    #https://stackoverflow.com/questions/2104782/returning-the-product-of-a-list
    circuit_sizes = functools.reduce(operator.mul, lengths[:3], 1)
    return circuit_sizes

def makeLargeCircuit(j_boxes):
    circuits = [[x] for x in j_boxes]
    ordered_cons = orderConnections(j_boxes)
    first = second = None
    while len(circuits) > 1:
        first,second = ordered_cons.pop(0)[1]
        connect(circuits, first, second)

    return first[0] * second[0]

if __name__ == '__main__':
    junction_boxes = getInputs('input08.txt')
    num_to_connect = 1000
    answer = getCircuitSizes(junction_boxes, num_to_connect)
    print(f'Part 1: {answer}')

    answer = makeLargeCircuit(junction_boxes)
    print(f'Part 2: {answer}')
