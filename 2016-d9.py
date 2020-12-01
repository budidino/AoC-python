INPUT = "2016-d9.txt"
string = open(INPUT).read().rstrip('\n')

result = ""

while "(" in string:
    splits = string.split("(", 1)
    result += splits[0]
    
    splits = splits[1].split(")", 1)
    command = splits[0]
    remainder = splits[1]

    commandLen = int(command.split("x")[0])
    commandRepeat = int(command.split("x")[1])

    stringToRepeat = remainder[:commandLen]
    for _ in range(0, commandRepeat):
        result += stringToRepeat

    string = remainder[commandLen:]
result += string

print(f"part 1: {len(result)}") # 152851