INPUT = "2020-d13.txt"
strings = [string.strip('\n') for string in open(INPUT)]

part1, part2 = 0, 0

startTime = int(strings[0])
bussesP1 = list(map(int, strings[1].replace(",x", "").split(",")))
busses = list(map(int, strings[1].replace(",x", ",0").split(",")))
print(busses)

def findFirstBus(startTime, busses):
  timePassed = 0
  while True:
    for bus in busses:
      if (startTime+timePassed) % bus == 0:
        return bus * timePassed
    timePassed += 1

def modDiff(t, busses):
  for i, bus in enumerate(busses):
    if bus == 0: continue
    if (t+i) % bus != 0:
      return (False, i)
  return (True, i)

def findAllBusses(startTime, busses):
  startTime = startTime + (busses[0] - startTime % busses[0])
  timePassed = 0
  while True:
    t = startTime + timePassed
    res = modDiff(t, busses)
    if res[0]:
      return t
    timePassed += busses[0]

def findAllBusses2(startTime, increment, busses):
  timePassed = 0
  while True:
    t = startTime + timePassed
    res = modDiff(t, busses)
    if res[0]:
      return t
    timePassed += increment

part1 = findFirstBus(startTime, bussesP1)
print(f"part 1: {part1}") # 295

# find biggest increment number
# high = max(busses)
# highIndex = busses.index(high)
# part2 = findAllBusses2(high - highIndex, high, busses)
# print(f"part 2: {part2}") # 