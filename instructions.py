import os


#   PROCESSOR REGISTERS
REGA = 0
REGB = 0
REGC = 0
REGD = 0

#   PROCESSOR FLAGS

ZERO  = 0
CARRY = 0
FFLAG = 0


#   STACK MEMORY
STACK = []

#   RAM MEMORY
RAM = list(0 for i in range(256))
    
#   PROCESSOR INSTRUCTIONS
def MOV(destiny, value):
    global REGA, REGB, REGC, REGD
    if type(value) == int:
        match destiny.upper():
            case 'REGA':
                REGA = value
            case 'REGB':
                REGB = value
            case 'REGC':
                REGC = value
            case 'REGD':
                REGD = value

    elif type(value) == str:
        res = getRegister(value)
        MOV(destiny, res)

def PUSH(value):
    STACK.append(value)
    
def POP(destiny):
    value = STACK[-1]
    STACK.pop(-1)
    MOV(destiny, value)
    
def ADD(destiny, value):
    res = arithmetic(destiny, '+', value)
    MOV(destiny, res)
    
def SUB(destiny, value):
   res = arithmetic(destiny, '-', value)
   MOV(destiny, res)

def MUL(destiny, value):
    res = arithmetic(destiny, '*', value)
    MOV(destiny, res)
    
def DIV(destiny, value):
   res = arithmetic(destiny, '//', value)
   MOV(destiny, res)
    
def INC(destiny):
    ADD(destiny, 1)
def DEC(destiny):
    SUB(destiny, 1)
    
#   ROM FUNCTIONS

def arithmetic(destiny, operator, value):
    if type(value) == int:
        des = getRegister(destiny)
        res = eval(f'{des} {operator} {value}')
        return res
    elif type(value) == str:
        des = getRegister(destiny)
        val = getRegister(value)
        res = eval(f'{des} {operator} {val}')
        return res
    
def getRegister(reg):
    match reg.upper():
        case 'REGA':
            return REGA
        case 'REGB':
            return REGB
        case 'REGC':
            return REGC
        case 'REGD':
            return REGD
    
def printStack():
    print('Stack:', STACK)
    
def printRegisters():
    global REGA, REGB, REGC, REGD
    print(f"A: {REGA} B: {REGB} C: {REGC} D: {REGD}")
    
def printMachine():
    printRegisters()
    printStack()

def printRam():
    print('RAM :\n',RAM)

