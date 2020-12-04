INPUT = "2015-d9.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

from collections import defaultdict
import itertools

cities = defaultdict()

for string in strings:
  destFrom, _, destTo, _, distance = string.split(" ")
  if destFrom not in cities:
    cities[destFrom] = defaultdict()
  if destTo not in cities:
    cities[destTo] = defaultdict()
  cities[destFrom][destTo] = int(distance)
  cities[destTo][destFrom] = int(distance)

def distanceForRoute(route):
  global cities
  distance = 0
  isValid = True
  
  for cityFrom, cityTo in zip(route, route[1:]):
    if cityTo in cities[cityFrom]:
      distance += cities[cityFrom][cityTo]
    else:
      isValid = False

  return (isValid, distance)

shortestDistance = 99999
longestDistance = 0

for route in itertools.permutations(cities.keys()):
  routeValid, routeDistance = distanceForRoute(route)
  if routeValid:
    if routeDistance < shortestDistance:
      shortestDistance = routeDistance
    if routeDistance > longestDistance:
      longestDistance = routeDistance
  
print(f"part 1 - shortest route: {shortestDistance}") # 207
print(f"part 2 - longest route: {longestDistance}") # 804