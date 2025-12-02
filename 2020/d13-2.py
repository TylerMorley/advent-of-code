#! usr/bin/python3

def openfile(filename):
    with open(filename) as f:
        earliest, bus_list = [line.strip() for line in f]
        bus_ids = bus_list.split(',')

        return bus_ids

def find_timestamp(buses):
    bus_info = organize(buses)
    timestamp = search_for_timestamp(bus_info)
    return timestamp

def organize(buses):
    position = 0
    buses_info = {}
    
    for bus in buses:
        if bus != 'x':
            bus_info = {'position':position}
            buses_info.update({int(bus):bus_info})
        position += 1
    return buses_info

def search_for_timestamp(buses):
    starting_bus = max(buses)
    step = starting_bus
    locked_in = [starting_bus]
    found_timestamp = False
    current_timestamp = (-1) * (buses[starting_bus]['position'])
    while not found_timestamp:
        if current_timestamp % 1000000 == 0:
            print(f'timestamp: {current_timestamp}')
        current_timestamp += step
        found_timestamp, locked_in, step = check_timestamp(buses, current_timestamp, locked_in, step)
        
    return current_timestamp

def check_timestamp(buses, timestamp, locked_in, step):
    if timestamp == 3417:
        print(f'timestamp: {timestamp}')
    found_timestamp = True
    for bus_number in buses:
        position = buses[bus_number]['position']
        next_departure = find_next_departure(timestamp, bus_number)
        if next_departure - position != timestamp:
            found_timestamp = False
        else:
            if bus_number not in locked_in:
                locked_in.append(bus_number)
                step *= bus_number
            
    return [found_timestamp, locked_in, step]

def find_next_departure(timestamp, bus_number):
    check = bus_number * (timestamp // bus_number)
    if check != timestamp:
        check += bus_number

    return check
    
bus_ids = openfile('example13-6.txt')
timestamp = find_timestamp(bus_ids)
print(timestamp)
