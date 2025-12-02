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
    for i in range(0, len(layout)):
        for j in range(0, len(layout[i])):
            position = layout[i][j]
            new_status = ''
            if position == 'L':
                adjacent_seats = get_adjacent(layout, i, j)
                new_status = simulate_empty(adjacent_seats)
            elif position == '#':
                adjacent_seats = get_adjacent(layout, i, j)
                new_status = simulate_occupied(adjacent_seats)
            elif position == '.':
                new_status = '.'

            new_layout[i][j] = new_status
            
    return new_layout

def get_adjacent(layout, row, col):
    adjacent_seats = []
    if row > 0 and col > 0:
        adjacent_seats.append(layout[row-1][col-1])
    if row > 0:
        adjacent_seats.append(layout[row-1][col])
    if row > 0 and col < len(layout[row]) - 1:
        adjacent_seats.append(layout[row-1][col+1])
    if col < len(layout[row]) - 1:
        adjacent_seats.append(layout[row][col+1])
    if row < len(layout) - 1 and col < len(layout[row]) - 1:
        adjacent_seats.append(layout[row+1][col+1])
    if row < len(layout) - 1:
        adjacent_seats.append(layout[row+1][col])
    if row < len(layout)- 1 and col > 0:
        adjacent_seats.append(layout[row+1][col-1])
    if col > 0:
        adjacent_seats.append(layout[row][col-1])

    return adjacent_seats
        
def simulate_empty(seats):
    for seat in seats:
        if seat == '#':
            return 'L'
    return '#'

def simulate_occupied(seats):
    occupied = seats.count('#')

    if occupied < 4:
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
# print('output:')
# for row in stable_layout:
    # print(row)
num_occupied_seats = count_occupied_seats(stable_layout)
print(num_occupied_seats)
