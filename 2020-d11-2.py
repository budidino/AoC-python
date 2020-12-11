INPUT = "2020-d11.txt"
strings = [string.strip('\n') for string in open(INPUT)]

import copy

wh = len(strings)

def isOccupied(x, y, dx, dy, s):
  while True:
    x += dx
    y += dy
    if 0 <= x < wh and 0 <= y < wh:
      seat = s[x][y]
      if seat == ".":
        continue
      return seat == "#"
    else:
      return 0

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

changes = 1
while changes != 0:
  changes = doTheMath(copy.deepcopy(strings))

part2 = 0
for string in strings:
  part2 += string.count("#")

print(f"part 2: {part2}") # 2119