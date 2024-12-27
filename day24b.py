import itertools
from copy import deepcopy
from utilities import *

arr = parse_single_string(False)

outputs = {}
for a in arr:
    if "->" in a:
        left, right = a.split(" -> ")
        a, op, b = left.split(" ")
        outputs[right] = ((a, b), op)


inputs = {}
op_lookup = {"AND": lambda a, b: a * b, "OR": lambda a, b: max(a, b), "XOR": lambda a, b: (a + b) % 2}

z_outputs = sorted([x for x in outputs if x.startswith("z")])
max_bit = int(z_outputs[-1][1:])


def get_outputs(x, inputs):
    if x in inputs:
        return inputs[x], []
    (a, b), op = outputs[x]
    op_fun = op_lookup[op]
    if a in inputs:
        a_val = inputs[a]
    else:
        a_val = get_outputs(a, inputs)
    if b in inputs:
        b_val = inputs[b]
    else:
        b_val = get_outputs(b, inputs)
    ans = op_fun(a_val, b_val)
    inputs[x] = ans
    return ans


def check_bit(bit, max_bit, wrong_bits):
    # check whether addition in this bit works
    checks = [((0, 0), (0, 0)), ((0, 1), (0, 1)), ((1, 0), (0, 1)), ((1, 1), (1, 0))]
    wrong_bit = False
    for (x, y), (z1, z0) in checks:
        x_inputs = {f"x{i:02d}": 0 for i in range(max_bit)}
        x_inputs[f"x{bit:02d}"] = x
        y_inputs = {f"y{i:02d}": 0 for i in range(max_bit)}
        y_inputs[f"y{bit:02d}"] = y
        z_inputs = {f"z{i:02d}": 0 for i in range(bit)}
        test_inputs = x_inputs
        test_inputs.update(y_inputs)
        test_inputs.update(z_inputs)
        test_outputs = []
        for curr_bit in [bit + 1, bit]:
            curr_output = get_outputs(f"z{curr_bit:02d}", deepcopy(test_inputs))
            test_outputs.append(curr_output)
        expected_outputs = [z1, z0]
        if expected_outputs[0] != test_outputs[0]:
            wrong_bits.add(bit + 1)
        if expected_outputs[1] != test_outputs[1]:
            wrong_bits.add(bit)
    return wrong_bit


wrong_bits = set()
for i in range(max_bit):
    check_bit(i, max_bit, wrong_bits)
print(wrong_bits)


def rename(rename_dict, outputs):
    new_name = lambda x: rename_dict[x] if x in rename_dict else x
    new_outputs = {}
    for x, ((a, b), op) in outputs.items():
        key = new_name(x)
        val = ((new_name(a), new_name(b)), op)
        new_outputs[key] = val
    return new_outputs


rename_dict = {}
for x, ((a, b), op) in outputs.items():
    if {a[0], b[0]} == {"x", "y"} and a[1:] == b[1:]:
        bit = a[1:]
        rename_dict[x] = f"x{bit}_{op}_y{bit}"
outputs = rename(rename_dict, outputs)


def swap(g1, g2, outputs):
    old_g1 = deepcopy(outputs[g1])
    old_g2 = deepcopy(outputs[g2])
    outputs[g1] = old_g2
    outputs[g2] = old_g1


reverse_rename_dict = {v: k for k, v in rename_dict.items()}
outputs = rename(reverse_rename_dict, outputs)

# solution omitted
swaps = []
for a, b in swaps:
    swap(a, b, outputs)

wrong_bits = set()
for i in range(max_bit):
    check_bit(i, max_bit, wrong_bits)
assert wrong_bits == set()

swapped_nodes = itertools.chain.from_iterable(swaps)
swapped_nodes = sorted(swapped_nodes)
ans = ",".join(swapped_nodes)
print(ans)
