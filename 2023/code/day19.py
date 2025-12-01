#! usr/bin/python

def getInputs(filename):
    with open(filename) as f:
        in_file = f.read()
        str_workflows, str_parts = [x.strip() for x in in_file.split('\n\n')]

        list_workflows = [x.strip() for x in str_workflows.split('\n')]
        dict_workflows = dict()
        for workflow in list_workflows:
            name, flow = workflow[:-1].split('{')
            flow = flow.split(',')
            dict_workflows[name] = flow

        list_parts = [x.strip()[1:-1] for x in str_parts.split('\n')]
        parts = []
        for part in list_parts:
            part = [x.split('=') for x in part.split(',')]
            d_part = {x[0]:int(x[1]) for x in part}
            parts.append(d_part)

        return [dict_workflows, parts]
