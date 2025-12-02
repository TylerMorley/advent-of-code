#usr/env/bin python

def getInput(filename):
    with open(filename) as f:
        return f.read().strip()

def formBlocks(layout):
    blocks = []
    id_num = 0
    isFile = True
    while len(layout) > 0:
        length = int(layout[0])
        layout = layout[1:]
        mem_character = []
        if isFile:
            mem_character = str(id_num)
            id_num += 1
        else:
            mem_character = '.'
        
        new_segment = [mem_character for x in range(length)]
        blocks += new_segment
        isFile = not isFile

    return blocks

def moveBlocks(blocks):
    dots = blocks.count('.')
    while dots > 0:
        if dots == 1 and blocks[-1] == '.':
            blocks.pop()
            break
        i = blocks.index('.')
        if dots % 1000 == 0:
            print(f'{blocks.count('.')}')
        to_move = blocks.pop()
        try:
            blocks[i] = to_move
        except IndexError:
            print(f'Index Error: {blocks.count('.')}')
            raise IndexError
        dots = blocks.count('.')

    return blocks

def moveFiles(unmoved):
    current_id = unmoved[-1]
    current_index = unmoved.index(current_id)
    current_file = unmoved[current_index:]
    candidate_index = 0

    found_spot = False
    while not found_spot and candidate_index < len(unmoved)-1:
        candidate_index = unmoved.index('.')
        return False

def calcChecksum(layout):
    print('moveBlocks')
    unmoved = formBlocks(layout)
    blocks = moveBlocks(unmoved)
    print('checksum')
    checksum = 0
    i = 0
    while len(blocks) > 0:
        checksum += i * int(blocks.pop(0))
        i += 1

    return checksum

if __name__ == '__main__':
    filename = 'input09.txt'
    layout = getInput(filename)
    checksum = calcChecksum(layout)
    print(f'Part 1: {checksum}')
