INPUT = "2020-d10.txt"
num = [int(line.rstrip('\n')) for line in open(INPUT)]

adapter = max(num) + 3
num.append(adapter)
num.append(0)
num = sorted(num)

diff1, diff3 = 0, 0
for num1, num2 in zip(num[:], num[1:]):
  if    num2 - num1 == 1: diff1 += 1
  elif  num2 - num1 == 3: diff3 += 1
print(f"part 1: {diff1 * diff3}") # 2277

from collections import defaultdict
dic = defaultdict()

totalLen = len(num)
for index in range(totalLen-1):
  dic[num[index]] = set()
  options = 0
  for i in range(1, 4):
    if totalLen-index > i and num[index+i] - num[index] <= 3:
      dic[num[index]].add(num[index+i])
      options += 1

revEng = defaultdict()
revEng[adapter] = 1
for val in num[::-1]:
  if val == num[len(num)-1]: 
    revEng[val] = 1
  else:
    total = 0
    for subVal in dic[val]:
      total += revEng[subVal]
    revEng[val] = total

print(f"part 2: {revEng[0]}") # 37024595836928