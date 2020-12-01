INPUT = "2016-d7.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

result = 0

def hasABBA(string):
    first = string[0]
    second = string[1]
    return first != second and f"{first}{second}{second}{first}" == string

def checkBrackets(strings):
    for string in strings:
        for i in range(0, len(string)-3):
            substring = string[i:i+4]
            if hasABBA(substring):
                return False
    return True

def checkOutsides(strings):
    for string in strings:
        for i in range(0, len(string)-3):
            substring = string[i:i+4]
            if hasABBA(substring):
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

    if checkBrackets(brackets) and checkOutsides(outsides):
        result += 1


print(f"result: {result}") # 110