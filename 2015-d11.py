string = "hxbxwxba"

def incrementString(index, string):
  letter = string[index]
  if ord(letter) == 122: # z
    string = string[:index] + "a" + string[index+1:]
    return incrementString(index-1, string)
  string = string[:index] + chr(ord(letter)+1) + string[index+1:]
  return string

def hasStraight(string):
  for char1, char2, char3 in zip(string, string[1:], string[2:]):
    if ord(char1) + 1 == ord(char2) and ord(char2) + 1 == ord(char3):
      return True
  return False

def hasGoodLetters(string):
  return "i" not in string and "o" not in string and "l" not in string

def hasTwoPairs(string):
  pairIndex = []
  index = 0
  for char1, char2 in zip(string, string[1:]):
    index += 1
    if char1 == char2:
      pairIndex.append(index)
      if len(pairIndex) > 1:
        if max(pairIndex) - min(pairIndex) >= 2:
          return True
  return False

def findNextPassword(string):
  foundPassword = False
  while not foundPassword:
    string = incrementString(len(string) - 1, string)
    foundPassword = hasStraight(string) and hasGoodLetters(string) and hasTwoPairs(string)
  return string

part1 = findNextPassword(string)
print(f"part 1: {part1}") # hxbxxyzz
print(f"part 2: {findNextPassword(part1)}") # hxcaabcc