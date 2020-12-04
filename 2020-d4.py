INPUT = "2020-d4.txt"
strings = [string.strip('\n') for string in open(INPUT)]

import re

part1, part2 = 0, 0

def validate(passport, checkDetails):
  valid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  passportPartsFound = []

  for entry in passport.split(" "):
    pKey, pVal = entry.split(":")
    if pKey in valid and pKey not in passportPartsFound:
      passportPartsFound.append(pKey)
      if not checkDetails: continue
      
      if pKey == "byr":
        if not pVal.isdigit() or not 1920 <= int(pVal) <= 2002:
          return 0
      if pKey == "iyr":
        if not pVal.isdigit() or not 2010 <= int(pVal) <= 2020:
          return 0
      if pKey == "eyr":
        if not pVal.isdigit() or not 2020 <= int(pVal) <= 2030:
          return 0
      if pKey == "hgt":
        number = int(re.sub(r"\D", "", pVal))
        if "cm" in pVal:
          if not 150 <= number <= 193:
            return 0
        elif "in" in pVal:
          if not 59 <= number <= 76:
            return 0
        else:
          return 0
      if pKey == "hcl":
        # alternative: re.match('^#[a-f0-9]{6}$', pVal)
        if pVal[0] != "#" or len(pVal) != 7:
          return 0
        for ch in pVal[1:]:
          if not ('a' <= ch <= 'z' or '0' <= ch <= '9'):
            return 0
      if pKey == "ecl":
        if not pVal in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
          return 0
      if pKey == "pid":
        # alternative: re.match('^[0-9]{9}$', pVal)
        if not pVal.isdigit() or len(pVal) != 9:
          return 0

  return len(passportPartsFound) == len(valid)

# build passports for processing
toProcess = []
currentPassport = ""
for string in strings:
  if string == "" and currentPassport != "":
    toProcess.append(currentPassport.lstrip())
    currentPassport = ""
  else:
    currentPassport += f" {string}"
toProcess.append(currentPassport.lstrip())

for passport in toProcess:
  part1 += validate(passport, False)
  part2 += validate(passport, True)

print(f"part 1: {part1}") # 170
print(f"part 2: {part2}") # 103