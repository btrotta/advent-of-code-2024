from utilities import *
from itertools import product
import operator

arr = parse_multi_string(False)

ans = 0
for a in arr:
    target = int(a[0][:-1])
    for ops in product([operator.mul, operator.add], repeat=len(a) - 2):
        curr_sum = 0
        for i in range(1, len(a) - 1):
            if i == 1:
                curr_sum += ops[i - 1](int(a[i]), int(a[i + 1]))
            else:
                curr_sum = ops[i - 1](curr_sum, int(a[i + 1]))
            if curr_sum > target:
                break
        if curr_sum == target:
            ans += target
            break

print(ans)