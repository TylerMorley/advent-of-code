#! usr/bin/python3

def openfile(filename):
    contents = []
    with open(filename) as f:
        contents = [line.strip() for line in f]

    return contents

def organize(dbFile):
    organizedFile = []
    for entry in dbFile:
        endOfPolicy = entry.find(':') + 1
        policy = organizePolicy(entry[:endOfPolicy - 1])
        password = entry[endOfPolicy:].strip()

        organizedFile.append([policy, password])

    return organizedFile

def organizePolicy(policy):
    hyphen = policy.find('-')
    space = policy.find(' ')
    
    minimum = int(policy[:hyphen])
    maximum = int(policy[hyphen + 1 : space])
    letter = policy[space:].strip()

    return [minimum, maximum, letter]
#consider using a dict

def validate(pwDatabase):
    count = 0
    for entry in pwDatabase:
        minimum = entry[0][0]
        maximum = entry[0][1]
        letter = entry[0][2]
        password = entry[1]

        frequency = password.count(letter)

        if frequency >= minimum and frequency <= maximum:
            count += 1
            
    return count

databaseFile = openfile('input2.txt')
passwordDatabase = organize(databaseFile)
numValidPasswords = validate(passwordDatabase)
print(numValidPasswords)
