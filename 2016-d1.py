INPUT = "2016-d1.txt"
strings = open(INPUT).read().split(', ')

directions = ["N", "E", "S", "W"]
directionIndex = 0 # North
distanceX = 0
distanceY = 0

def changeDirection(direction):
    global directionIndex
    if direction == "L":
        directionIndex -= 1
    else:
        directionIndex += 1

def walk(distance):
    global directions, directionIndex, distanceX, distanceY

    currentDirection = directions[directionIndex%4]
    if currentDirection == "N":
        distanceY += distance
    elif currentDirection == "S":
        distanceY -= distance
    elif currentDirection == "E":
        distanceX += distance
    else:
        distanceX -= distance

for string in strings:
    stepDirection = string[:1]
    changeDirection(stepDirection)

    stepDistance = int(string[1:])
    walk(stepDistance)

print(f"distance: {distanceX + distanceY}")