#! usr/bin/python3

def openFile(filename):
    with open(filename) as f:
        contents = f.read().strip()
        groupedContents = contents.split('\n\n')
        answerList = [group.split('\n') for group in groupedContents]
        return answerList

def countAnswers(answerList):
    count = 0
    for group in answerList:
        groupCount = countGroup(group)
        count += groupCount

    return count

def countGroup(groupAnswers):
    personTallyList = []
    for personAnswers in groupAnswers:
        personTally = countPerson(personAnswers)
        personTallyList.append(personTally)

    groupTally = personTallyList[0]
    for tally in personTallyList:
        groupTally = groupTally & tally
        
    return len(groupTally)

def countPerson(personAnswers):
    personTally = set()
    for answer in personAnswers:
        personTally.update(answer)

    return personTally
    
answerList = openFile('input6.txt')
countSum = countAnswers(answerList)
print(countSum)
