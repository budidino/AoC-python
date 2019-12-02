INPUT = "2019-d2.txt"
array = list(map(int, open(INPUT).read().split(',')))

def process(arr, noun, verb):
    arr[1] = noun
    arr[2] = verb

    pointer = 0
    shouldStop = False

    while not shouldStop:
        opcode = arr[pointer]
        param1 = arr[pointer+1]
        param2 = arr[pointer+2]
        param3 = arr[pointer+3]

        if opcode == 1:
            arr[param3] = arr[param1] + arr[param2]
        elif opcode == 2:
            arr[param3] = arr[param1] * arr[param2]
        else:
            shouldStop = True

        pointer += 4

    return arr

# part 1
part1 = process(array.copy(), 12, 2)
print(f"part 1: {part1[0]}")

# part 2
for n in range(100):
    for v in range(100):
        part2 = process(array.copy(), n, v)
        if part2[0] == 19690720:
            print(f"part 2: {100 * n + v}")
