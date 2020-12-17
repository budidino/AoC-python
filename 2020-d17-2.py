INPUT = "2020-d17.txt"
strings = [string.strip('\n').replace(".", "0").replace("#", "1") for string in open(INPUT)]

from collections import defaultdict
m = defaultdict()

initialWH = len(strings[0])
minVal = (-1, -1, -1, -1)
maxVal = (initialWH, initialWH, 1, 1)

# OPTIMIZATIONS:
# since the results are mirrored compared to z=0 we can always look at z=-1 as z=0 and never need to calculate anything z<0
# as we add value 1 (#) we can observer x, y, z position so we can know which min/max coordinates we should check in the next cycle

# populate initial data
for x in range(len(strings[0])):
  for y in range(len(strings)):
    m[(x, y, 0, 0)] = int(strings[y][x])

def activeNeighbours(pos):
  count = 0
  for x in range(pos[0]-1, pos[0]+2):
    for y in range(pos[1]-1, pos[1]+2):
      for z in range(pos[2]-1, pos[2]+2):
        for w in range(pos[3]-1, pos[3]+2):
          if pos != (x, y, z, w):
            count += m.get((x, y, z, w), 0)
  return count

def cycle():
  toUpdate = defaultdict()
  for x in range(minVal[0], maxVal[0]):
    for y in range(minVal[1], maxVal[1]):
      for z in range(minVal[2], maxVal[2]):
        for w in range(minVal[3], maxVal[3]):
          pos = (x,y,z,w)
          active = activeNeighbours(pos)
          val = m.get(pos, 0)
          if val == 1 and active not in [2, 3]:
            toUpdate[pos] = 0
          elif val == 0 and active == 3:
            toUpdate[pos] = 1
  
  for key, val in toUpdate.items():
    m[key] = val

numCycles = 0
while numCycles < 6:
  minVal = (-1 - numCycles, -1 - numCycles, -1 - numCycles, -1 - numCycles)
  maxVal = (initialWH + numCycles + 1, initialWH + numCycles + 1, numCycles + 2, numCycles + 2)
  cycle()
  numCycles += 1

part2 = 0
for x in range(minVal[0], maxVal[0]):
  for y in range(minVal[1], maxVal[1]):
    for z in range(minVal[2], maxVal[2]):
      for w in range(minVal[3], maxVal[3]):
        part2 += m.get((x,y,z,w), 0)

print(f"part 2: {part2}") # 2440