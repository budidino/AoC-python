INPUT = "2015-d7.txt"
source = [string.rstrip('\n') for string in open(INPUT)]

import re
from collections import defaultdict
wires = defaultdict(int)

def int2bin(integer):
    if integer == 0:
        return "".join("0" * 16)
    else:
        return bin(integer)[2:].zfill(16)

def bin2int(binString):
    return int(binString, 2)

def runTheWires(strings):
    global wires
    toProcess = []
    while len(strings) > 0:
        toProcess = []
        for string in strings:
            splits = string.split(" ")
            if "NOT" == splits[0]:
                wireFrom = splits[1]
                wireTo = splits[3]
                if wireFrom in wires:
                    wires[wireTo] = wires[wireFrom].replace("1", "2").replace("0", "1").replace("2", "0")
                else:
                    toProcess.append(string)
            elif "AND" == splits[1] or "OR" == splits[1]:
                wireFrom1 = splits[0]
                wireFrom2 = splits[2]
                wireTo = splits[4]
                if wireFrom1 in wires and wireFrom2 in wires:
                    output = ""
                    if "AND" == splits[1]:
                        for i in range(16):
                            if wires[wireFrom1][i] == wires[wireFrom2][i] == "1":
                                output += "1"
                            else:
                                output += "0"
                    else: # OR
                        for i in range(16):
                            if wires[wireFrom1][i] == "1" or wires[wireFrom2][i] == "1":
                                output += "1"
                            else:
                                output += "0"
                    wires[wireTo] = output
                else:
                    toProcess.append(string)

            elif "LSHIFT" == splits[1] or "RSHIFT" == splits[1]:
                wireFrom = splits[0]
                shift = int(splits[2])
                wireTo = splits[4]
                if wireFrom in wires:
                    filler = "".join("0" * shift)
                    if "LSHIFT" == splits[1]:
                        wires[wireTo] = wires[wireFrom][shift:] + filler
                    else: # RSHIFT
                        wires[wireTo] = filler + wires[wireFrom][:-shift]
                else:
                    toProcess.append(string)
            else:
                toWire = splits[2]
                if splits[0].isdigit():
                    wires[toWire] = int2bin(int(splits[0]))
                elif splits[0] in wires:
                    wires[toWire] = wires[splits[0]]
                else:
                    toProcess.append(string)
        strings = toProcess

wires["1"] = "0000000000000001"
strings = source
runTheWires(strings)
part1 = bin2int(wires['a'])
print(f"part 1: {part1}") # 46065

wires = defaultdict(int)
wires["1"] = "0000000000000001"
strings = source
strings.remove("1674 -> b")
strings.append(f"{str(part1)} -> b")
runTheWires(strings)
part2 = bin2int(wires['a'])
print(f"part 2: {part2}") # 14134