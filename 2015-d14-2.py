INPUT = "2015-d14.txt"
strings = [string.rstrip('\n').replace(".", "") for string in open(INPUT)]

from collections import defaultdict

raindeer = []

class Deer:
  flySpeed = 0
  flyDuration = 0
  restDuration = 0

  flightRemaining = 0
  restRemaining = 0
  distance = 0
  score = 0

  def __init__(self, flySpeed, flyDuration, restDuration):
    self.flySpeed = flySpeed
    self.flyDuration = flyDuration
    self.restDuration = restDuration
    
    self.flightRemaining = flyDuration
    self.restRemaining = 0
    self.distance = 0
    self.score = 0

for string in strings:
  deer, _, _, flySpeed, _, _, flyDuration, _, _, _, _, _, _, restDuration, _ = string.split(" ")
  newDeer = Deer(int(flySpeed), int(flyDuration), int(restDuration))
  raindeer.append(newDeer)

def moveDeer(deer):
  if deer.restRemaining > 0:
    deer.restRemaining -= 1
    if deer.restRemaining == 0:
      deer.flightRemaining = deer.flyDuration
  elif deer.flightRemaining > 0:
    deer.distance += deer.flySpeed
    deer.flightRemaining -= 1
    if deer.flightRemaining == 0:
      deer.restRemaining = deer.restDuration

for _ in range(2503):
  for deer in raindeer:
    moveDeer(deer)
  
  maxDistance = 0
  for index, deer in enumerate(raindeer):
    if deer.distance > maxDistance:
      maxDistance = deer.distance
  
  for deer in raindeer:
    if deer.distance == maxDistance:
      deer.score += 1

maxScore = 0
for deer in raindeer:
  if deer.score > maxScore:
    maxScore = deer.score

print(f"part 2: {maxScore}") # 1102