start = 124075
end = 580769

def isAscending(number):
    s = str(number)
    return int(s[0]) <= int(s[1]) <= int(s[2]) <= int(s[3]) <= int(s[4]) <= int(s[5])

def isRepeating(number):
    string = str(number)
    for char in set(string):
        if string.count(char) >= 2:
            return True
    return False

def isRepeatingTwice(number):
    string = str(number)
    for char in set(string):
        if string.count(char) == 2:
            return True
    return False

part1, part2 = 0, 0

for i in range(start, end+1):
    if isAscending(i):
        if isRepeating(i):
            part1 += 1
            if isRepeatingTwice(i):
                part2 += 1

print("part 1:", part1)
print("part 2:", part2)
