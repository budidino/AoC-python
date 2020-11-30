
# process input
INPUT = "input.txt"
numbers = [int(line.rstrip('\n')) for line in open(INPUT)]
numbers = array = list(map(int, open(INPUT).read().split(',')))
strings = [string.rstrip('\n') for string in open(INPUT)]
string = open(INPUT).read().rstrip('\n')
strings = open(INPUT).read().split(', ')

# creating dictionaries
from collections import defaultdict
dic = defaultdict(int)

# combinations and parmutations
import itertools
parmList = itertools.permutations(range(5), 5) # numbers 0-5 in groups of 5

# for
for number in numbers:
    print(number)
    break # stop the for loop

# for specific range
for x in range(0, 3): # or range(3)
    print(x) # numbers 0, 1, 2

# for through dic
for key, value in dic.items():
    print(key, value)

# for through string starting with index 1
for index, char in enumerate(string, start=1):
    print(index, char)

# while
not_found = True
while not_found:
    print("still not found")

# sum
sum(numbers, 0)

# array
someArray = []
someArray.append(3) # add to array

if item in my_list:
    # do something

# compare strings
import jellyfish as jf
if jf.levenshtein_distance("abc", "abx") == 1:
    print("string diff is only one character")

# strings
everyOther = string[0::2]           # get every 2nd character of string
firstCharacterOfString = string[:1] # get first char of string
withoutFirstCharacter = string[1:]  # remove first char from string

# extract all numbers from string
import re
number = int(re.sub(r"\D", "", string))

# md5
import hashlib
string = "abcdef".encode('utf-8')
encoded = hashlib.md5(string).hexdigest()

# regex - all numbers from a string
import re
numbers = list(map(int, re.findall(r'\d+', string))) # just positive numbers
numbers = list(map(int, re.findall(r'[-\d]+', string))) # also negative