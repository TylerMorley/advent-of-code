#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f]
        str_machines = []
        machine = []
        for line in lines:
            if line == '':
                str_machines.append(machine)
                machine = []
            else:
                machine.append(line)
        str_machines.append(machine)

        machines = []
        for sm in str_machines:
            machine = dict()
            for line in sm:
                title, nums = line.split(': ')
                x,y = nums.split(', ')
                machine[title] = [int(x[2:]), int(y[2:])]
            machines.append(machine)

        return machines

def calcTokens(machine):
    x, z = machine['Button A']
    y, w = machine['Button B']
    m, n = machine['Prize']

    a = (n*y - w*m)/(z*y - w*x)
    b = (m - x*a)/y

    if a.is_integer() and b.is_integer():
        return [int(a),int(b)]
    else:
        return None

def convert(machine):
    conversion_rate = 10000000000000
    for i in range(len(machine['Prize'])):
        machine['Prize'][i] += conversion_rate
    return machine

def playMachines(machines, should_convert=False):
    tokens = 0
    for machine in machines:
        if should_convert:
            machine = convert(machine)

        cost = calcTokens(machine)
        if cost != None:
            tokens += (cost[0]*3 + cost[1])

    return tokens

if __name__ == '__main__':
    filename = 'input13.txt'
    machines = getInput(filename)
    tokens = playMachines(machines)
    print(f'Part 1: {tokens}')

    tokens = playMachines(machines, True)
    print(f'Part 2: {tokens}')
