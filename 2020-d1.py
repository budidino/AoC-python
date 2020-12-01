INPUT = "2020-d1.txt"
numbers = [int(line.rstrip('\n')) for line in open(INPUT)]

def part1():
    for num1 in numbers:
        for num2 in numbers:
            if num1 + num2 == 2020:
                return num1 * num2

def part2():
    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                if num1 != num2 and num2 != num3:
                    if num1 + num2 + num3 == 2020:
                        return num1 * num2 * num3

print(f"part 1: {part1()}")
print(f"part 2: {part2()}")