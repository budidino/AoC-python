
# process input
INPUT = "input.txt"
numbers = [int(line.rstrip('\n')) for line in open(INPUT)]
numbers = array = list(map(int, open(INPUT).read().split(',')))
strings = [string.rstrip('\n') for string in open(INPUT)]
string = open(INPUT).read().rstrip('\n')
strings = open(INPUT).read().split(', ')
groups = open('2020-d7.txt').read().split('\n\n') # double enter separator

# creating dictionaries
from collections import defaultdict
dic = defaultdict(int)

# check var type
isinstance(var, list) # supports inheritance

# matrix
w, h = 50, 6
matrix = [[0] * w for _ in range(h)]

# combinations and parmutations
import itertools
pairsOfNumbers = itertools.combinations(numbers, 2)
for num1, num2 in itertools.combinations(numbers, 2): # loop pairs of numbers

# for
for number in numbers:
    print(number)
    break # stop the for loop

# for specific range
for x in range(0, 3): # or range(3)
    print(x) # numbers 0, 1, 2
for i in range(4, 12, 4):
    print(i) # numbers 4, 8 (not 12)

# for through dic
for key, value in dic.items():
    print(key, value)

# for through string starting with index 1
for index, char in enumerate(string, start=0):
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

# iterations
import itertools
for someList in itertools.combinations(report, 3): # all possible combinations of these 3 elements

# get pairs from array
names = ["mark", "philip", "john"]
for i1, i2 in zip(names, names[1:]):
  print(i1, i2) # mark, philip

# compare strings
import jellyfish as jf
if jf.levenshtein_distance("abc", "abx") == 1:
    print("string diff is only one character")

# strings
everyOther = string[0::2]   # get every 2nd character of string
first4 = string[:4]         # first 4 char
last4 = string[-4:]         # last 4 char
withoutFirst4 = string[4:]  # without first 4
withoutLast4 = string[:-4]  # without last 4

# md5
import hashlib
string = "abcdef".encode('utf-8')
encoded = hashlib.md5(string).hexdigest()

# regex - all numbers from a string
import re
number = int(re.sub(r"\D", "", string)) # all digits
numbers = list(map(int, re.findall(r'\d+', string))) # just positive numbers
numbers = list(map(int, re.findall(r'[-\d]+', string))) # also negative
# numbers = re.findall('^-?[0-9]\d*(\.\d+)?$', str) # array of all numbers

# useful set operations
s = set("123 ABC")
t = set("135 AZ")
intersect = s & t # or s.intersection(t)
exclusion = s ^ t # or s.symmetric_difference(t)
a_minus_b = s - t # or s.difference(t)
b_minus_a = t - s # or t.difference(s)

# set of all letters from a-z
from string import ascii_lowercase
letters = set(ascii_lowercase)

# measure performance
from time import time 
msStart = int(time() * 1000)
# heavy lifting
print(f"ms: {int(time() * 1000) - msStart}")