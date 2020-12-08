INPUT = "2020-d8.txt"
strings = [string.strip('\n') for string in open(INPUT)]

from collections import defaultdict
program = defaultdict()

for index, string in enumerate(strings):
  command, value = string.split(" ")
  program[index] = (command, int(value))

def runProgram(prog):
  index, accumulator = 0, 0
  visited = set()
  while True:
    if index in visited:
      return (False, accumulator)
    elif index == len(prog):
      return (True, accumulator)
    visited.add(index)

    if prog[index][0] == "jmp":
      index += prog[index][1]
    else:
      if prog[index][0] == "acc":
        accumulator += prog[index][1]
      index += 1

def findWorkingProgram(program):
  for index in range(len(program)):
    cmnd = program[index][0]
    if cmnd == "nop" or cmnd == "jmp":
      newProg = program.copy()
      newCommand = "jmp" if cmnd == "nop" else "nop"
      newProg[index] = (newCommand, program[index][1])

      result = runProgram(newProg)
      if result[0] == True:
        return result[1]

print(f"part 1: {runProgram(program)[1]}") # 1337
print(f"part 2: {findWorkingProgram(program)}") # 1358