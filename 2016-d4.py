INPUT = "2016-d4.txt"
strings = [string.rstrip('\n') for string in open(INPUT)]

import collections
import re

result = 0

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
        result += int(number)

print(f"result: {result}") # 245102