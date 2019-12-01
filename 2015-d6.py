INPUT = "2015-d6.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

import re # regex

w, h = 1000, 1000
grid = [[0 for x in range(w)] for y in range(h)]

for s in strings:
    operation = 2 # toggle
    if "on" in s:
        operation = 1 # on
    elif "off" in s:
        operation = 0 # off

    co = list(map(int, re.findall(r'\d+', s)))

    for x in range(co[0], co[2]+1):
        for y in range(co[1], co[3]+1):
            if operation == 2:
                if grid[x][y] == 0:
                    grid[x][y] = 1
                else:
                    grid[x][y] = 0
            else:
                grid[x][y] = operation
    
lightsOn = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        if grid[x][y] == 1:
            lightsOn += 1

print(f"part 1: {lightsOn}")

# 569999

# PART 2

grid = [[0 for x in range(w)] for y in range(h)]

for s in strings:
    operation = 2 # toggle
    if "on" in s:
        operation = 1 # on
    elif "off" in s:
        operation = 0 # off

    co = list(map(int, re.findall(r'\d+', s)))

    for x in range(co[0], co[2]+1):
        for y in range(co[1], co[3]+1):
            if operation == 2:
                grid[x][y] += 2
            elif operation == 1:
                grid[x][y] += 1
            elif grid[x][y] > 0:
                grid[x][y] -= 1
    
brightness = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        brightness += grid[x][y]

print(f"part 2: {brightness}")
# 17836115