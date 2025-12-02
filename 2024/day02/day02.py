#! usr/bin/env python

def getInputs(filename):
    with open(filename) as f:
        return [[int(x) for x in report.split(' ')] for report in f]

def compareLevels(levels):
    cur, nxt = levels
    difference = cur - nxt

    direction = ''
    if difference > 0:
        direction = 'decreasing'
    elif difference < 0:
        direction = 'increasing'
    else:
        direction = 'flat'

    gradation = abs(difference)

    return [direction, gradation]

def checkReportSafety(report):
    direction = None

    for i in range(len(report)-1):
        cur_direction, gradation = compareLevels([report[i], report[i+1]])
        
        if direction == None:
            direction = cur_direction
        elif direction != cur_direction:
            return [False, i]
        if gradation > 3 or gradation < 1:
            return [False, i]

    return [True, None]

def countSafeReports(reports, is_dampened=False):
    count = 0
    for report in reports:
        report_is_safe, i = checkReportSafety(report)
        if report_is_safe:
            count += 1
        elif is_dampened:
            if checkDampenedSafety(report, i) == True:
                count += 1
    return count

def checkDampenedSafety(report, i):
    indices = [i, i+1]
    if i > 0:
        indices.append(i-1)
    reports = []

    for j in indices:
        new_report = report.copy()
        new_report.pop(j)
        reports.append(new_report)
            
    dampened_safety = False
    for rep in reports:
        is_safe, k = checkReportSafety(rep)
        if is_safe:
            dampened_safety = True

    return dampened_safety

if __name__ == '__main__':
    filename = 'input02.txt'
    reports = getInputs(filename)
    safe_reports = countSafeReports(reports)
    print(f'part 1: {safe_reports}')

    dampened_reports = countSafeReports(reports, True)
    print(f'part 2: {dampened_reports}')
