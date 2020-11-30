INPUT = "2019-d6.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

undiscovered = []
discovered = []

class Planet:
    name = ""
    parent = ""
    distance = -1

for string in strings:
    planet1 = string[:3]
    planet2 = string[4:]
    
    planet = Planet()
    planet.name = planet2
    planet.parent = planet1
    if planet2 != "COM":
        undiscovered.append(planet)

# for planet in planets:
#     if planet not in parentPlanet.keys():
#         print("no orbit - ", planet)
# COM is home

home = Planet()
home.distance = 0
home.name = "COM"
discovered.append(home)

while len(undiscovered) > 0:
    for planet in undiscovered:
        for parent in discovered:
            if planet.parent == parent.name:
                planet.distance = parent.distance + 1
                discovered.append(planet)
                undiscovered.remove(planet)

print("calculated distances")
part1 = 0
for planet in discovered:
    part1 += planet.distance
print("part1", part1)

from collections import defaultdict
distances = defaultdict()

# for planet in discovered:
#     if planet.name == "M1S" or planet.name == "JHP":
#         print(planet.name, planet.parent)

def findParent(name):
    for p in discovered:
        if p.name == name:
            #print(p.parent)
            return p.parent + findParent(p.parent)

print("part2 YOU")
you = findParent("YOU")

print("part2 SAN")
san = findParent("SAN")

print(you)
print(san)

print(you)[::-1]
print(san)[::-1]

# YOU - MV2 - JJT - N87 - HSZ - JHP - B86 = 236
# SAN - R5H - DRX - TQL - C45 - M1S - BNY = 208
# 442


# for key, value in parentPlanet.items():
#     print(key, value)
#print(parentPlanet)


