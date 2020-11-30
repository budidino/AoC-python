INPUT = "2016-d2.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

coordinateX = 1
coordinateY = 1
result = ""

#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D

from collections import defaultdict
keypad = defaultdict(dict)
keypad[0][0] = ""
keypad[1][0] = ""
keypad[2][0] = "1"
keypad[3][0] = ""
keypad[4][0] = ""

keypad[0][1] = ""
keypad[1][1] = "2"
keypad[2][1] = "3"
keypad[3][1] = "4"
keypad[4][1] = ""

keypad[0][2] = "5"
keypad[1][2] = "6"
keypad[2][2] = "7"
keypad[3][2] = "8"
keypad[4][2] = "9"

keypad[0][3] = ""
keypad[1][3] = "A"
keypad[2][3] = "B"
keypad[3][3] = "C"
keypad[4][3] = ""

keypad[0][4] = ""
keypad[1][4] = ""
keypad[2][4] = "D"
keypad[3][4] = ""
keypad[4][4] = ""

def move(direction):
    global coordinateX, coordinateY
    if direction == "R":
        if coordinateX+1 < 5 and keypad[coordinateX+1][coordinateY] != "":
            coordinateX += 1
    elif direction == "L":
        if coordinateX-1 >= 0 and keypad[coordinateX-1][coordinateY] != "":
            coordinateX -= 1
    elif direction == "U":
        if coordinateY-1 >= 0 and keypad[coordinateX][coordinateY-1] != "":
            coordinateY -= 1
    else:
        if coordinateY+1 < 5 and keypad[coordinateX][coordinateY+1] != "":
            coordinateY += 1

def getNumberForCurrentCoordinates():
    global coordinateX, coordinateY, result
    result += str(keypad[coordinateX][coordinateY])

for string in strings:
    for index, char in enumerate(string, start=0):
        move(char)
    getNumberForCurrentCoordinates()
    
print(f"result: {result}") # C2C28