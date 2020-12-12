INPUT = "2020-d12.txt"
strings = [string.strip('\n') for string in open(INPUT)]

positionX, positionY = 0, 0
waypointX, waypointY = 10, 1

def move(direction, number):
  global positionX, positionY, waypointX, waypointY

  if direction == "F":
    positionX += waypointX * number
    positionY += waypointY * number
    
  elif direction in ["N", "S", "E", "W"]:
    if    direction == "N": waypointY += number
    elif  direction == "S": waypointY -= number
    elif  direction == "E": waypointX += number
    else: waypointX -= number

  elif number == 180 and direction in ["L", "R"]:
    waypointX *= -1
    waypointY *= -1

  elif direction in ["L", "R"]:
    if direction == "L":
      if number == 90:  number = 270
      else:             number = 90

    # rotate right
    tempX = waypointX
    tempY = waypointY
    if number == 90:
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