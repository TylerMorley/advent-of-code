#! usr/bin/python3

def openfile(filename):
    with open(filename) as f:
        layout = [list(line.strip()) for line in f]
        return layout

def run_simulation(layout):
    current_layout = []
    new_layout = layout.copy()
    while new_layout != current_layout:
        current_layout = new_layout
        new_layout = simulate(current_layout)

    return new_layout
    
def simulate(layout):
    new_row = ['' for x in layout[0]]
    new_layout = [new_row.copy() for x in layout]
    # print(get_visible(layout, 3, 3))
    for i in range(0, len(layout)):
        for j in range(0, len(layout[i])):
            position = layout[i][j]
            new_status = ''
            if position == 'L':
                visible_seats = get_visible(layout, i, j)
                new_status = simulate_empty(visible_seats)
            elif position == '#':
                visible_seats = get_visible(layout, i, j)
                new_status = simulate_occupied(visible_seats)
            elif position == '.':
                new_status = '.'

            new_layout[i][j] = new_status

    # print('layout:')
    # for row in new_layout:
        # print(row)
    return new_layout

def get_visible(layout, row, col):
    adjacent_seats = []

    adjacent_seats.append(sightline(layout, row, col, -1, -1))
    adjacent_seats.append(sightline(layout, row, col, -1, 0))
    adjacent_seats.append(sightline(layout, row, col, -1, 1))
    adjacent_seats.append(sightline(layout, row, col, 0, 1))
    adjacent_seats.append(sightline(layout, row, col, 1, 1))
    adjacent_seats.append(sightline(layout, row, col, 1, 0))
    adjacent_seats.append(sightline(layout, row, col, 1, -1))
    adjacent_seats.append(sightline(layout, row, col, 0, -1))
        
    return adjacent_seats

def sightline(layout, row, col, dir_x, dir_y):
    curx = row + dir_x
    cury = col + dir_y
    while 0 <= curx < len(layout) and 0 <= cury < len(layout[0]):
        if layout[curx][cury] == '#':
            return '#'
        if layout[curx][cury] == 'L':
            return 'L'

        curx += dir_x
        cury += dir_y

    return '.'

def simulate_empty(seats):
    for seat in seats:
        if seat == '#':
            return 'L'
    return '#'

def simulate_occupied(seats):
    occupied = seats.count('#')

    if occupied < 5:
        return'#'
    else:
        return 'L'

def count_occupied_seats(layout):
    count = 0
    for row in layout:
        count += row.count('#')

    return count
                         
seat_layout = openfile('input11.txt')
stable_layout = run_simulation(seat_layout)
print('output:')
for row in stable_layout:
    print(row)
num_occupied_seats = count_occupied_seats(stable_layout)
print(num_occupied_seats)
