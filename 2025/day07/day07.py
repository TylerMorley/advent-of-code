#! usr/bin/env python

def getInputs(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

def moveBeams(beams, cur_row, use_quantum=False):
    new_beams = [0 for x in range(len(cur_row))]
    new_splits = 0
    for i in range(len(beams)):
        beam = beams[i]
        if beam == 0 or beam == '.':
            continue
        elif cur_row[i] == '.':
            new_beams[i] += beam
        elif cur_row[i] == '^':
            new_splits += 1
            new_beams[i-1] += beam
            new_beams[i+1] += beam

    if not use_quantum:
        return [new_splits,new_beams]
    elif use_quantum:
        return new_beams

def countSplits(diagram):
    num_splits = 0
    first_line = diagram.pop(0)
    beam_entry = first_line.index('S')
    beams = list(first_line)
    beams[beam_entry] = 1
    for line in diagram:
        new_splits, beams = moveBeams(beams, line)
        num_splits += new_splits

    return num_splits

def countTimelines(diagram):
    use_quantum = True
    first_line = diagram.pop(0)
    beam_entry = first_line.index('S')
    beams = list(first_line)
    beams[beam_entry] = 1
    for line in diagram:
        beams = moveBeams(beams, line, use_quantum)

    return sum(beams)

if __name__ == '__main__':
    diagram = getInputs('input07.txt')
    splits = countSplits(diagram)
    print(f'Part 1: {splits}')

    diagram = getInputs('input07.txt')
    timelines = countTimelines(diagram)
    print(f'Part 2: {timelines}')
