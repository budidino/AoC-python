INPUT = "2020-d16.txt"
groups = open('2020-d16.txt').read().replace("nearby tickets:\n", "").replace("your ticket:\n", "").split('\n\n')

from collections import defaultdict
dic = defaultdict()
validTicketParts = set()

def splitAndAddToValid(data):
  validInSection = set()
  for d in data:
    low, high = d.split("-")
    for i in range(int(low), int(high)+1):
      validTicketParts.add(i)
      validInSection.add(i)
  return validInSection

for row in groups[0].split('\n'):
  section, data = row.split(": ")
  dic[section] = splitAndAddToValid(data.split(" or ")) # sends: ["6-11", "33-44"]

tickets = groups[2].split("\n")
validTickets = []
for ticket in tickets:
  isValid = True
  ticketValues = []
  for ticketPart in map(int, ticket.split(",")):
    if ticketPart in validTicketParts:
      ticketValues.append(ticketPart)
    else:
      isValid = False
  if isValid:
    validTickets.append(ticketValues)
# print(validTickets)

def getAllPartsAtIndex(index):
  res = set()
  for ticket in validTickets:
    res.add(ticket[index])
  return res

part2 = 1
for i in range(0, len(validTickets[0])):
  subset = getAllPartsAtIndex(i)

  for key, val in dic.items():
    if subset.issubset(val):
      print(i, key)

  # if it fits "departure" multiply with part2

print(part2)

# print(dic)

