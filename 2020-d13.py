INPUT = "2020-d13.txt"
strings = [string.strip('\n') for string in open(INPUT)]

part1, part2 = 0, 0

startTime = int(strings[0])
bussesP1 = list(map(int, strings[1].replace(",x", "").split(",")))
busses = list(map(int, strings[1].replace(",x", ",0").split(",")))

def findFirstBus(startTime, busses):
  timePassed = 0
  while True:
    for bus in busses:
      if (startTime+timePassed) % bus == 0:
        return bus * timePassed
    timePassed += 1

def findAllBusses(time, busses):
  foundBusses = 0
  increment = 1
  while foundBusses < len(busses):
    if busses[foundBusses] == 0:
      foundBusses += 1
      continue
    time += increment
    if (time + foundBusses) % busses[foundBusses] == 0:
      increment *= busses[foundBusses]
      foundBusses += 1
  return time

part1 = findFirstBus(startTime, bussesP1)
print(f"part 1: {part1}") # 5946

part2 = findAllBusses(startTime, busses)
print(f"part 2: {part2}") # 645338524823718