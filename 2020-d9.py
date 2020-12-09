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
  low, high = 0, 1
  setSum = numbers[low] + numbers[high]
  while setSum != suspect:
    if setSum < suspect:
      high += 1
      setSum += numbers[high]
    else:
      setSum -= numbers[low]
      low += 1
  return min(numbers[low:high+1]) + max(numbers[low:high+1])

suspect = findSuspect(numbers, 25)
print(f"part 1: {suspect}") # 257342611

weakness = findWeakness(numbers, suspect)
print(f"part 2: {weakness}") # 35602097