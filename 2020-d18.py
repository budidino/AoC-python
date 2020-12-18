import re

INPUT = "2020-d18.txt"
strings = [string.strip('\n') for string in open(INPUT)]

def extract(num, opr):
  number = int(re.sub(r"\D", "", num))
  brackets = num.replace(str(number), "")
  return (number, opr, brackets) # brackets

def calc(n1, n2):
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
  while len(nums) > 1:
    n1 = nums[i]
    n2 = nums[i+1]

    if "(" in n2[2]:
      i += 1
      continue
    
    removedBrackets, n1 = calc(n1, n2)
    nums.pop(i)
    nums.pop(i)
    nums.insert(i, n1)

    if removedBrackets and i > 0:
      i -= 1
  return nums[0][0]

part1 = 0
for string in strings:
  part1 += process(string.split(" "))

print(f"part 1: {part1}") # 1890866893020