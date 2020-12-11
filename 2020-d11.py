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
  changes = 0
  for row in range(wh):
    for col in range(wh):
      seat = s[row][col]
      if seat == ".": continue
      if seat == "L" and occupiedSeat(row, col, s) == 0:
        changes += 1
        strings[row] = strings[row][:col] + "#" + strings[row][col + 1:]
      elif seat == "#" and occupiedSeat(row, col, s) >= 4:
        changes += 1
        strings[row] = strings[row][:col] + "L" + strings[row][col + 1:]
  return changes

changes = 1
while changes != 0:
  changes = doTheMath(copy.deepcopy(strings))

part1 = 0
for string in strings:
  part1 += string.count("#")

print(f"part1: {part1}")