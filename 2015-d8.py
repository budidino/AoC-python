INPUT = "2015-d8.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

def calculatePart1(strings):
  literal, memory = 0, 0
  for string in strings:
    literal += len(string)

    skipNext = 0
    memoryString = ""
    for index, char in enumerate(string):
      if skipNext:
        skipNext -= 1
        continue

      if char == "\\":
        nextChar = string[index+1]
        if nextChar == "x":
          skipNext = 3
        else:
          skipNext = 1
        memoryString += "O"
        continue
      
      memoryString += char
    memory += len(memoryString) - 2
  return literal - memory

def calculatePart2(strings):
  literal, encoded = 0, 0
  for string in strings:
    literal += len(string)
    encoded += len(string.replace("\"", "OO").replace("\\", "OO")) + 2
  return encoded - literal

print(f"part 1: {calculatePart1(strings)}") # 1342
print(f"part 2: {calculatePart2(strings)}") # 2074