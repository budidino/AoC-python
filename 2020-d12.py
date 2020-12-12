INPUT = "2020-d12.txt"
strings = [string.strip('\n') for string in open(INPUT)]

directionIndex = 1
positionX, positionY = 0, 0

def move(direction, distance):
  global positionX, positionY, directionIndex
  directions = ["N", "E", "S", "W"]

  if direction in ["R", "L"]:
    rotations = int(distance / 90)
    if    direction == "R": directionIndex += rotations
    elif  direction == "L": directionIndex -= rotations
    return
    
  if direction == "F":
    direction = directions[directionIndex%4]

  if    direction == "N": positionY += distance
  elif  direction == "S": positionY -= distance
  elif  direction == "E": positionX += distance
  else: positionX -= distance

for string in strings:
  direction = string[:1]
  distance = int(string[1:])
  move(direction, distance)

print("part 1: ", abs(positionX) + abs(positionY)) # 1710