from utilities import *

arr = parse_single_string(False)

registers = []
for a in arr:
    if a.startswith("Register"):
        registers.append(int(a.split(" ")[-1]))
    elif a.startswith("Program"):
        a = a.split(" ")[-1]
        program = [int(x) for x in a.split(",")]


def adv(pointer, registers):
    x = get_combo_operand(program[pointer + 1], registers)
    registers[0] = registers[0] // (2**x)
    return pointer + 2, None


def bxl(pointer, registers):
    registers[1] = registers[1] ^ program[pointer + 1]
    return pointer + 2, None


def bst(pointer, registers):
    x = get_combo_operand(program[pointer + 1], registers)
    registers[1] = x % 8
    return pointer + 2, None


def jnz(pointer, registers):
    if registers[0] != 0:
        return program[pointer + 1], None
    return pointer + 2, None


def bxc(pointer, registers):
    registers[1] = registers[1] ^ registers[2]
    return pointer + 2, None


def out(pointer, registers):
    x = get_combo_operand(program[pointer + 1], registers)
    return pointer + 2, x % 8


def bdv(pointer, registers):
    x = get_combo_operand(program[pointer + 1], registers)
    registers[1] = registers[0] // (2**x)
    return pointer + 2, None


def cdv(pointer, registers):
    x = get_combo_operand(program[pointer + 1], registers)
    registers[2] = registers[0] // (2**x)
    return pointer + 2, None


def get_combo_operand(x, registers):
    if x <= 3:
        return x
    if x == 4:
        return registers[0]
    if x == 5:
        return registers[1]
    if x == 6:
        return registers[2]
    else:
        print("error")


instructions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

ans = []
pointer = 0
while True:
    try:
        instruction = instructions[program[pointer]]
        pointer, res = instruction(pointer, registers)
        if res is not None:
            ans.append(res)
    except IndexError:
        break

ans_str = ",".join([str(x) for x in ans])
print(ans_str)

