INPUT = "2019-d3.txt"
wires = [string.rstrip('\n') for string in open(INPUT)]
wire1 = wires[0].split(',')
wire2 = wires[1].split(',')

from collections import defaultdict
path = defaultdict(int) # dictionary of int values

crossingDistances = []
crossingSteps = []

def walkTheWire(wire, isFirstWire):
    x, y, steps = 0, 0, 0

    for step in wire:
        direction = step[:1]
        distance = int(step[1:])

        while distance > 0:
            steps += 1
            distance -= 1
            if direction == "L":
                x -= 1
            elif direction == "R":
                x += 1
            elif direction == "U":
                y += 1
            else:
                y -= 1
            
            key = f"{x} {y}"
            if isFirstWire:
                path[key] = steps
            elif key in path:
                crossingDistances.append(abs(x) + abs(y))
                crossingSteps.append(path[key] + steps)

walkTheWire(wire1, True)
walkTheWire(wire2, False)

print(f"part 1: {min(crossingDistances)}")
print(f"part 2: {min(crossingSteps)}")