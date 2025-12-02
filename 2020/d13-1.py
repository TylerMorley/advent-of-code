#! usr/bin/python3

def openfile(filename):
    with open(filename) as f:
        earliest_time, bus_list = [line.strip() for line in f]
        bus_ids = bus_list.split(',')

        return [int(earliest_time), bus_ids]

def find_bus(earliest_time, buses):
    best_bus = 0
    best_depart_time = earliest_time * 2
    
    for entry in buses:
        if entry == 'x':
            continue
        else:
            bus = int(entry)

        depart_time = bus * ((earliest_time // bus) + 1)

        if depart_time < best_depart_time:
            best_bus = bus
            best_depart_time = depart_time

    wait_time = best_depart_time - earliest_time
    return [best_bus, wait_time]

earliest_time, bus_ids = openfile('input13.txt')
earliest_bus, wait_time = find_bus(earliest_time, bus_ids)
print(earliest_bus * wait_time)
