INPUT = "2020-d3.txt"
worldMap = [string.strip('\n') for string in open(INPUT)]
mapWidth = len(worldMap[0])

def fly(right, down):
    trees, x, y = 0, 0, down

    while y < len(worldMap):
        x += right
        if worldMap[y][x % mapWidth] == "#":
            trees += 1
        y += down
    return trees

part1 = fly(3, 1)
part2 = fly(1, 1) * part1 * fly(5, 1) * fly(7, 1) * fly(1, 2)

print(f"part 1: {part1}") # 176
print(f"part 2: {part2}") # 5872458240