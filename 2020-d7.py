INPUT = "2020-d7.txt"
strings = [string.strip('\n') for string in open(INPUT)]

from collections import defaultdict
bags = defaultdict()

for string in strings:
  splits = string.split(" ")
  bagColor = splits[0]+splits[1]
  bags[bagColor] = []
  if splits[4] != "no":
    for i in range(4, len(splits), 4):
      count, name1, name2 = splits[i], splits[i+1], splits[i+2]
      bags[bagColor].append((int(count), f"{name1}{name2}"))

def find(bagSearch, inBag):
  for bag in bags[inBag]:
    if bagSearch in bag:
      return True
    if find(bagSearch, bag[1]):
      return True
  return False

def bagsIn(bagSearch):
  result = 0
  for bag in bags[bagSearch]:
    result += bag[0] + bag[0] * bagsIn(bag[1])
  return result

part1 = 0
for bag in bags:
  part1 += find("shinygold", bag)

part2 = bagsIn("shinygold")

print(f"part 1: {part1}") # 257
print(f"part 2: {part2}") # 1038