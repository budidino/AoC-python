INPUT = "2015-d12.txt"
string = open(INPUT).read()

import re
import json

allNumbers = list(map(int, re.findall(r'[-\d]+', string)))
print(f"part 1: {sum(allNumbers)}") # 191164

def getObjectValue(data):
  if isinstance(data, int):
    return data
  elif isinstance(data, list):
    result = 0
    for obj in data:
      result += getObjectValue(obj)
    return result
  elif isinstance(data, dict):
    if "red" in data.values() or "red" in data:
      return 0
    result = 0
    for key in data:
      result += getObjectValue(data[key])
    return result
  else:
    return 0

print(f"part 2: {getObjectValue(json.loads(string))}") # 87842