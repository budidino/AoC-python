INPUT = "2015-d5.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

### PART 1

# at least 3 vowels
# at least one letter twice in a row
# no bad strings

vowels = ["a", "e", "i", "o", "u"]
badStrings = ["ab", "cd", "pq", "xy"]

niceStrings = 0
for s in strings:
    vowelCount = 0
    hasDoubleLetter = False
    hasBadStrings = False
    
    for bad in badStrings:
        if bad in s:
            hasBadStrings = True
            #continue

    prevChar = ""
    for char in s:
        if char in vowels:
            vowelCount += 1
        if char == prevChar:
            hasDoubleLetter = True
        prevChar = char
        
    if vowelCount > 2 and hasDoubleLetter and not hasBadStrings:
        niceStrings += 1

print(f"part 1: {niceStrings}")


### PART 2

def hasPair(s):
    for a, b in zip(s, s[1:]):
        couple = f"{a}{b}"
        if s.count(couple) > 1:
            return True
    return False

def hasRepeatingLetter(s):
    for a, c in zip(s, s[2:]):
        if a == c:
            return True
    return False

niceStrings = 0
for s in strings:
    if hasPair(s) and hasRepeatingLetter(s):
        niceStrings += 1

print(f"part 2: {niceStrings}")

# 51