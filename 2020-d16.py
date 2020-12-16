INPUT = "2020-d16.txt"
groups = open('2020-d16.txt').read().replace("nearby tickets:\n", "").replace("your ticket:\n", "").split('\n\n')

valid = set()

def splitAndAddToValid(data):
  for d in data:
    low, high = d.split("-")
    for i in range(int(low), int(high)+1):
      valid.add(i)

for row in groups[0].split('\n'):
  splitAndAddToValid(row.split(": ")[1].split(" or ")) # sends: ["6-11", "33-44"]
  
tickets = groups[2].replace("\n", ",")

part1 = 0
for ticket in map(int, tickets.split(",")):
  if ticket not in valid:
    part1 += ticket

print(f"part 1: {part1}") # 19240