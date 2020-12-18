# TODO: brackets fuck things up... make sure to process brackets seperately
# probably best to take a different approach but I could still just fetch deepest brackets first and run process on them
# could be fun to find the deepest bracket in source string and then process it

import re

INPUT = "2020-d18.txt"
strings = [string.strip('\n') for string in open(INPUT)]

def extract(num, opr):
  number = int(re.sub(r"\D", "", num))
  brackets = num.replace(str(number), "")
  return (number, opr, brackets) # brackets

def calc(n1, n2):
  print(f"calc: ", n1, n2)
  removedBrackets = False
  brackets = n1[2]+n2[2]
  while "(" in brackets and ")" in brackets:
    brackets = brackets.replace("(", "", 1).replace(")", "", 1)
    removedBrackets = True # might be called multiple times but who gives a damn :D
    
  res = n1[0] + n2[0] if n1[1] == "+" else n1[0] * n2[0]
  return (removedBrackets, (res, n2[1], brackets)) # res, 2nd opr, cleaned brackets

def process(splits):
  nums = []
  for num, opr in zip(splits[::2], splits[1::2]):
    nums.append(extract(num, opr))
  nums.append(extract(splits[-1], "+"))

  i = 0
  additionOnly = True
  changes = 0
  while len(nums) > 1:
    n1 = nums[i]
    n2 = nums[i+1]
    print(i, n1, n2)

    shouldSkip = False
    if "(" in n2[2]:
      shouldSkip = True
      print(f"skip because n2 has (")
    if ")" in n1[2]:
      shouldSkip = True
      print(f"skip because n1 has )")
    if additionOnly and n1[1] == "*":
      shouldSkip = True
      print(f"skip because operation * while looking for +")
    
    removedBrackets = False
    if shouldSkip == False:
      removedBrackets, n1 = calc(n1, n2)
      changes += 1

      print(f"calc result: ", n1)
      nums.pop(i)
      nums.pop(i)
      nums.insert(i, n1)

      if additionOnly == False:
        additionOnly = True
        changes = 0
        i = 0
        continue

    if shouldSkip:
      i += 1

    if removedBrackets and i > 0:
      print("step back")
      i -= 1
    elif i == len(nums) - 1:
      print("go back to start")
      i = 0
      additionOnly = True if changes > 0 else False
      changes = 0
  return nums[0][0]

part1 = 0
for string in strings:
  part1 += process(string.split(" "))

print(f"part 1: {part1}") 
# 4952695568732 LOW - because I need to process brackets first



