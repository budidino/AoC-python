INPUT = "2015-d1.txt"
string = open(INPUT).read().rstrip('\n')

# part 1
floor = 0
for char in string:
    if char == "(":
        floor += 1
    else:
        floor -= 1

print(floor)

# part 2
floor = 0
for index, char in enumerate(string, start=1):
    if char == "(":
        floor += 1
    else:
        floor -= 1

    if floor < 0:
        print(index)
        break