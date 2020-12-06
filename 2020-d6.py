INPUT = "2020-d6.txt"
strings = [string.strip('\n') for string in open(INPUT)]

answers = []
part1, part2 = 0, 0

def processPart1(answers):
  union = set()
  for a in answers:
    union.update(a)
  return len(union)

def processPart2(answers):
  intersect = answers[0]
  for a in answers[1:]:
    intersect &= a
  return len(intersect)

for string in strings:
  if string != "":
    answers.append(set(string))
  else:
    part1 += processPart1(answers)
    part2 += processPart2(answers)
    answers = []

print(f"part 1: {part1}") # 6587
print(f"part 2: {part2}") # 3235