INPUT = "2020-d16.txt"
groups = open('2020-d16.txt').read().replace("nearby tickets:\n", "").replace("your ticket:\n", "").split('\n\n')

from collections import defaultdict
sectionSets = defaultdict()
validTicketParts = set()
myTicket = list(map(int, groups[1].split(",")))
part2 = 1
sections = defaultdict()
departureIndexSet = set()

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
  sectionSets[section] = splitAndAddToValid(data.split(" or ")) # sends: ["6-11", "33-44"]

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

def getAllPartsAtIndex(index):
  res = set()
  for ticket in validTickets:
    res.add(ticket[index])
  return res

def findNextSection():
  global part2
  for i in range(0, len(validTickets[0])):
    subset = getAllPartsAtIndex(i)
    validSections = []
    for key, val in sectionSets.items():
      if subset.issubset(val):
        validSections.append(key)

    if len(validSections) == 1:
      sectionName = validSections[0]
      if "departure " in sectionName:
        departureIndexSet.add(i)
        part2 *= myTicket[i]

      sections[sectionName] = i
      sectionSets.pop(sectionName, None)
      return

while len(departureIndexSet) < 6:
  findNextSection()

print(f"part 2: {part2}") # 21095351239483