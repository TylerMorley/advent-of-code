#! usr/bin/python

def getPatterns(filename):
    with open(filename) as f:
        everything = [x.strip() for x in f]
        block = []
        patterns = []
        while len(everything) > 0:
            line = everything.pop(0)
            if line == '':
                patterns.append(block)
                block = []
            else:
                block.append(line)
        patterns.append(block)

        return patterns
