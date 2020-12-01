INPUT = "2016-d8.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

import re

w, h = 50, 6
matrix = [["."] * w for _ in range(h)]

def getRowAsString(row):
    global w, matrix
    string = ""
    for x in range(0, w):
        string += matrix[row][x]
    return string

def getColumnAsString(column):
    global h, matrix
    string = ""
    for y in range(0, h):
        string += matrix[y][column]
    return string

def draw(num1, num2):
    global matrix
    for y in range(0, num2):
        for x in range(0, num1):
            matrix[y][x] = "#"

def updateRow(row, string):
    global matrix
    for index, char in enumerate(string, start=0):
        matrix[row][index] = char

def updateColumn(column, string):
    global matrix
    for index, char in enumerate(string, start=0):
        matrix[index][column] = char

def shiftRow(row, amount):
    current = getRowAsString(row)
    new = current[-amount:] + current[:-amount]
    updateRow(row, new)

def shiftColumn(column, amount):
    current = getColumnAsString(column)
    new = current[-amount:] + current[:-amount]
    updateColumn(column, new)

def printPartOne():
    global matrix
    result = 0
    for y in range(0, h):
        for x in range(0, w):
            if matrix[y][x] == "#":
                result += 1
    print(result)

def printPartTwo():
    global w, h, matrix
    for y in range(0, h):
        row = getRowAsString(y)
        print(row)

for string in strings:
    if "rect " in string:
        splits = string.split("x")
        number1 = int(re.sub(r"\D", "", splits[0]))
        number2 = int(re.sub(r"\D", "", splits[1]))
        draw(number1, number2)
    elif "y=" in string:
        splits = string.split("y=")
        splits = splits[1].split(" by ")
        row = int(splits[0])
        shifts = int(splits[1])
        shiftRow(row, shifts)
    else:
        splits = string.split("x=")
        splits = splits[1].split(" by ")
        column = int(splits[0])
        shifts = int(splits[1])
        shiftColumn(column, shifts)

printPartOne() # 1115
printPartTwo() # EFEYKFRFIJ