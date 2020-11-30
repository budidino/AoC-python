INPUT = "2019-d8.txt"
string = open(INPUT).read().rstrip('\n')
numbers = []
for c in string:
    number = int(c)
    numbers.append(int(c))

w = 25
h = 6
pixels = w*h

passCounter = 0
charCounter = 0
zeroDigitCounter = 0
oneDigitCounter = 0
twoDigitCounter = 0

minZeroDigits = 99999999
result = 0

for num in numbers:
    charCounter += 1
    if num == 0:
        zeroDigitCounter += 1
    elif num == 1:
        oneDigitCounter += 1
    elif num == 2:
        twoDigitCounter += 1

    if charCounter == pixels:
        charCounter = 0
        passCounter += 1
        if zeroDigitCounter < minZeroDigits:
            number = oneDigitCounter * twoDigitCounter
            minZeroDigits = zeroDigitCounter
            result = number
        
        zeroDigitCounter = 0
        oneDigitCounter = 0
        twoDigitCounter = 0  

print("part 1: ", result)
# not 2112

from collections import defaultdict
layers = defaultdict(int)

charCounter = 0
passCounter = 0
numberList = []

# create layers
for num in numbers:
    charCounter += 1
    numberList.append(num)
    if charCounter == pixels:
        layers[passCounter] = numberList
        charCounter = 0
        passCounter += 1
        numberList = []

resultList = layers[0]
for i in range(1, 99):
    for j in range(0, 149):
        if resultList[j] == 2 and layers[i][j] != 2:
            resultList[j] = layers[i][j]

mystring = ""
for digit in resultList:
    mystring += str(digit)

rowCount = 0
mystring = mystring.replace("2", " ")
mystring = mystring.replace("1", "░")
mystring = mystring.replace("0", "█")
for y in range(h):
    startingPixel = rowCount * w
    print(mystring[startingPixel:][:25])
    rowCount += 1

# FKAHL