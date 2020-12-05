INPUT = "2017-d12.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

import re
from collections import defaultdict
programs = defaultdict()

for string in strings:
  numbers = list(map(str, re.findall(r'\d+', string)))
  
  # create programs if they don't exist
  for x in numbers:
    if x not in programs:
      programs[x] = set([])

  # connect all programs from current list
  for x in numbers:
    for y in numbers[1:]:
      if x == y: continue
      if y not in programs[x]:
        programs[x].add(y)
      if x not in programs[y]:
        programs[y].add(x)

# go through all programs and connect with the programs in their direct connection
hasChanges = True
while hasChanges:
  hasChanges = False
  for x in programs:
    addToX = set([])
    for y in programs[x]:
      for z in programs[y]:
        if x == z: continue
        if z not in programs[x]:
          addToX.add(z)
    if len(addToX) > 0:
      hasChanges = True
      for z in addToX:
        programs[x].add(z)
        programs[z].add(x)

print(f"part 1: {len(programs['0']) + 1}") # 145

groups = set([])
for x in programs:
  prog = programs[x]
  prog.add(x)
  groups.add(','.join(sorted(prog)))

print(f"part 2: {len(groups)}")