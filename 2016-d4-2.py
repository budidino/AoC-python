INPUT = "2016-d4.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

import collections
import re

candidates = []

for string in strings:
    # get number and remove it from string
    number = re.sub(r"\D", "", string)
    string = string.replace(number, "")

    # get checksum
    split = string.split("[", 1)
    checksum = split[1][:-1]

    # fix and sort remaining string
    string = split[0].replace("-", "")
    frequency = collections.Counter(sorted(string)).most_common()

    candidate = f"{frequency[0][0]}{frequency[1][0]}{frequency[2][0]}{frequency[3][0]}{frequency[4][0]}"
    if candidate == checksum:
        cleanedString = split[0].replace("-", " ")
        candidates.append(f"{cleanedString} {number}")

def cipher(string, rotations):
    result = ""
    for letter in string:
        if letter == " ":
            result += " "
            continue

        letterCode = ord(letter) + rotations
        if letterCode > 122:
            letterCode -= 26
        
        result += chr(letterCode)

    # print(result) # funny

    return "north" in result

for string in candidates:
    number = re.sub(r"\D", "", string)
    string = string.replace(number, "")

    if cipher(string, int(number) % 26):
        print(number)