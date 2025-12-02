#usr/env/bin python

def getInput(filename):
    with open(filename) as f:
        return [x.strip().split('-') for x in f]

def buildNetwork(connections):
    network = dict()
    for connection in connections:
        first, second = connection
        if first not in network:
            network[first] = set()
        if second not in network:
            network[second] = set()
        network[first].update([second])
        network[second].update([first])

    return network

def common(first, second):
    common = list(first[1] & second[1])
    new_sets = [{first[0], second[0], x} for x in common]
    return new_sets

def findSets(network, set_size=3):
    sets = []
    computers = list(network.keys())
    for computer in computers:
        other_computers = network[computer].copy()
        for other in other_computers:
            network[other].remove(computer)
        while len(other_computers) > 1:
            other = other_computers.pop()

            common = list(network[computer] & network[other])
            new_sets = [{computer, other, x} for x in common]
            sets += new_sets

    return sets
       
def getTSets(sets):
    t_sets = []
    for s in sets:
        if 't' in [x[0] for x in s]:
            t_sets.append(s)
    return t_sets

if __name__ == '__main__':
    filename = 'input23.txt'
    connections = getInput(filename)
    network = buildNetwork(connections)
    sets = findSets(network)
    t_sets = getTSets(sets)
    print(f'Part 1: {len(t_sets)}')
