INPUT = "2020-d5.txt"
strings = [string.strip('\n').replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0") for string in open(INPUT)]

seats = []
for string in strings:
    seats.append(int(string, 2))

def findMySeat():
    for x in range(min(seats), max(seats)):
        if x not in seats:
            return x

print(f"part 1: {max(seats)}") # 832
print(f"part 2: {findMySeat()}") # 517