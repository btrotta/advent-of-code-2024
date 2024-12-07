from utilities import *
import operator

arr = parse_multi_string()

ops = [operator.mul, operator.add]
next_op = {ops[i]: ops[(i + 1) % len(ops)] for i in range(len(ops))}

ans = 0
for a in arr:
    ops_stack = []
    target = int(a[0][:-1])
    a = [target] + [int(x) for x in a[1:]]
    sum_stack = [0]
    while True:
        if len(ops_stack) == 0:
            ops_stack.append(ops[0])
        elif len(ops_stack) == len(a) - 2 and sum_stack[-1] == target:
            ans += target
            break
        else:
            if sum_stack[-1] > target or len(ops_stack) == len(a) - 2:
                while len(ops_stack) > 0 and ops_stack[-1] == ops[-1]:
                    ops_stack.pop()
                    sum_stack.pop()
                if len(ops_stack) == 0:
                    break
                ops_stack[-1] = next_op[ops_stack[-1]]
                sum_stack.pop()
            else:
                ops_stack.append(ops[0])
        i = len(ops_stack)
        curr_op = ops_stack[-1]
        if i == 1:
            new_sum = curr_op(a[i], a[i + 1])
        else:
            new_sum = curr_op(sum_stack[-1], a[i + 1])
        sum_stack.append(new_sum)

print(ans)
