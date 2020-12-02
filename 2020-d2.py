INPUT = "2020-d2.txt"
strings = [string.strip('\n') for string in open(INPUT)]

part1, part2 = 0, 0
for string in strings:
    policy, password = string.split(': ')
    numbers, letter = policy.split(' ')
    minVal, maxVal = map(int, numbers.split('-'))
    part1 += minVal <= password.count(letter) <= maxVal
    part2 += (password[minVal-1] == letter) != (password[maxVal-1] == letter)
print(f"part 1: {part1}\npart 2: {part2}") # 548 # 502