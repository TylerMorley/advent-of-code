#usr/bin/env python

def getInput(filename):
    with open(filename) as f:
        return [int(x) for x in f]

def mix(secret, to_mix):
    return secret ^ to_mix

def prune(secret):
    return secret % 16777216

def nextSecret(secret):
    to_mix = secret * 64
    secret = mix(secret, to_mix)
    secret = prune(secret)
    to_mix = secret // 32
    secret = mix(secret, to_mix)
    secret = prune(secret)
    to_mix = secret * 2048
    secret = mix(secret, to_mix)
    secret = prune(secret)

    return secret

def getChange(secret, next_secret):
    first = int(str(secret)[-1])
    nxt = int(str(next_secret)[-1])
    return nxt - first

def nextSecrets(secret, num, get_changes=False):
    changes = []
    last_secret = None
    for i in range(num):
        secret = nextSecret(secret)
        if get_changes and last_secret:
            changes.append(getChange(last_secret, secret))
        if not last_secret:
            last_secret = secret

    if get_changes:
        return [secret, changes]
    else:
        return secret

def allBuyers(secrets):
    score = 0
    for secret in secrets:
        score += nextSecrets(secret, 2000)
    return score

if __name__ == '__main__':
    filename = 'input22.txt'
    secrets = getInput(filename)
    score = allBuyers(secrets)
    print(f'Part 1: {score}')
