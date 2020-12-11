INPUT = "2020-d11.txt"
strings = [string.strip('\n') for string in open(INPUT)]

import copy

wh = len(strings)

# WORK IN PROGRESS!!! MOREM OFFLINE :D

def isOccupied(x, y, dx, dy, s):
  cx = x
  cy = y
  print(cx, cy, "direction: ", dx, dy)
  while True:
    if not 0 < x < wh and not 0 < y < wh:
      return 0
    cx += dx
    cy += dy
    print("after ", cx, cy)
    seat = s[cx][cy]
    if seat == ".":
      continue
    return seat == "L"

def occupiedSeat(row, col, s):
  occupied = 0
  for x, y in [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (-1, -1)]:
    occupied += isOccupied(row, col, x, y, s)
  return occupied

def doTheMath(s):
  changes = 0
  for row in range(wh):
    for col in range(wh):
      seat = s[row][col]
      if seat == ".": continue
      if seat == "L" and occupiedSeat(row, col, s) == 0:
        changes += 1
        strings[row] = strings[row][:col] + "#" + strings[row][col + 1:]
      elif seat == "#" and occupiedSeat(row, col, s) >= 5:
        changes += 1
        strings[row] = strings[row][:col] + "L" + strings[row][col + 1:]
  return changes

for string in strings:
  print(string)

doTheMath(copy.deepcopy(strings))

print()

for string in strings:
  print(string)

# changes = 1
# while changes != 0:
#   changes = doTheMath(copy.deepcopy(strings))

# part1 = 0
# for string in strings:
#   part1 += string.count("#")

# print(f"part1: {part1}")