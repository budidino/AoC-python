INPUT = "2019-d9.txt"
array = list(map(int, open(INPUT).read().split(',')))

base = 0

def processInstruction(instruction):
    opcode = instruction % 100
    modesStr = str(instruction//100)[::-1] # remove opcode and reverse the result
    modes = [0, 0, 0]
    for i, c in enumerate(modesStr):
        modes[i] = int(c)
    return opcode, modes

def getValue(parameter, mode, code):
    if mode == 0:
        return code[parameter]
    if mode == 2:
        return code[base + parameter]
    else:
        return parameter

def run(code, input, base):
    errors = []
    pointer = 0
    shouldStop = False
    
    while not shouldStop:
        opcode, modes = processInstruction(code[pointer])

        if opcode == 1:
            p1 = getValue(code[pointer+1], modes[0], code)
            p2 = getValue(code[pointer+2], modes[1], code)
            p3 = code[pointer+3]
            code[p3] = p1 + p2
            pointer += 4
        elif opcode == 2:
            p1 = getValue(code[pointer+1], modes[0], code)
            p2 = getValue(code[pointer+2], modes[1], code)
            p3 = code[pointer+3]
            code[p3] = p1 * p2
            pointer += 4
        elif opcode == 3:
            p1 = code[pointer+1]
            code[p1] = input
            pointer += 2
        elif opcode == 4:
            p1 = getValue(code[pointer+1], modes[0], code)
            if code[pointer+2] == 99:
                return p1
            
            errors.append(p1)
            pointer += 2
        elif opcode == 5:
            p1 = getValue(code[pointer+1], modes[0], code)
            if p1 != 0:
                p2 = getValue(code[pointer+2], modes[1], code)
                pointer = p2
            else:
                pointer += 3
        elif opcode == 6:
            p1 = getValue(code[pointer+1], modes[0], code)
            if p1 == 0:
                p2 = getValue(code[pointer+2], modes[1], code)
                pointer = p2
            else:
                pointer += 3
        elif opcode == 7:
            p1 = getValue(code[pointer+1], modes[0], code)
            p2 = getValue(code[pointer+2], modes[1], code)
            p3 = code[pointer+3]
            if p1 < p2:
                code[p3] = 1
            else:
                code[p3] = 0
            pointer += 4
        elif opcode == 8:
            p1 = getValue(code[pointer+1], modes[0], code)
            p2 = getValue(code[pointer+2], modes[1], code)
            p3 = code[pointer+3]
            if p1 == p2:
                code[p3] = 1
            else:
                code[p3] = 0
            pointer += 4
        elif opcode == 9:
            p1 = getValue(code[pointer+1], modes[0], code)
            base += p1
            pointer += 2
        if opcode == 99:
            shouldStop = True
    
    print("returning errors!")
    return errors[0]

code = array.copy()
for i in range(99999999):
    code.append(0)

result = 0
while result == 0:
    result = run(code, 1, base)
    
print("part 1: ", result)
#print("part 2: ", run(array.copy(), 5))


# 203 too low