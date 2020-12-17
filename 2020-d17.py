INPUT = "2020-d17.txt"
strings = [string.strip('\n').replace(".", "0").replace("#", "1") for string in open(INPUT)]

from collections import defaultdict
m = defaultdict()

minVal = (-1, -1, -1)
maxVal = (len(strings[0]), len(strings[0]), 1)

# OPTIMIZATIONS:
# since the results are mirrored compared to z=0 we can always look at z=-1 as z=0 and never need to calculate anything z<0
# as we add value 1 (#) we can observer x, y, z position so we can know which min/max coordinates we should check in the next cycle

# populate z = 0
for x in range(len(strings[0])):
  for y in range(len(strings)):
    m[(x, y, 0)] = int(strings[y][x])

def activeNeighbours(pos):
  count = 0
  for x in range(pos[0]-1, pos[0]+1):
    for y in range(pos[1]-1, pos[1]+1):
      for z in range(pos[2]-1, pos[2]+1):
        if pos != (x, y, z):
          count += m.get(pos, 0)
  return count

# If active and exactly 2 or 3 neighbors active = stay active else inactive
# If inactive but exactly 3 neighbors active = become active else remains inactive

def cycle():
  for x in range(minVal[0], maxVal[0]):
    for y in range(minVal[1], maxVal[1]):
      for z in range(minVal[2], maxVal[2]):
        pos = (x,y,z)
        active = activeNeighbours(pos)
        val = m.get(pos, 0)
        if val == 1 and active not in [2, 3]:
          m.pop(pos, None) # compare speed to: m[pos] = 0
        elif val == 0 and active == 3:
          m[pos] = 1

numCycles = 0
while numCycles < 1:
  cycle()
  numCycles += 1

# debug
print(m)
print(minVal)
print(maxVal)

# print(f"part 1: {part1}") # 
# print(f"part 2: {part2}") # 