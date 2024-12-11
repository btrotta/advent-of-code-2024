from utilities import *

arr = parse_multi_int(False)[0]

for blink in range(25):
    new_arr = []
    for a in arr:
        if a == 0:
            new_arr.append(1)
        else:
            str_a = str(a)
            if len(str_a) % 2 == 0:
                new_arr += [int(str_a[:len(str_a) // 2]), int(str_a[len(str_a) // 2:])]
            else:
                new_arr.append(a * 2024)
    arr = new_arr

print(len(arr))
