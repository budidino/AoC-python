INPUT = "2020-d14.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

from collections import defaultdict
import itertools
mem = defaultdict()
part2mem = []
mask = ""

def int2bin(integer):
  if integer == 0:
    return "".join("0" * 36)
  else:
    return bin(integer)[2:].zfill(36)

def part2process(b):
  returnArray = []
  floatingPoints = b.count("X")
  for product in itertools.product(["0", "1"], repeat=floatingPoints):
    newB = b
    for i in range(floatingPoints):
      newB = newB.replace("X", product[i], 1)
    returnArray.append(newB)
  return returnArray

def save(memIndex, val):
  b = str(int2bin(memIndex))
  resBin = ""
  for i in range(len(b)):
    if mask[i] == "X":
      resBin += "X"
    elif mask[i] == "1":
      resBin += "1"
    else:
      resBin += b[i]

  for a in part2process(resBin):
    mem[int(a, 2)] = val

for string in strings:
  left, right = string.split(" = ")
  if left == "mask":
    mask = right
  else:
    memIndex = int(left.split("[")[1].split("]")[0])
    overrideValue = int(right)
    save(memIndex, overrideValue)

part2 = 0
for val in mem.values():
  part2 += val

print(f"part 2: {part2}") # 3905642473893