INPUT = "2016-d3.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

validTriangles = 0
row1 = []
row2 = []
row3 = []

for string in strings:
    chunks = string.split(' ')
    row1.append(int(chunks[0]))
    row2.append(int(chunks[1]))
    row3.append(int(chunks[2]))

def isTriangleValid(val1, val2, val3):
    values = []
    values.append(val1)
    values.append(val2)
    values.append(val3)
    values.sort()
    if values[0] + values[1] > values[2]:
        return True
    else:
        return False

def validTrianglesInArray(arr):
    global validTriangles
    index = 0
    while index < len(arr) - 2:
        if isTriangleValid(arr[index], arr[index+1], arr[index+2]):
            validTriangles += 1
        index += 3

validTrianglesInArray(row1)
validTrianglesInArray(row2)
validTrianglesInArray(row3)

print(f"valid triangles: {validTriangles}") # 1826