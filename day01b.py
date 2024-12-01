from utilities import *

x = parse_multi_int(sep="   ")
a, b = list(zip(*x))
a = np.array(sorted(a))
b = np.array(sorted(b))
ans = 0
for x in a:
    ans += x * np.sum(b == x)
print(ans)
