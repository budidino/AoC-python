INPUT = "2015-d2.txt"
string = [string.rstrip('\n') for string in open(INPUT)]

# part 1
total = 0
for s in string:
    values = s.split("x")
    values = sorted(list(map(int, values))) # convert string array to int array // and sort it
    side1 = 2 * values[0] * values[1]
    side2 = 2 * values[0] * values[2]
    side3 = 2 * values[1] * values[2]
    total += side1 + side2 + side3 + values[0] * values[1]

print(f"part 1: {total}")
# 1598415

# part 2
total = 0
for s in string:
    values = s.split("x")
    values = sorted(list(map(int, values))) # convert string array to int array // and sort it
    total += values[0] * values[1] * values[2] + values[0]*2 + values[1]*2

print(f"part 2: {total}")
# 3812909