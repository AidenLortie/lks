# Lolks Komputer System (LKS) Instruction set

## Introduction
The Lolks Komputer System is a bastardized set of computing instructions designed to be absolute hell (not really)

These instructions were created while i was bored and messing around with Python

## CPU

The CPU is a simple accumulator based CPU with 5 general purpose registers, a program counter, an accumulator, and 1024 memory locations

### Registers
- A - General purpose register
- B - General purpose register
- C - General purpose register
- D - General purpose register
- E - General purpose register
- NI - Program counter (Next Instruction)
- ACC - Accumulator

### Memory
The memory is a list of 1024 memory locations, each location can store a value from 0x0000 to 0xFFFF

### Program Counter
The program counter is a register that stores the location of the next instruction to be executed

### Accumulator
The accumulator is a register that stores the result of arithmetic operations


## Instructions

### Comments
Comments are denoted by a semicolon `;` and are ignored by the interpreter
```lks
; This is a comment
```

### Data Manipulation
#### SET
Takes in two arguments, the first being the register to set, and the second being the value to set it to
```lks
SET A 0x0011 ; Set register A to 0x0011
```

#### MOV
Takes in two arguments, the first being the register to move, and the second being the register to move it to
```lks
MOV AAC A;
```

#### MOM
Moves the value of the first register to the location in memory specified by the second register
```lks
SET A 0x0011 ; Set register A to 0x0011
SET B 0x0100 ; Set register B to 0x0100
MOM A B ; Move the value of register A to the location in memory specified by register B
```

### Arithmetic

#### ADD
Takes in two arguments, adds the values of the arguments, stores the result in the accumulator
```lks
SET A 0x0011 ; Set register A to 0x0011
SET B 0x0011 ; Set register B to 0x0011
ADD A B ; Add the values of registers A and B, store the result in the accumulator
```

#### SUB
Takes in two arguments, subtracts the second argument from the first, stores the result in the accumulator
```lks
SET A 0x0011 ; Set register A to 0x0011
SET B 0x0011 ; Set register B to 0x0011
SUB A B ; Subtract the value of register B from register A, store the result in the accumulator
```

#### MUL
Takes in two arguments, multiplies the values of the arguments
```lks
SET A 0x0011 ; Set register A to 0x0011
SET B 0x0011 ; Set register B to 0x0011
MUL A B ; Multiply the values of registers A and B, store the result in the accumulator
```

#### DIV
Takes in two arguments, divides the first argument by the second, stores the result in the accumulator
```lks
SET A 0x0011 ; Set register A to 0x0011
SET B 0x0011 ; Set register B to 0x0011
DIV A B ; Divide the value of register A by the value of register B, store the result in the accumulator
```

### Control Flow

#### CMP
Takes in two arguments, compares the values of the arguments
```lks
SET A 0x0011 ; Set register A to 0x0011
SET B 0x0011 ; Set register B to 0x0011
CMP A B ; Compare the values of registers A and B
```

#### JMP
Takes in one argument - Jumps to that line in the program
```lks
JMP 0x0001 ; Jump to line 0x0001
```

#### JE
Takes in one argument - Jumps to that line in the program if the previous comparison was equal
```lks
JE 0x0001 ; Jump to line 0x0001 if the previous comparison was equal
```

#### JNE
Takes in one argument - Jumps to that line in the program if the previous comparison was not equal
```lks
JNE 0x0001 ; Jump to line 0x0001 if the previous comparison was not equal
```

#### JG
Takes in one argument - Jumps to that line in the program if the previous comparison was greater
```lks
JG 0x0001 ; Jump to line 0x0001 if the previous comparison was greater
```

#### JL
Takes in one argument - Jumps to that line in the program if the previous comparison was less
```lks
JL 0x0001 ; Jump to line 0x0001 if the previous comparison was less
```

#### JGE
Takes in one argument - Jumps to that line in the program if the previous comparison was greater or equal
```lks
JGE 0x0001 ; Jump to line 0x0001 if the previous comparison was greater or equal
```

#### JLE
Takes in one argument - Jumps to that line in the program if the previous comparison was less or equal
```lks
JLE 0x0001 ; Jump to line 0x0001 if the previous comparison was less or equal
```

### INTERRUPTS

#### INT
Takes in one argument - Calls the interrupt specified by the argument

#### INT 0x00
Reads console input
```lks
INT 0x00 ; Read console input
```

#### INT 0x01
Prints the value of the accumulator to the console
```lks
INT 0x01 ; Print the value of the accumulator to the console
```

#### INT 0x02
Prints the value of the accumulator as a character to the console
```lks
INT 0x02 ; Print the value of the accumulator as a character to the console
```

#### INT 0x03
Outputs png from video memory
```lks
INT 0x03 ; Outputs png from video memory
```




