INPUT = "2016-d3.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

validTriangles = 0

for string in strings:
    chunks = string.split(' ')
    val1 = int(chunks[0])
    val2 = int(chunks[1])
    val3 = int(chunks[2])
    values = []
    values.append(val1)
    values.append(val2)
    values.append(val3)
    values.sort()

    if values[0] + values[1] > values[2]:
        validTriangles += 1

print(f"valid triangles: {validTriangles}") # 982