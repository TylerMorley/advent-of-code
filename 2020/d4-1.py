#! usr/bin/python

def getData(filename):
    passportFile = openfile(filename)
    passportList = splitPassports(passportFile)
    passportDict = listToDict(passportList)

    return passportDict
    
def openfile(filename):
    with open(filename) as f:
        passportFile = [line.strip() for line in f]
        return passportFile

def splitPassports(passportFile):
    passports = []
    currentPassport = []

    for line in passportFile:
        if line == '':
            passports.append(currentPassport)
            currentPassport = []

        else:
            fields = [field for field in line.split(' ')]
            currentPassport += fields

    passports.append(currentPassport)
            
    return passports

def listToDict(passportList):
    passports = []
    for pport in passportList:
        passport = {}
        for field in pport:
            key, val = field.split(':')
            passport.update({key:val})
        passports.append(passport)

    return passports

def validatePassports(passportDict):
    count = 0
    for passport in passportDict:
        if validatePassport(passport):
            count += 1

    return count

def validatePassport(passport):
    ppFields = passport.keys()
    for reqField in requiredFields:
        if reqField not in ppFields:
            return False
        
    return True

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #'cid'

passportData = getData('input4.txt')
numValidPassports = validatePassports(passportData)
print(numValidPassports)
