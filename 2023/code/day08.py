#! usr/bin/python

def getDocument(filename):
    with open(filename) as f:
        document = [x.strip() for x in f if x != '\n']
        instructions = document.pop(0)

        network = dict()
        for node in document:
            name = node[:3]
            next_elements = node[7:-1].split(', ')
            network[name] = next_elements

        return [instructions, network]

def getNextNode(node, direction):
    if direction == 'L':
        return node[0]
    elif direction == 'R':
        return node[1]
    else:
        return False

def planJourney(instructions, network):
    i = 0
    node = 'AAA'
    steps = 0

    while node != 'ZZZ':
        node = getNextNode(network[node], instructions[i])
        i = (i + 1) % len(instructions)
        steps += 1

    return steps

def getStartNodes(network):
    return [x for x in list(network.keys()) if x[2] == 'A']

def checkForEndNodes(nodes):
    for node in nodes:
        if node[2] != 'Z':
            return False
    return True

def planJourney2(instructions, network):
    i = 0
    nodes = getStartNodes(network)
    atEndNodes = False
    next_nodes = []
    steps = 0

    while atEndNodes == False:
        for node in nodes:
            next_nodes.append(getNextNode(network[node], instructions[i]))
        
        nodes = next_nodes
        next_nodes = []
        i = (i + 1) % len(instructions)
        steps += 1
        atEndNodes = checkForEndNodes(nodes)

    return steps

if __name__ == '__main__':
    filename = 'inputs/input08.txt'
    instructions, network = getDocument(filename)
    score = planJourney(instructions, network)
    print(f'Part 1: {score}')

    score = planJourney2(instructions, network)
    print(f'Part 2: {score}')
