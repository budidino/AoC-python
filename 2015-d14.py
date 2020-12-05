INPUT = "2015-d14.txt"
strings = [string.rstrip('\n').replace(".", "") for string in open(INPUT)]

from collections import defaultdict
import itertools

raindeer = []

for string in strings:
  deer, _, _, speed, _, _, duration, _, _, _, _, _, _, rest, _ = string.split(" ")
  raindeer.append( (deer, int(speed), int(duration), int(rest)) )

def moveDeer(deer, raceDuration):
  flightRemaining = deer[2]
  restRemaining = 0
  distance = 0
  for _ in range(raceDuration):
    if restRemaining > 0:
      restRemaining -= 1
      if restRemaining == 0:
        flightRemaining = deer[2]
    elif flightRemaining > 0:
      distance += deer[1]
      flightRemaining -= 1
      if flightRemaining == 0:
        restRemaining = deer[3]
  return distance

maxDistance = 0
for deer in raindeer:
  distance = moveDeer(deer, 2503)
  if distance > maxDistance:
    maxDistance = distance

print(f"part 1: {maxDistance}") # 2640
