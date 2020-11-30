INPUT = "2016-d2.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

coordinateX = 1
coordinateY = 1
result = ""

from collections import defaultdict
keypad = defaultdict(dict)
keypad[0][0] = 1
keypad[1][0] = 2
keypad[2][0] = 3
keypad[0][1] = 4
keypad[1][1] = 5
keypad[2][1] = 6
keypad[0][2] = 7
keypad[1][2] = 8
keypad[2][2] = 9

def move(direction):
    global coordinateX, coordinateY
    if direction == "R":
        coordinateX += 1
    elif direction == "L":
        coordinateX -= 1
    elif direction == "U":
        coordinateY -= 1
    else:
        coordinateY += 1
    
    if coordinateX > 2:
        coordinateX = 2
    if coordinateX < 0:
        coordinateX = 0
    
    if coordinateY > 2:
        coordinateY = 2
    if coordinateY < 0:
        coordinateY = 0

def getNumberForCurrentCoordinates():
    global coordinateX, coordinateY, result
    result += str(keypad[coordinateX][coordinateY])

for string in strings:
    for index, char in enumerate(string, start=0):
        move(char)
    getNumberForCurrentCoordinates()
    
print(f"result: {result}") # 61529