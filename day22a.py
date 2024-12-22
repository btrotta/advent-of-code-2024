from utilities import *

arr = parse_single_int(False)

prune = lambda x: x % 16777216


def step(x):
    x = prune(x ^ (x * 64))
    x = prune(x ^ (x // 32))
    x = prune(x ^ (x * 2048))
    return x


ans = 0
for a in arr:
    for i in range(2000):
        a = step(a)
    ans += a
print(ans)

