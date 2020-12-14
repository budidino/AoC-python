INPUT = "2020-d14.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

from collections import defaultdict
mem = defaultdict()
mask = ""

def int2bin(integer):
  if integer == 0:
    return "".join("0" * 36)
  else:
    return bin(integer)[2:].zfill(36)

def save(val, i):
  b = str(int2bin(val))
  resBin = ""
  for pos, bitVal in enumerate(b):
    resBin += bitVal if mask[pos] == "X" else mask[pos]
  mem[i] = resBin

for string in strings:
  left, right = string.split(" = ")
  if left == "mask":
    mask = right
  else:
    index = int(left.split("[")[1].split("]")[0])
    save(int(right), index)

part1 = 0
for m in mem.values():
  intVal = int(m, 2)
  part1 += intVal

print(f"part 1: {part1}") # 12512013221615