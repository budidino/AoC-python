INPUT = "2020-d9.txt"
numbers = [int(line.rstrip('\n')) for line in open(INPUT)]

from itertools import combinations 

def isValid(numbers, number):
  for num1, num2 in combinations(numbers, 2):
    if num1 + num2 == number:
      return True
  return False

def findSuspect(numbers, preamble):
  for index, number in enumerate(numbers[preamble:], preamble):
    num = numbers[index-preamble:index]
    if not isValid(num, number):
      return number
  return 0

def findWeakness(numbers, suspect):
  low, high = 0, 2
  numSet = numbers[low:high]
  setSum = sum(numSet)
  while setSum != suspect:
    setSum = sum(numbers[low:high])
    if setSum + numbers[high] > suspect:
      low += 1
    elif setSum + numbers[high] < suspect:
      high += 1
    else:
      numSet = numbers[low:high+1]
      return min(numSet) + max(numSet)

suspect = findSuspect(numbers, 25)
print(f"part 1: {suspect}") # 257342611

weakness = findWeakness(numbers, suspect)
print(f"part 2: {weakness}") # 35602097