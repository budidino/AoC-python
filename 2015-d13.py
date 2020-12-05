INPUT = "2015-d13.txt"
strings = [string.rstrip('\n').replace(".", "") for string in open(INPUT)]

from collections import defaultdict
import itertools

people = defaultdict()

for string in strings:
  person1, _, indicator, happiness, _, _, _, _, _, _, person2 = string.split(" ")
  if person1 not in people:
    people[person1] = defaultdict()
  if person2 not in people:
    people[person2] = defaultdict()
  if person2 not in people[person1]:
    people[person1][person2] = []
  if person1 not in people[person2]:
    people[person2][person1] = []
  multiply = 1
  if indicator == "lose":
    multiply = -1
  people[person1][person2].append(int(happiness) * multiply)
  people[person2][person1].append(int(happiness) * multiply)

def happinessForSeating(arrangement):
  global people
  happiness = 0
  
  for person1, person2 in zip(arrangement, arrangement[1:]):
    if person1 in people[person2]:
      happiness += sum(people[person1][person2])
  happiness += sum(people[arrangement[0]][arrangement[len(arrangement)-1]])
  return happiness

def maxHappinesWithPeople(people):
  mostHappiness = 0
  for arrangement in itertools.permutations(people.keys()):
    happiness = happinessForSeating(arrangement)
    if happiness > mostHappiness:
      mostHappiness = happiness
  return mostHappiness
  
print(f"part 1 - happiest: {maxHappinesWithPeople(people)}") # 709

myName = "Dino"
people[myName] = defaultdict()
for person in people:
  if person == myName: continue
  people[person][myName] = [0]
  people[myName][person] = [0]
print(f"part 2 - happiest with {myName}: {maxHappinesWithPeople(people)}") # 668