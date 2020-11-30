INPUT = "2019-d5.txt"
array = list(map(int, open(INPUT).read().split(',')))

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
    else:
        return parameter

def run(code, input):
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
        if opcode == 99:
            shouldStop = True
    
    print("returning errors!")
    return errors[0]

print("part 1: ", run(array.copy(), 1))
print("part 2: ", run(array.copy(), 5))