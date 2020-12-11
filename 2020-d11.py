INPUT = "2020-d11.txt"
strings = ["." + string.strip('\n') + "." for string in open(INPUT)]

import copy

wh = len(strings) + 2

# convenience
emptyRow = "." * wh
strings.insert(0, emptyRow)
strings.append(emptyRow)

def occupiedSeat(row, col, s):
  rowAbove = s[row-1][col-1:col+2]
  rowSame = s[row][col-1:col+2:2]
  rowUnder = s[row+1][col-1:col+2]
  return rowAbove.count("#") + rowUnder.count("#") + rowSame.count("#")

def doTheMath(s):
  hasChanges = False
  for row in range(wh):
    for col in range(wh):
      seat = s[row][col]
      if seat == ".": continue
      if seat == "L" and occupiedSeat(row, col, s) == 0:
        hasChanges = True
        strings[row] = strings[row][:col] + "#" + strings[row][col + 1:]
      elif seat == "#" and occupiedSeat(row, col, s) >= 4:
        hasChanges = True
        strings[row] = strings[row][:col] + "L" + strings[row][col + 1:]
  return hasChanges

hasChanges = True
while hasChanges:
  hasChanges = doTheMath(copy.deepcopy(strings))

part1 = 0
for string in strings:
  part1 += string.count("#")

print(f"part 1: {part1}") # 2361