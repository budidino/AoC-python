INPUT = "2020-d2.txt"
strings = [string.strip('\n') for string in open(INPUT)]

part1, part2 = 0, 0

for string in strings:
    splits = string.split(" ")
    letter = splits[1][0]
    string = splits[2]
    minMaxSplit = splits[0].split("-")
    minVal = int(minMaxSplit[0])
    maxVal = int(minMaxSplit[1])

    part1 += minVal <= string.count(letter) <= maxVal
    part2 += (string[minVal-1] == letter) != (string[maxVal-1] == letter)

print(f"part 1: {part1}") # 548
print(f"part 2: {part2}") # 502