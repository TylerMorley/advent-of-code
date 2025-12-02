#! usr/bin/python3

def openfile(filename):
    with open(filename) as f:
        program = [line.strip() for line in f]
        for line in program:
            line = line.split(' = ')
        return program

def run(program):
    mask = ''
    mem = {}

    for line in program:
        command, value = line
        if command == 'mask':
            mask = command
        else:
            location = int(command.split('[')[1][:-1])
            masked_command = apply_mask(value, mask)
            mem = update_memory(mem, masked_command, value)

    init = sum_values(mem)
    return init

def apply_mask(value, mask):
    bit_value = dec_to_bit(value)
    masked_value = ''
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            masked_value += bit_value[i]
        else:
            masked_value += mask[i]

    return masked_value

def dec_to_bit(decimal):
    binary = ''
    while decimal >= 1:
        binary += str(decimal % 2)
        print(str(decimal % 2))
        decimal //= 2
    return binary[::-1]

def update_memory(mem, masked_command, value):
    if mem[location]:
        mem[location] = masked_value
    else:
        mem.update({location:masked_value})

    return mem

init_program = openfile('example14.txt')
initialization = run(init_program)
print(initialization)
