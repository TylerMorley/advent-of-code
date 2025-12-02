#! usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        return [x.strip() for x in f]

def searchableTransform(word_search):
    searchable = []

    rows = word_search.copy()
    searchable.append(rows)
    columns = [''.join(x) for x in list(zip(*word_search.copy()))]
    searchable.append(columns)

    diagonal_nwse = transformDiag(word_search.copy())
    searchable.append(diagonal_nwse)

    rotated = [''.join(x) for x in list(zip(*word_search.copy()[::-1]))]
    diagonal_nesw = transformDiag(rotated)
    searchable.append(diagonal_nesw)

    return searchable

def transformDiag(word_search):
    undiagonal = [list(x) for x in word_search]
    diagonal = []
    height = len(word_search)
    i = 1
    while len(undiagonal[-1]) > 0: 
        r = min(i,height)
        d_line = []
        for line in range(r):
            if len(undiagonal[line]) > 0:
                d_line.append(undiagonal[line].pop())

        diagonal.append(d_line)
        i += 1

    diagonal = [''.join(x) for x in diagonal]
    return diagonal

def countInstances(word_search, rule):
    searchable = searchableTransform(word_search)
    count = 0

    if rule == 'XMAS':
        for s in searchable:
            for row in s:
                count += row.count('XMAS')
                count += row.count('SAMX')

    elif rule == 'X-MAS':
        puzzle_size = [len(word_search), len(word_search[0])]
        nwse_diag = getMasLocs(searchable[2], 'MAS') + getMasLocs(searchable[2], 'SAM')
        nesw_diag = getMasLocs(searchable[3], 'MAS') + getMasLocs(searchable[3], 'SAM')
        nwse_rect = []
        nesw_rect = []
        for loc in nwse_diag:
            nwse_rect.append(transposeNwse(loc, puzzle_size))
        for loc in nesw_diag:
            nesw_rect.append(transposeNesw(loc, puzzle_size))

        count = len([x for x in nwse_rect if x in nesw_rect])

    return count

def getMasLocs(word_search, word):
    locations = []
    for i in range(len(word_search)):
        row = word_search[i]
        j = row.find(word)
        while j != -1:
            locations.append([i,j+1])
            j = row.find(word, j+1)

    return locations

def transposeNwse(location, puzzle_size):
    height, width = puzzle_size
    height -= 1
    width -= 1
    j,i = location

    if j <= width:
        y = i
        x = width - j + i
    else:
        y = j - width + i
        x = i
    return [y, x]

def transposeNesw(location, puzzle_size):
    height, width = puzzle_size
    height -= 1
    width -= 1
    j,i = location

    if j <= height:
        y = j - i
        x = i
    else:
        y = height - i
        x = j - height + i
    return [y, x]

if __name__ == '__main__':
    filename = 'input04.txt'
    word_search = getInput(filename)
    count = countInstances(word_search, 'XMAS')
    print(f'Part 1: {count}')

    count = countInstances(word_search, 'X-MAS')
    print(f'Part 2: {count}')
