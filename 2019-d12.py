INPUT = "2019-d12.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

import re

class Moon:
    position: [int] = [0, 0, 0]
    velocity: [int] = [0, 0, 0]
    velocityChange: [int] = [0, 0, 0]

class System:
    moons: [Moon] = []

    def applyGravity(self):
        for m1 in self.moons:
            m1.velocityChange = [0, 0, 0]
            for m2 in self.moons:
                if m1 == m2:
                    continue

                for i in range(3):
                    if m1.position[i] < m2.position[i]:
                        m1.velocityChange[i] += 1
                    elif m1.position[i] > m2.position[i]:
                        m1.velocityChange[i] -= 1

        for moon in self.moons:
            for i in range(3):
                moon.velocity[i] += moon.velocityChange[i]

        self.processVelocity()

    def processVelocity(self):
        for moon in self.moons:
            for i in range(3):
                moon.position[i] += moon.velocity[i]

    def totalEnergy(self) -> int:
        energy = 0
        for moon in self.moons:
            pot = 0
            kin = 0
            for num in moon.position:
                pot += abs(num)
            for num in moon.velocity:
                kin += abs(num)
            energy += pot * kin
        return energy

system = System()

for string in strings:
    numbers = list(map(int, re.findall(r'[-\d]+', string)))
    moon = Moon()
    moon.position = numbers
    moon.velocity = [0, 0, 0]
    system.moons.append(moon)
    
# for i in range(1000):
#     system.applyGravity()

# for moon in system.moons:
#     print(f"moon: {moon.position} - {moon.velocity}")

# print(f"part 1: {system.totalEnergy()}")
# 14809

# part 2

counter = 0
backToStart = False
while not backToStart:
    system.applyGravity()
    counter += 1
    if system.totalEnergy() == 0:
        print(f"{counter} - {system.totalEnergy()}")
    # if counter == 2775: #2772:
    #     backToStart = True

# 8064768 LOW

4686774924


# TASK INPUT
# <x=0, y=6, z=1>
# <x=4, y=4, z=19>
# <x=-11, y=1, z=8>
# <x=2, y=19, z=15>


# TEST 1: 2772 to repeat
# <x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>
