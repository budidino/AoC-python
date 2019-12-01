INPUT = "2019-d1.txt"
numbers = [int(line.rstrip('\n')) for line in open(INPUT)]

def fuel(number):
    return number // 3 - 2

# part 1
total = 0
for num in numbers:
    total += fuel(num)

print(f"part 1: {total}")

# part 2
total = 0
for num in numbers:
    fuelNeeded = fuel(num)
    while fuelNeeded > 0:
        total += fuelNeeded
        fuelNeeded = fuel(fuelNeeded)

print(f"part 2: {total}")
