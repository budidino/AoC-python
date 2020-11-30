INPUT = "2016-d7.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

import collections
result = 0

def isABA(string):
    first = string[0]
    second = string[1]
    return first != second and f"{first}{second}{first}" == string

def isBAB(aba, bab):
    return bab[0] == aba[1] and bab[1] == aba[0] and bab[2] == aba[1]

def supportsSSL(brackets, outsides):
    for bracket in brackets:
        for i in range(0, len(bracket)-2):
            aba = bracket[i:i+3]
            if isABA(aba):
                for outside in outsides:
                    for i in range(0, len(outside)-2):
                        bab = outside[i:i+3]
                        if isBAB(aba, bab):
                            return True
    return False

for string in strings:
    outsides = []
    brackets = []

    while "[" in string:
        splits = string.split("[", 1)
        outsides.append(splits[0])
        splits = splits[1].split("]", 1)
        brackets.append(splits[0])
        string = splits[1]
    outsides.append(string)

    if supportsSSL(brackets, outsides):
        result += 1

print(f"result: {result}") # 242