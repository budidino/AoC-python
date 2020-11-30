INPUT = "2016-d1.txt"
strings = open(INPUT).read().split(', ')

directions = ["N", "E", "S", "W"]
directionIndex = 0 # North
distanceX = 0
distanceY = 0
visitedCoordinates = []
alreadyVisited = []

def changeDirection(direction):
    global directionIndex
    if direction == "L":
        directionIndex -= 1
    else:
        directionIndex += 1

def walk(distance):
    global directions, directionIndex, distanceX, distanceY, visitedCoordinates, alreadyVisited

    currentDirection = directions[directionIndex%4]

    while distance > 0:
        if currentDirection == "N":
            distanceY += 1
        elif currentDirection == "S":
            distanceY -= 1
        elif currentDirection == "E":
            distanceX += 1
        else:
            distanceX -= 1
        
        distance -= 1
        coordinate = f"{distanceX},{distanceY}"
        if coordinate in visitedCoordinates:
            alreadyVisited.append(distanceX + distanceY)
        else:
            visitedCoordinates.append(coordinate)

for string in strings:
    stepDirection = string[:1]
    changeDirection(stepDirection)

    stepDistance = int(string[1:])
    walk(stepDistance)

print(f"first already visited: {alreadyVisited[0]}") # 126