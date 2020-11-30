INPUT = "2016-d6.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

import collections

part1 = ""
part2 = ""

for index in range(0, len(strings[0])):
    letters = ""
    for string in strings:
        letters += string[index]
    frequency = collections.Counter(sorted(letters)).most_common()
    part1 += frequency[0][0]
    part2 += frequency[len(frequency)-1][0]
    
print(f"part 1: {part1}") # asvcbhvg
print(f"part 2: {part2}") # odqnikqv