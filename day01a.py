from utilities import *

x = parse_multi_int(sep="   ")
a, b = list(zip(*x))
a = sorted(a)
b = sorted(b)
print(np.sum(np.abs(np.array(a) - np.array(b))))
