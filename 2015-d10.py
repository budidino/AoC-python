string = "1321131112"

def process(x): # TODO: improve :D
  result = ""
  while len(x) > 0:
    sameCount = len(x) - len(x.lstrip(x[0]))
    result += str(sameCount) + x[0]
    x = x[sameCount:]
  return result

for i in range(50):
  string = process(string)
  if i+1 == 40:
    print(f"part 1: {len(string)}") # 492982
  elif i+1 == 50:
    print(f"part 2: {len(string)}") # 6989950
  print(f"pass {i+1} = {len(string)}") # debug to see progress