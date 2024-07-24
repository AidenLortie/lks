"""
Instruction Description:
SET - Set register a to value b
ADD - add b to a and store in accumulator
SUB - subtract b from a and store in accumulator
MUL - multiply a by b and store in accumulator - NO FLOATING POINT
DIV - divide a by b and store in accumulator - NO FLOATING POINT
MOD - store the remainder of a divided by b in accumulator - NO FLOATING POINT
MOV - move b to a
MOM - move to memory address b from a
CMP - compare with value in RegisterA and stores result in COMP
CLR - clear a
JMP - jump to a
JE - jump to a if equal
JNE - jump to a if not equal
JG - jump to a if greater
JL - jump to a if less
JGE - jump to a if greater or equal
JLE - jump to a if less or equal
INT - interrupt 0x00 - read from input and store in A, 0x01 - write A to output
HLT - halt

Registers:
A - general purpose register
B - general purpose register
C - general purpose register
D - general purpose register
E - general purpose register
CMP - comparison register
NI - Index of next instruction
ACC - accumulator

Memory:
0x0000 - 0x00FF - general purpose memory
0x0100 - 0x01FF - video memory represents a 16 x 16 grid of pixels r, g, b, a

Interrupts:
0x00 - read from input and store in A
0x01 - write A to output
0x02 - output video memory to screen


Instructions:
SET A B
ADD A B
SUB A B
MUL A B
DIV A B
MOD A B
MOV A B
MOM A B
CMP A
JMP A
JE A
JNE A
JG A
JL A
JGE A
JLE A
INT A
"""
import numpy
from PIL import Image

registerA = 0
registerB = 0
registerC = 0
registerD = 0
registerE = 0

registerNI = 0
registerCOMP = 0
registerACC = 0

memory = numpy.zeros(1024, dtype=int)

instructFile = open("instruct.lks", "r")
instruct = instructFile.readlines()
instructFile.close()

def SET(a, b):
    global registerA, registerB, registerC, registerD, registerE, registerACC, registerCOMP, memory
    b = int(b, 0)
    if a == "A":
        registerA = b
    elif a == "B":
        registerB = b
    elif a == "C":
        registerC = b
    elif a == "D":
        registerD = b
    elif a == "E":
        registerE = b
    elif a == "ACC":
        registerACC = b
    elif a == "CMP":
        registerCOMP = b
    else:
        memory[int(a, 0)] = b


def ADD(a, b):
    global registerACC
    registerACC = a + b

def SUB(a, b):
    global registerACC
    registerACC = a - b

def MUL(a, b):
    global registerACC
    registerACC = a * b

def DIV(a, b):
    global registerACC
    registerACC = a // b

def MOD(a, b):
    global registerACC
    registerACC = a % b

def MOV(b, a):
    global registerA, registerB, registerC, registerD, registerE, registerACC, registerCOMP, memory
    # if a references a register (A, B, C, ACC, CMP) then set the value of that register to b
    # otherwise set the value of the memory address to b
    if a == "A":
        a = registerA
    elif a == "B":
        a = registerB
    elif a == "C":
        a = registerC
    elif a == "D":
        a = registerD
    elif a == "E":
        a = registerE
    elif a == "ACC":
        a = registerACC
    elif a == "CMP":
        a = registerCOMP
    else:
        a = memory[int(a, 0)]

    if b == "A":
        registerA = a
    elif b == "B":
        registerB = a
    elif b == "C":
        registerC = a
    elif b == "D":
        registerD = a
    elif b == "E":
        registerE = a
    else:
        memory[int(b, 0)] = a


def MOM(a, b):
    global registerA, registerB, registerC, registerD, registerE, registerACC, registerCOMP, memory
    if a == "A":
        a = registerA
    elif a == "B":
        a = registerB
    elif a == "C":
        a = registerC
    elif a == "D":
        a = registerD
    elif a == "E":
        a = registerE
    elif a == "ACC":
        a = registerACC
    elif a == "CMP":
        a = registerCOMP
    else:
        a = memory[int(a, 0)]

    if b == "A":
        b = registerA
    elif b == "B":
        b = registerB
    elif b == "C":
        b = registerC
    elif b == "D":
        b = registerD
    elif b == "E":
        b = registerE

    memory[b] = a

def CMP(a, b):
    global registerCOMP
    if a == b:
        registerCOMP = 0
    elif a > b:
        registerCOMP = 1
    else:
        registerCOMP = -1

def JMP(a):
    global registerNI
    registerNI = a

def JE(a):
    global registerNI, registerCOMP
    if registerCOMP == 0:
        registerNI = a

def JNE(a):
    global registerNI, registerCOMP
    if registerCOMP != 0:
        registerNI = a

def JG(a):
    global registerNI, registerCOMP
    if registerCOMP == 1:
        registerNI = a

def JL(a):
    global registerNI, registerCOMP
    if registerCOMP == -1:
        registerNI = a

def JGE(a):
    global registerNI, registerCOMP
    if registerCOMP >= 0:
        registerNI = a

def JLE(a):
    global registerNI, registerCOMP
    if registerCOMP <= 0:
        registerNI = a

def INT(a):
    global registerA
    if a == 0:
        registerA = int(input(), 0)
    elif a == 1:
        print(registerA)
    elif a == 2:
        videobuffer = numpy.reshape(memory[0x0100:0x0200], (16, 16))
        videoout = [[0 for x in range(16)] for y in range(16)]
        for i in range(16):
            for j in range(16):
                videoout[i][j] = (videobuffer[i][j], videobuffer[i][j], videobuffer[i][j])
        videoout = numpy.array(videoout, dtype=numpy.uint8)
        img = Image.fromarray(videoout)
        img.show()
        img.save("output.png")
    else:
        print("Invalid interrupt")

def HLT():
    exit()

def CLR(a):
    global registerA, registerB, registerC, registerACC, registerCOMP, memory, registerNI, registerD, registerE
    if a == "A":
        registerA = 0
    elif a == "B":
        registerB = 0
    elif a == "C":
        registerC = 0
    elif a == "D":
        registerD = 0
    elif a == "E":
        registerE = 0
    elif a == "ACC":
        registerACC = 0
    elif a == "CMP":
        registerCOMP = 0
    else:
        memory[a] = 0

def executeInstruction(lineIn):
    opcode = lineIn[0]
    a = 0
    b = 0
    if len(lineIn) > 1:
        a = lineIn[1]
        if a == "A":
            a = registerA
        elif a == "B":
            a = registerB
        elif a == "C":
            a = registerC
        elif a == "D":
            a = registerD
        elif a == "E":
            a = registerE
        elif a == "ACC":
            a = registerACC
        elif a == "CMP":
            a = registerCOMP
        elif a[0:3] == "m0x" and not opcode == "INT": # check if it is a memory address and not an interrupt
            a.strip("m")
            a = memory[int(a, 16)]
        else:
            a = int(a, 0)
    if len(lineIn) > 2:
        b = lineIn[2]
        if b == "A":
            b = registerA
        elif b == "B":
            b = registerB
        elif b == "C":
            b = registerC
        elif b == "D":
            b = registerD
        elif b == "E":
            b = registerE
        elif b == "ACC":
            b = registerACC
        elif b == "CMP":
            b = registerCOMP
        elif b[0:3] == "m0x":
            b.strip("m")
            b = memory[int(b, 16)]
        else:
            b = int(b, 0)

    if opcode == "SET":
        a = lineIn[1]
        b = lineIn[2]
        SET(a, b)
    elif opcode == "ADD":
        ADD(a, b)
    elif opcode == "SUB":
        SUB(a, b)
    elif opcode == "MUL":
        MUL(a, b)
    elif opcode == "DIV":
        DIV(a, b)
    elif opcode == "MOD":
        MOD(a, b)
    elif opcode == "MOV":
        a = lineIn[1]
        b = lineIn[2]
        MOV(a, b)
    elif opcode == "MOM":
        a = lineIn[1]
        b = lineIn[2]
        MOM(a,b)
    elif opcode == "CMP":
        CMP(a, b)
    elif opcode == "JMP":
        JMP(a)
    elif opcode == "JE":
        JE(a)
    elif opcode == "JNE":
        JNE(a)
    elif opcode == "JG":
        JG(a)
    elif opcode == "JL":
        JL(a)
    elif opcode == "JGE":
        JGE(a)
    elif opcode == "JLE":
        JLE(a)
    elif opcode == "INT":
        a = int(lineIn[1], 0)
        INT(a)
    elif opcode == "HLT":
        HLT()
    elif opcode == "CLR":
        a = lineIn[1]
        CLR(a)

def main(isGUI=False):
    global registerNI
    if not isGUI:
        while registerNI < len(instruct):
            line = instruct[registerNI]
            registerNI += 1
            line = line.split(";")[0]
            line = line.strip()
            if line == "":
                continue
            lineElem = line.split()
            executeInstruction(lineElem)
        else:
            print("Program finished execution - EOF")
    else:
        line = instruct[registerNI]
        registerNI += 1
        line = line.split(";")[0]
        line = line.strip()
        if line == "":
            pass
        lineElem = line.split()
        executeInstruction(lineElem)


if __name__ == "__main__":
    main()
