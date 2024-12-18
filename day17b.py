from utilities import *

arr = parse_single_string(False)

original_registers = []
for a in arr:
    if a.startswith("Register"):
        original_registers.append(int(a.split(" ")[-1]))
    elif a.startswith("Program"):
        a = a.split(" ")[-1]
        program = [int(x) for x in a.split(",")]


def run_program(reg_a):
    # this is what the program outputs after one iteration, then it jumps back to the start
    # and runs again with reg_a // 8 in register a
    return ((((reg_a % 8) ^ 5) ^ 6) ^ (reg_a // (2 ** ((reg_a % 8) ^ 5)))) % 8


def to_decimal(arr):
    return int("".join(str(x) for x in arr), 8)


to_visit = [[i for i in range(8) if run_program(i) == program[-1]]]
while len(to_visit) > 0:
    curr = to_visit.pop()
    reg_a = to_decimal(curr)
    position = len(program) - 1 - len(curr)
    target = program[position]
    new_reg_a = 8 * reg_a
    program_outputs = [run_program(new_reg_a + i) for i in range(8)]
    valid_digits = [i for i in range(8) if program_outputs[i] == target]
    if position == 0:
        ans = curr + [valid_digits[0]]
        break
    if valid_digits != []:
        to_visit += [curr + [v] for v in reversed(valid_digits)]
print(to_decimal(ans))
