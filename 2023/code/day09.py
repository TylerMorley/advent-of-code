#! usr/bin/python

def getAnalysis(filename):
    with open(filename) as f:
        strings = [x.strip().split(' ') for x in f]
        analysis = []
        for line in strings:
            analysis.append([int(x) for x in line])

        return analysis

def getDifferences(line):
    differences = []
    cur_val = line[0]
    for i in range(1,len(line)):
        differences.append(line[i] - cur_val)
        cur_val = line[i]

    return differences

def hasAllZeros(line):
    return line == [0] * len(line)

def getAllDifferences(line):
    all_differences = [line]
    isZeros = False
    while isZeros == False:
        new_line = getDifferences(all_differences[-1])
        all_differences.append(new_line)
        if hasAllZeros(new_line):
            isZeros = True

    return all_differences

def extrapolate(report):
    current_diff = 0
    for i in range(len(report)-1, -1, -1):
        new_value = report[i][-1] + current_diff
        report[i].append(new_value)
        current_diff = new_value

    return report[0][-1]

def extrapolateBwd(report):
    current_diff = 0
    for i in range(len(report)-1, -1, -1):
        new_value = report[i][0] - current_diff
        report[i].append(new_value)
        current_diff = new_value

    return report[0][-1]

def getExtrValues(analysis, isBwd=False):
    sum_extrapolated = 0
    for line in analysis:
        differences = getAllDifferences(line)
        if isBwd:
            sum_extrapolated += extrapolateBwd(differences)
        else:
            sum_extrapolated += extrapolate(differences)

    return sum_extrapolated

if __name__ == '__main__':
    filename = 'inputs/input09.txt'
    analysis = getAnalysis(filename)
    sum_extr = getExtrValues(analysis)
    print(f'Part 1: {sum_extr}')

    sum_extr = getExtrValues(analysis, True)
    print(f'Part 2: {sum_extr}')
