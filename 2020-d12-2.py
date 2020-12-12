INPUT = "2020-d12.txt"
strings = [string.strip('\n') for string in open(INPUT)]

positionX, positionY = 0, 0
waypointX, waypointY = 10, 1

def move(direction, repeat):
  global positionX, positionY, waypointX, waypointY

  if direction == "F":
    positionX += waypointX * repeat
    positionY += waypointY * repeat
    return
    
  if direction in ["N", "S", "E", "W"]:
    if    direction == "N": waypointY += repeat
    elif  direction == "S": waypointY -= repeat
    elif  direction == "E": waypointX += repeat
    else: waypointX -= repeat
    return

  if repeat == 180 and direction in ["L", "R"]:
    waypointX *= -1
    waypointY *= -1
    return

  if direction == "L":
    if repeat == 90:  repeat = 270
    else:             repeat = 90

  # rotate right
  tempX = waypointX
  tempY = waypointY
  if repeat == 90:
    waypointX = tempY
    waypointY = -1 * tempX
  else: # 270
    waypointX = -1 * tempY
    waypointY = tempX
      
for string in strings:
  direction = string[:1]
  distance = int(string[1:])
  move(direction, distance)

print("part 2: ", abs(positionX) + abs(positionY)) # 62045