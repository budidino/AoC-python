INPUT = "2016-d9.txt"
string = open(INPUT).read().rstrip('\n')

result = 0

while "(" in string:
    splits = string.split("(", 1)
    result += len(splits[0])
    
    splits = splits[1].split(")", 1)
    command = splits[0]
    remainder = splits[1]

    commandLen = int(command.split("x")[0])
    commandRepeat = int(command.split("x")[1])

    stringToRepeat = remainder[:commandLen]
    stringToAppend = ""
    for _ in range(0, commandRepeat):
        stringToAppend += stringToRepeat

    string = stringToAppend + remainder[commandLen:]
result += len(string)

# slow but worked :D # TODO: optimize
print(f"part 2: {result}") # 11 797 310 782