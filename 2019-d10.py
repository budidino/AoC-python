INPUT = "2019-d10.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

import math

h = len(strings)
w = len(strings[0])
map = [[0 for x in range(w)] for y in range(h)]

class Asteroid:
    x: int
    y: int
    laserAngle: float = 0
    laserDistance: float = 0
    isVaporised = False
    
    def angleToAsteroid(self, a):
        radians = math.atan2(self.y - a.y, self.x - a.x)
        return (math.degrees(radians) + 270) % 360

    def distanceToAsteroid(self, laser):
        a = abs(self.x - laser.x)
        b = abs(self.y - laser.y)
        c = math.sqrt(a * a + b * b)
        return  c

asteroids = []

# detect and create asteroids
for y, row in enumerate(strings):
    for x, char in enumerate(row):
        if char == "#":
            a = Asteroid()
            a.x = x
            a.y = y
            asteroids.append(a)
            map[x].append(1)
        else:
            map[x].append(0)

# calculate visible asteroids / laser position
laser = asteroids[0]
maxVisible = 0
for a in asteroids:
    angles = set()
    for b in asteroids:
        if a == b:
            continue

        angle = a.angleToAsteroid(b)
        if angle not in angles:
            angles.add(angle)

    numVisible = len(angles)
    if numVisible > maxVisible:
        laser = a
        maxVisible = numVisible

print("part 1:", maxVisible)

# part 2

from collections import defaultdict
angles = defaultdict(int)

# calculate angles and distances from laser
for a in asteroids:
    if a == laser:
        continue

    angle = laser.angleToAsteroid(a)
    a.laserAngle = angle
    a.laserDistance = laser.distanceToAsteroid(a)

    if angle not in angles:
        angles[angle] = 1
    else:
        angles[angle] += 1

sortedAngles = sorted(angles.keys())

# vaporise asteroids
vaporised = 0
while vaporised < 200:
    for angle in sortedAngles:
        if angles[angle] > 0:
            candidates = []
            for a in asteroids:
                if a.laserAngle == angle and a.isVaporised == False and a.laserDistance != 0:
                    candidates.append(a)

            toVaporise = candidates[0]
            if len(candidates) > 1:
                closestDistance = 999999
                for a in asteroids:
                    if a.laserDistance == 0:
                        continue
                    if a.laserDistance < closestDistance:
                        closestDistance = a.laserDistance
                        toVaporise = a

            toVaporise.isVaporised = True
            angles[angle] -= 1
            vaporised += 1

            # debug
            # print(f"{vaporised}: {toVaporise.x}x{toVaporise.y} @ {angle}")

            if vaporised == 200:
                print(f"part 2: {toVaporise.x * 100 + toVaporise.y}")
                break
