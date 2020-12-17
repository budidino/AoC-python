INPUT = "2020-d17.txt"
strings = [string.strip('\n').replace(".", "0").replace("#", "1") for string in open(INPUT)]

from collections import defaultdict
m = defaultdict()
initialWH = len(strings[0])

# OPTIMIZATIONS:
# since the results are mirrored compared to z=0 we can always look at z=-1 as z=0 and never need to calculate anything z<0
# as we add value 1 (#) we can observer x, y, z position so we can know which min/max coordinates we should check in the next cycle

for x in range(len(strings[0])):
  for y in range(len(strings)):
    m[(x, y, 0)] = int(strings[y][x])

def activeNeighbours(pos):
  count = 0
  for x in range(pos[0]-1, pos[0]+2):
    for y in range(pos[1]-1, pos[1]+2):
      for z in range(pos[2]-1, pos[2]+2):
        if pos != (x, y, z):
          count += m.get((x, y, z), 0)
  return count

def cycle(i):
  toUpdate = defaultdict()
  for x in range(-1-i, initialWH+i+1):
    for y in range(-1-i, initialWH+i+1):
      for z in range(-1-i, i+2):
        pos = (x,y,z)
        active = activeNeighbours(pos)
        val = m.get(pos, 0)
        if val == 1 and active not in [2, 3]:
          toUpdate[pos] = 0
        elif val == 0 and active == 3:
          toUpdate[pos] = 1
  
  for key, val in toUpdate.items():
    m[key] = val

for i in range(6):
  cycle(i)

print(f"part 1: {sum(m.values())}") # 338