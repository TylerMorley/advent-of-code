#! usr/bin/python

def getConfig(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f]
        modules = dict()
        for line in lines:
            name, destination = line.split(' -> ')
            destination = destination.split(', ')
            info = {'destination': destination}

            if name == 'broadcaster':
                modules[name] = info
            else:
                info['prefix'] = name[0]
                name = name[1:]
                modules[name] = info

        return modules

def sendPulse(pulse, config):
    pulse_type = pulse[0]
    module = config[pulse[1]]
    if module['prefix'] == '%' and pulse_type == 'low':
        if 'isOn' not in module or not module['isOn']:
            module['isOn'] = True
        else:
            module['isOn'] = False
    
    status = 'high' if module['isOn'] else 'low'
    destination = [[status, x] for x in module['destination']]
    config[pulse[1]] = module
    return [destination, config]
