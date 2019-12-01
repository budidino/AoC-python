INPUT = "2015-d3.txt"
string = open(INPUT).read().rstrip('\n')

from collections import defaultdict

dic = defaultdict(int) # dictionary of int values

def walkString(s):
    x = 0
    y = 0
    for d in s:
        if d == "^":
            y += 1
        elif d == "v":
            y -= 1
        elif d == ">":
            x += 1
        elif d == "<":
            x -= 1
    
        if not dic[f"{x}-{y}"]:
            dic[f"{x}-{y}"] = 1
        else:
            dic[f"{x}-{y}"] += 1

# part 1
dic = defaultdict(int) # dictionary of int values
dic["0-0"] = 1

walkString(string)

print(f"part 1: {len(dic)}")
# 2592

# part 2
dic = defaultdict(int) # dictionary of int values
dic["0-0"] = 2

walkString(string[::2])
walkString(string[1::2])

print(f"part 2: {len(dic)}")
# 2360