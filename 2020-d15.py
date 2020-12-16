INPUT = "2020-d15.txt"
nums = list(map(int, open(INPUT).read().split(',')))

from collections import defaultdict
dic = defaultdict()

for i, num in enumerate(nums):
  if i == len(nums)-1: continue
  dic[num] = i+1
nextToAdd = (nums[-1], len(nums))

while len(nums) < 30000000:
  nextNum = dic.get(nums[-1], 0)
  if nextNum > 0:
    nextNum = len(nums) - nextNum
  # nextNum = 0 if nums[-1] not in dic.keys() else len(nums) - dic[nums[-1]]
  nums.append(nextNum)
  dic[nextToAdd[0]] = nextToAdd[1]
  nextToAdd = (nextNum, len(nums))

print(f"part 1: {nums[2020-1]}")  # 870
print(f"part 2: {nums[-1]}")      # 9136