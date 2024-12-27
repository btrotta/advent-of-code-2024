from utilities import *

arr = parse_single_string(False)

locks = set()
keys = set()
curr = None
height = 0
count = 0
for a in arr:
    if a == "":
        if is_lock:
            locks.add(tuple(curr))
            count += 1
        else:
            keys.add(tuple(curr))
            count += 1
        curr = None
        height = 0
    elif curr is None:
        is_lock = (a[0] == "#")
        curr = [0 for ch in a]
    else:
        height += 1
        if (not is_lock) and height == 6:
            continue
        for i, ch in enumerate(a):
            if ch == "#":
                curr[i] += 1
if is_lock:
    locks.add(tuple(curr))
    count += 1
else:
    keys.add(tuple(curr))
    count += 1

height -= 1
ans = 0
for a in locks:
    for b in keys:
        if all([a[i] + b[i] <= height for i in range(len(a))]):
            ans += 1
print(ans)
