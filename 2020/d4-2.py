#! usr/bin/python

import re

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
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #'cid'
    for reqField in requiredFields:
        if reqField not in ppFields:
            return False

    return validateFields(passport)

def validateFields(passport):
    validationStatus = True

    if len(passport['byr']) != 4:
        return False
    birthYear = int(passport['byr'])
    if birthYear < 1920 or birthYear > 2002:
        return False

    if len(passport['iyr']) != 4:
        return False
    issueYear = int(passport['iyr'])
    if issueYear < 2010 or issueYear > 2020:
        return False

    if len(passport['eyr']) != 4:
        return False
    expirationYear = int(passport['eyr'])
    if expirationYear < 2020 or expirationYear > 2030:
        return False

    height = passport['hgt']
    if len(height) < 3:
        return False
    if not validateHeight(height):
        return False

    hairColor = passport['hcl']
    if hairColor[0] != '#' and len(hairColor) != 7:
        return False
    if not validateHairColor(hairColor[1:]):
        return False

    eyeColor = passport['ecl']
    eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if eyeColor not in eyeColors:
        return False

    passportID = passport['pid']
    if len(passportID) != 9:
        return False
    if not validatePID(passportID):
        return False

    return True

def validatePID(passportID):
    pattern = re.compile('[0-9]+')
    return pattern.fullmatch(passportID) != None

def validateHeight(height):
    units = height[-2:]
    value = int(height[:-2])
    
    if units == 'cm':
        return value >= 150 and value <= 193
    elif units == 'in':
        return value >= 59 and value <= 76
    else:
        return False

def validateHairColor(hairColorValue):
    pattern = re.compile('[0-9a-f]+')
    return pattern.fullmatch(hairColorValue) != None
    
passportData = getData('input4.txt')
numValidPassports = validatePassports(passportData)
print(numValidPassports)
