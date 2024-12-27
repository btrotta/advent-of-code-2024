from utilities import *

arr = parse_single_string(False)

inputs = {}
outputs = {}
for a in arr:
    if "->" in a:
        left, right = a.split(" -> ")
        a, op, b = left.split(" ")
        if op == "AND":
            op_fun = lambda a, b: a * b
        elif op == "OR":
            op_fun = lambda a, b: max(a, b)
        elif op == "XOR":
            op_fun = lambda a, b: (a + b) % 2
        outputs[right] = [(a, b), op_fun]
    elif len(a) > 0:
        input, val = a.split(": ")
        inputs[input] = int(val)


def get_outputs(x):
    (a, b), op = outputs[x]
    if a in inputs:
        a_val = inputs[a]
    else:
        a_val = get_outputs(a)
    if b in inputs:
        b_val = inputs[b]
    else:
        b_val = get_outputs(b)
    ans = op(a_val, b_val)
    inputs[x] = ans
    return ans


z_outputs = sorted([x for x in outputs if x.startswith("z")])
ans = 0
for i, x in enumerate(z_outputs):
    ans += 2**i * get_outputs(x)
print(ans)
