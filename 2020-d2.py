INPUT = "2020-d2.txt"
strings = [string.strip('\n') for string in open(INPUT)]

part1 = 0
part2 = 0

for string in strings:
    splits = string.split(" ")
    minMax = splits[0].split("-")
    min = int(minMax[0])
    max = int(minMax[1])
    letter = splits[1][0]
    string = splits[2]

    count = string.count(letter)
    part1 += count >= min and count <= max
    
    part2 += (string[min-1] == letter) + (string[max-1] == letter) == 1

print(f"part 1: {part1}") # 548
print(f"part 2: {part2}") # 502