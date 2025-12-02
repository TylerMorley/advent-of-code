#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f]
        gap = lines.index('')
        
        starting_values = lines[:gap]
        starting_values = [x.split(': ') for x in starting_values]
        for val in starting_values:
            val[1] = int(val[1])
        starting_values = {x[0]:x[1] for x in starting_values}

        wires = lines[gap+1:]
        inputs = [x.split(' -> ')[0].split(' ') for x in wires]
        in_wires = [[x[0],x[2]] for x in inputs]
        commands = [x[1] for x in inputs]
        outputs = [x.split(' -> ')[1] for x in wires]
        wires = [list(x) for x in list(zip(in_wires, commands, outputs))]
        wires = [{'inputs':x[0], 'command':x[1], 'output':x[2]} for x in wires]

        return [starting_values, wires]

def simulateGate(gate, values):
    first, second = [values[x] for x in gate['inputs']]
    result = None
    if gate['command'] == 'AND':
        result = first & second
    elif gate['command'] == 'OR':
        result = first | second
    if gate['command'] == 'XOR':
        result = first ^ second
    values[gate['output']] = result

    return values

def simulateGates(gates, values):
    while(len(gates)) > 0:
        gate = gates.pop(0)
        if gate['inputs'][0] not in values or gate['inputs'][1] not in values:
            gates.append(gate)
        else:
            values = simulateGate(gate, values)

    output_keys = list(reversed(sorted([x for x in values.keys() if x[0] == 'z'])))
    output = [str(values[x]) for x in output_keys]
    output = int(''.join(output), 2)
    return output

if __name__ == '__main__':
    filename = 'input24.txt'
    values, gates = getInput(filename)
    score = simulateGates(gates, values)
    print(f'Part 1: {score}')
